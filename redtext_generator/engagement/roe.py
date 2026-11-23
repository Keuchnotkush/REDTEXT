"""Rules of Engagement (RoE) capture and validation.

The RoE is the authorization context for an engagement. Generation is gated
on a *valid* RoE (see issue #36), so validity here means the engagement is
genuinely authorized and bounded, not merely that the fields are non-empty:

  * a named signatory **with stated authority** to authorize the work,
  * an explicit in-scope boundary and out-of-scope / no-go list,
  * an abort path (emergency contacts + abort conditions),
  * data jurisdiction and a per-target deconfliction process.

Stdlib only. Dataclasses keep the shape explicit and serializable.
"""

import json
from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Signatory:
    """A person authorizing the engagement.

    ``authority`` is load-bearing: a name and title alone do not establish
    that this person *may* authorize the work. It records what grants them
    that authority (e.g. a board delegation, a signed contract clause).
    """

    name: str
    title: str
    authority: str


@dataclass
class EmergencyContact:
    """A contact reachable to halt or deconflict the engagement."""

    name: str
    role: str
    phone: str


@dataclass
class RulesOfEngagement:
    """The authorization and scope context for a single engagement."""

    client_name: str
    engagement_name: str
    scope_description: str
    allowed_vectors: List[str]
    windows: List[str]
    authorized_signatories: List[Signatory]
    out_of_scope: List[str]
    emergency_contacts: List[EmergencyContact]
    abort_conditions: List[str]
    data_jurisdiction: str
    deconfliction: str = ""

    def validate(self) -> List[str]:
        """Return a list of problems with this RoE (empty list means valid).

        Reports *every* problem found, so an operator fixing an RoE sees the
        full list at once rather than one error per attempt.
        """
        errors: List[str] = []

        if not self.client_name.strip():
            errors.append("client_name is required.")
        if not self.engagement_name.strip():
            errors.append("engagement_name is required.")
        if not self.scope_description.strip():
            errors.append("scope_description is required.")

        if not self.allowed_vectors:
            errors.append("At least one allowed vector is required.")

        if not self.windows:
            errors.append("At least one authorized time window is required.")

        if not self.authorized_signatories:
            errors.append("At least one authorized signatory is required.")
        else:
            for i, s in enumerate(self.authorized_signatories):
                if not s.name.strip():
                    errors.append(f"Signatory {i + 1}: name is required.")
                if not s.authority.strip():
                    errors.append(
                        f"Signatory {i + 1} ({s.name or 'unnamed'}): "
                        "stated authority to authorize is required."
                    )

        if not self.out_of_scope:
            errors.append(
                "An explicit out-of-scope / no-go list is required "
                "(use an explicit 'none' entry if truly unbounded)."
            )

        if not self.emergency_contacts:
            errors.append("At least one emergency-stop contact is required.")
        else:
            for i, c in enumerate(self.emergency_contacts):
                if not c.name.strip() or not c.phone.strip():
                    errors.append(
                        f"Emergency contact {i + 1}: name and phone are required."
                    )

        if not self.abort_conditions:
            errors.append("At least one abort condition is required.")

        if not self.data_jurisdiction.strip():
            errors.append("data_jurisdiction is required.")

        return errors

    def to_dict(self):
        return asdict(self)


    def is_valid(self) -> bool:
        """True when the RoE is a complete, authorized engagement context."""
        return not self.validate()

    def raise_if_invalid(self) -> None:
        """Raise ``ValueError`` listing every problem if the RoE is invalid."""
        errors = self.validate()
        if errors:
            raise ValueError(
                "Invalid Rules of Engagement:\n  - " + "\n  - ".join(errors)
            )

    @classmethod
    def from_dict(cls, data):
        data = dict(data)
        data["authorized_signatories"] = [Signatory(**s) for s in data["authorized_signatories"]]
        data["emergency_contacts"] = [EmergencyContact(**s) for s in data["emergency_contacts"]]
        return cls(**data)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(),f)

    @classmethod
    def load(cls,path):
        with open(path, encoding="utf-8") as f:
            return cls.from_dict(json.load(f))
