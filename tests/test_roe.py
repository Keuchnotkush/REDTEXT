"""Tests for the Rules of Engagement (RoE) capture model.

Increment 1: the RulesOfEngagement data model and its validation. A valid
RoE is the authorization context that generation is later gated on (#36), so
"valid" has to mean *actually authorized* — a real signatory with named
authority, an in-scope/no-go boundary, and a way to abort — not merely
"the fields are populated".
"""

import pytest

from redtext_generator.engagement.roe import (
    EmergencyContact,
    RulesOfEngagement,
    Signatory,
)


def _valid_roe(**overrides):
    """Build a fully-authorized RoE, overriding individual fields per test."""
    base = dict(
        client_name="Acme Corp",
        engagement_name="2026 Q4 Phishing Assessment",
        scope_description="Authorized SE assessment of corporate email users.",
        allowed_vectors=["email-phishing", "vishing"],
        windows=["2026-12-01T09:00/2026-12-05T17:00"],
        authorized_signatories=[
            Signatory(
                name="Dana Reyes",
                title="CISO",
                authority="Written board delegation dated 2026-11-01",
            )
        ],
        out_of_scope=["C-suite home addresses", "production payroll system"],
        emergency_contacts=[
            EmergencyContact(name="Dana Reyes", role="CISO", phone="+1-555-0100")
        ],
        abort_conditions=["Any real credential is captured and not in scope"],
        data_jurisdiction="US-CA",
        deconfliction="Notify SOC lead before each wave; 30-min deconfliction window.",
    )
    base.update(overrides)
    return RulesOfEngagement(**base)


def test_fully_populated_roe_is_valid():
    roe = _valid_roe()
    assert roe.validate() == []
    assert roe.is_valid() is True


def test_missing_client_name_is_invalid():
    roe = _valid_roe(client_name="")
    errors = roe.validate()
    assert roe.is_valid() is False
    assert any("client" in e.lower() for e in errors)


def test_no_signatories_is_invalid():
    roe = _valid_roe(authorized_signatories=[])
    errors = roe.validate()
    assert roe.is_valid() is False
    assert any("signator" in e.lower() for e in errors)


def test_signatory_without_authority_is_invalid():
    """A name on a form is not authorization — the authority must be stated."""
    roe = _valid_roe(
        authorized_signatories=[
            Signatory(name="Pat Lee", title="Manager", authority="")
        ]
    )
    errors = roe.validate()
    assert roe.is_valid() is False
    assert any("authority" in e.lower() for e in errors)


def test_no_emergency_contact_is_invalid():
    roe = _valid_roe(emergency_contacts=[])
    errors = roe.validate()
    assert roe.is_valid() is False
    assert any("emergency" in e.lower() for e in errors)


def test_no_allowed_vectors_is_invalid():
    roe = _valid_roe(allowed_vectors=[])
    errors = roe.validate()
    assert roe.is_valid() is False
    assert any("vector" in e.lower() for e in errors)


def test_no_abort_conditions_is_invalid():
    roe = _valid_roe(abort_conditions=[])
    errors = roe.validate()
    assert roe.is_valid() is False
    assert any("abort" in e.lower() for e in errors)


def test_no_window_is_invalid():
    roe = _valid_roe(windows=[])
    errors = roe.validate()
    assert roe.is_valid() is False
    assert any("window" in e.lower() for e in errors)


def test_validate_reports_every_problem_at_once():
    """An operator fixing an RoE wants the full list, not one error at a time."""
    roe = _valid_roe(client_name="", allowed_vectors=[], abort_conditions=[])
    errors = roe.validate()
    assert len(errors) >= 3


def test_raise_if_invalid_raises_on_bad_roe():
    roe = _valid_roe(client_name="")
    with pytest.raises(ValueError):
        roe.raise_if_invalid()


def test_raise_if_invalid_is_silent_on_good_roe():
    roe = _valid_roe()
    roe.raise_if_invalid()  # must not raise


def test_roundtrip_through_dict():
    roe = _valid_roe()
    assert RulesOfEngagement.from_dict(roe.to_dict()) == roe


def test_roundtrip_through_file(tmp_path):
    roe = _valid_roe()
    path = tmp_path / "roe.json"
    roe.save(path)
    assert RulesOfEngagement.load(path) == roe
