"""
Core generator engine.
Assembles social engineering scenarios from templates and user parameters.
"""

import random
import string
import datetime
from typing import Optional

from .templates import (
    INDUSTRIES,
    PERSONAS,
    URGENCY_TRIGGERS,
    SEASONAL_HOOKS,
    PHISHING_TEMPLATES,
    VISHING_SCRIPTS,
    PHYSICAL_PRETEXTS,
    PSYCH_PRINCIPLES,
    FAKE_DOCUMENTS,
)


# ═══════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def _random_id(length: int = 6) -> str:
    """Generate a random numeric ID like '482901'."""
    return "".join(random.choices(string.digits, k=length))


def _random_name() -> str:
    """Generate a random full name."""
    first = random.choice([
        "James", "Sarah", "Michael", "Emily", "David", "Jennifer",
        "Robert", "Lisa", "Daniel", "Amanda", "Chris", "Rachel",
        "Mark", "Karen", "Tom", "Nicole", "Brian", "Michelle",
    ])
    last = random.choice([
        "Thompson", "Mitchell", "Anderson", "Roberts", "Campbell",
        "Martinez", "Williams", "Johnson", "Brown", "Davis",
        "Wilson", "Taylor", "Clark", "Lewis", "Walker",
    ])
    return f"{first} {last}"


def _get_quarter() -> str:
    """Return current quarter as 'q1', 'q2', 'q3', or 'q4'."""
    month = datetime.datetime.now().month
    if month <= 3:
        return "q1"
    elif month <= 6:
        return "q2"
    elif month <= 9:
        return "q3"
    return "q4"


def _random_date_near() -> str:
    """Generate a random date 1-14 days from now."""
    offset = random.randint(1, 14)
    date = datetime.datetime.now() + datetime.timedelta(days=offset)
    return date.strftime("%B %d, %Y")


def _build_signature(persona_title: str, company: str = "ACME Corp") -> str:
    """Build a realistic email signature."""
    name = _random_name()
    phone = f"+1 ({random.randint(200,999)}) {random.randint(100,999)}-{random.randint(1000,9999)}"
    return f"""Best regards,
{name}
{persona_title}
{company}
{phone}"""


# ═══════════════════════════════════════════════════════════════
#  GENERATOR CLASS
# ═══════════════════════════════════════════════════════════════

class PretextGenerator:
    """Generates social engineering pretexts based on target parameters."""

    def __init__(
        self,
        industry: str = "tech",
        urgency: str = "medium",
        persona: str = "it_support",
        company_name: str = "Target Corp",
    ):
        if industry not in INDUSTRIES:
            raise ValueError(f"Unknown industry: {industry}. Choose from: {list(INDUSTRIES.keys())}")
        if persona not in PERSONAS:
            raise ValueError(f"Unknown persona: {persona}. Choose from: {list(PERSONAS.keys())}")
        if urgency not in URGENCY_TRIGGERS:
            raise ValueError(f"Unknown urgency: {urgency}. Choose from: {list(URGENCY_TRIGGERS.keys())}")

        # Store selections
        self.industry = INDUSTRIES[industry]
        self.industry_key = industry
        self.persona = PERSONAS[persona]
        self.persona_key = persona
        self.urgency = urgency
        self.company_name = company_name

    # ───────────────────────────────────────────────────────
    #  METHOD 1: generate_phishing_email
    # ───────────────────────────────────────────────────────
    #
    # This method :
    # 1. Picks a random phishing template (or use template_id if provided)
    # 2. Picks random values from self.industry (software, department)
    # 3. Generates a random target name
    # 4. Picks a random urgency trigger from URGENCY_TRIGGERS[self.urgency]
    # 5. Picks a random persona title from self.persona["titles"]
    # 6. Fills all {placeholders} in the subject and body
    # 7. Returns a dict with: type, template name, subject, body,
    #    targets info, attacker persona, urgency level,
    #    psychological principles used, and indicators of compromise

    def generate_phishing_email(self, template_id: Optional[str] = None) -> dict:
        """Generate a phishing email scenario."""
        if template_id:
            template = next((t for t in PHISHING_TEMPLATES if t["id"] == template_id), None)
            if not template:
                template = random.choice(PHISHING_TEMPLATES)
        else:
            template = random.choice(PHISHING_TEMPLATES)

        software = random.choice(self.industry["software"])
        department = random.choice(self.industry["departments"])
        target_name = _random_name()
        first_name = target_name.split()[0]
        urgency_trigger = random.choice(URGENCY_TRIGGERS[self.urgency])
        persona_title = random.choice(self.persona["titles"])

        replacements = {
            "{first_name}": first_name,
            "{software}": software,
            "{department}": department,
            "{company}": self.company_name,
            "{urgency_opening}": urgency_trigger,
            "{deadline}": random.choice(["24 hours", "end of business today", "4:00 PM today", "Friday"]),
            "{signature}": _build_signature(persona_title, self.company_name),
            "{phishing_link}": f"https://{self.company_name.lower().replace(' ', '')}-verify.com/auth/{_random_id(12)}",
            "{document_name}": random.choice(FAKE_DOCUMENTS),
            "{document_type}": random.choice(["document", "spreadsheet", "report", "invoice"]),
            "{attachment_note}": f"Attachment: {random.choice(FAKE_DOCUMENTS)}",
            "{executive_name}": _random_name(),
            "{executive_signature}": _build_signature(random.choice(PERSONAS["executive"]["titles"]), self.company_name),"{amount}": f"{random.randint(1000, 10000):,}",
            "{bank_name}": random.choice(["Chase Bank", "Wells Fargo", "Bank of America"]),
            "{account_placeholder}": f"XXXX-XXXX-{random.randint(1000, 9999)}",
            "{reference}": f"PO-{_random_id(6)}",
            "{callback_number}": f"1-800-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "{date}": _random_date_near(),
            "{invoice_number}": _random_id(8),
            "{generic_signature}": f"Billing Department, {self.company_name}",
        }

        subject = random.choice(template["subject_lines"])
        body = template["body"]
        for key, val in replacements.items():
            subject = subject.replace(key, val)
            body = body.replace(key, val)

        return {
            "type": "phishing_email",
            "template": template["name"],
            "subject": subject,
            "body": body,
            "target": {
                "name": target_name,
                "department": department,
                "company": self.company_name,
            },
            "attacker_persona": persona_title,
            "urgency_level": self.urgency,
        }