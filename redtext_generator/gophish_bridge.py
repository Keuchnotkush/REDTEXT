"""
Bridge between REDTEXT generator output and GoPhish API payloads.

Pure data transformation — no network calls. Converts phishing_email dicts
from RedtextGenerator into GoPhish template/campaign payloads, and parses
target CSVs into group payloads.
"""

import csv
import re

# Basic email format validation
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Characters that can trigger formula injection in spreadsheet apps
_INJECTION_PREFIXES = ("=", "+", "-", "@", "\t", "\r")


def _validate_target(target, row_num):
    """Validate a single target dict for unsafe or malformed data.

    Args:
        target: Dict with email, first_name, last_name, position.
        row_num: 1-based row number for error messages.

    Raises:
        ValueError: If email is invalid or fields contain injection payloads.
    """
    email = target["email"]
    if not _EMAIL_RE.match(email):
        raise ValueError(f"Row {row_num}: invalid email format: {email!r}")

    for field, value in target.items():
        if value and value[0] in _INJECTION_PREFIXES:
            raise ValueError(
                f"Row {row_num}: suspicious value in '{field}': {value!r} "
                "(starts with formula injection character)"
            )


def text_to_html(text):
    """Convert plain text email body to basic HTML with GoPhish tracking pixel.

    Splits on blank lines for paragraphs, converts single newlines to <br>,
    and appends the GoPhish {{.Tracker}} pixel.

    Args:
        text: Plain text email body.

    Returns:
        HTML string wrapped in <html><body> tags.
    """
    paragraphs = text.split("\n\n")
    html_parts = []
    for para in paragraphs:
        para = para.strip()
        if para:
            para_html = para.replace("\n", "<br>")
            html_parts.append(f"<p>{para_html}</p>")

    body = "\n".join(html_parts)
    return f"<html><body>\n{body}\n{{{{.Tracker}}}}\n</body></html>"


def phishing_to_template(phishing_data, template_name=None):
    """Convert a REDTEXT phishing_email dict to a GoPhish template payload.

    Args:
        phishing_data: Output from RedtextGenerator.generate_phishing_email().
        template_name: Override name for the GoPhish template. Defaults to
                       "REDTEXT - {template_name_from_data}".

    Returns:
        Dict with keys: name, subject, text, html — ready for
        GoPhishClient.create_template().
    """
    name = template_name or f"REDTEXT - {phishing_data['template']}"
    return {
        "name": name,
        "subject": phishing_data["subject"],
        "text": phishing_data["body"],
        "html": text_to_html(phishing_data["body"]),
    }


def build_campaign_config(scenario_name, template_name, group_name, smtp_name,
                          landing_page, url, launch_date=None):
    """Assemble keyword arguments for GoPhishClient.create_campaign().

    Returns:
        Dict that can be unpacked as **kwargs into create_campaign().
    """
    return {
        "name": scenario_name,
        "template_name": template_name,
        "page_name": landing_page,
        "smtp_name": smtp_name,
        "url": url,
        "group_names": [group_name],
        "launch_date": launch_date,
    }


def parse_targets_csv(filepath):
    """Read a CSV file and return a list of target dicts for create_group().

    Expected CSV columns: email, first_name, last_name, position

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of dicts with keys: email, first_name, last_name, position.

    Raises:
        ValueError: If required columns are missing or the file has no data rows.
    """
    required = {"email", "first_name", "last_name", "position"}

    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError(f"CSV file is empty: {filepath}")

        actual = set(reader.fieldnames)
        missing = required - actual
        if missing:
            raise ValueError(
                f"CSV missing required columns: {', '.join(sorted(missing))}. "
                f"Expected: {', '.join(sorted(required))}"
            )

        targets = []
        for i, row in enumerate(reader, start=2):  # row 1 is header
            target = {
                "email": row["email"].strip(),
                "first_name": row["first_name"].strip(),
                "last_name": row["last_name"].strip(),
                "position": row["position"].strip(),
            }
            _validate_target(target, row_num=i)
            targets.append(target)

        if not targets:
            raise ValueError(f"CSV file has no data rows: {filepath}")

        return targets
