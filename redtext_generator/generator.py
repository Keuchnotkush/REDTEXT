"""
Core generator engine.
Assembles fictional social engineering scenarios from templates and user parameters.

Contributor notes:
- Keep templates as data in redtext_gen/templates.py.
- Keep generation logic in this file.
- Any new {placeholders} must be supported in the replacements map.
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

class RedtextGenerator:
    """Generates fictional social engineering pretexts based on target parameters."""

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
    # This method:
    # 1. Selects a phishing template (uses template_id if provided).
    # 2. Chooses random industry values (software, department).
    # 3. Generates a target name and derived values.
    # 4. Picks an urgency trigger and persona title.
    # 5. Replaces all {placeholders} in the subject and body.
    # 6. Returns a dict with: type, template name, subject, body,
    #    target info, attacker persona, urgency level,
    #    and psychological principles used.

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
            "{transaction_id}": f"TXN-{_random_id(10)}",
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
    
    # ───────────────────────────────────────────────────────
    #  METHOD 2: generate_vishing_script
    # ───────────────────────────────────────────────────────
    #
    # This method:
    # 1. Selects a vishing script (uses script_id if provided).
    # 2. Generates random names for caller, target, and manager.
    # 3. Chooses random industry values (department, software).
    # 4. Replaces all {placeholders} in opening, escalation, objective,
    #    and red_flags_to_avoid.
    # 5. Returns a dict with: type, template name, caller, target info,
    #    script sections, urgency level, recommended principles,
    #    and preparation notes.

    def generate_vishing_script(self, script_id: Optional[str] = None) -> dict:
        """Generate a vishing call script."""
        # TODO: Your code here
        if script_id:
            script = next((s for s in VISHING_SCRIPTS if s["id"] == script_id), None)
            if not script:
                script = random.choice(VISHING_SCRIPTS)
        else:
                script = random.choice(VISHING_SCRIPTS)
        caller = _random_name()
        target_name = _random_name()
        manager_name = _random_name()
        department = random.choice(self.industry["departments"])
        software = random.choice(self.industry["software"])
        replacements = {
            "{caller_name}": caller,
            "{company}": self.company_name,
            "{target_name}": target_name,
            "{department}": department,
            "{manager_name}": manager_name,
            "{software}": software,
            # TODO: Fill in the rest
            "{issue}": random.choice(["unusual login activity", "a failed security scan", "unpatched software vulnerabilities", "anomalous network traffic"]),
            "{ticket_number}": f"TCKT-{_random_id(8)}",
            "{time}": f"{random.randint(1, 12)}:{random.choice(['00', '15', '30', '45'])} {random.choice(['AM', 'PM'])}",
            "{time_of_day}": random.choice(["morning", "afternoon", "evening"]),
            "{vendor_name}": random.choice(["Microsoft", "Adobe", "Oracle"]),
            "{cve_year}": random.choice(["2023", "2025"]),
            "{cve_id}": _random_id(5),
            "{disclosure_date}": _random_date_near(),
            "{executive_name}": _random_name(),
            "{action}": random.choice(["wire transfer", "data transfer", "password reset"]),
            "{deadline}": random.choice(["end of day", "tomorrow", "by noon"]),
            "{department_head}": _random_name()
        }

        formatted = {}
        for key in ["opening", "escalation", "objective", "red_flags_to_avoid"]:
            text = script[key]
            for placeholder, value in replacements.items():
                text = text.replace(placeholder, value)
            formatted[key] = text
        return {
            "type": "vishing_script",
            "template": script["name"],
            "caller": caller,
            "target": {
                "name": target_name,
                "department": department,
                "company": self.company_name,
            },
            "manager": manager_name,
            "script": formatted,
            "urgency_level": self.urgency,
            "recommended_principles": ["authority", "urgency", "liking"],
            "preparation_notes": [
                f"OSINT the target's LinkedIn for role confirmation",
                f"Verify {software} is actually used (check job postings, Shodan)",
                f"Spoof caller ID to match {self.company_name}'s known numbers",
                f"Prepare a fake ticket number in case they want to verify"
            ],        
            
            }
    # ───────────────────────────────────────────────────────
    #  METHOD 3: generate_physical_pretext
    # ───────────────────────────────────────────────────────
    #
    # This method:
    # 1. Selects a physical pretext (uses pretext_id if provided).
    # 2. Generates operator and target names plus location details.
    # 3. Replaces {placeholders} in the script.
    # 4. Returns a dict with: type, template name, operator info
    #    (name, cover identity, appearance, props), script,
    #    target areas, objectives, urgency level, and preparation notes.

    def generate_physical_pretext(self, pretext_id: Optional[str] = None) -> dict:
        """Generate a physical access pretext scenario."""
        if pretext_id:
            pretext = next((p for p in PHYSICAL_PRETEXTS if p["id"] == pretext_id), None)
            if not pretext:
                pretext = random.choice(PHYSICAL_PRETEXTS)
        else:
            pretext = random.choice(PHYSICAL_PRETEXTS)
        operator_name = _random_name()
        target_name = _random_name()
        department = random.choice(self.industry["departments"])
        floor = random.randint(1, 20)
        replacements = {
            "{floor}": str(random.randint(1, 12)),
            "{name}": operator_name,
            "{target_name}": target_name,
            "{department}": department,
            "{wo_number}": f"WO-{_random_id(6)}",
            "{isp_name}": random.choice(["Comcast", "AT&T", "Verizon"]),
            "{fire_safety_company}": random.choice(["SafeFire Inc.", "FireGuard Solutions", "FlameSafe Services"]),
            "{area}": random.choice(["the server room HVAC", "3rd floor ventilation", "the east wing electrical panel"])
        }

        script_text = pretext["script"]
        for key, val in replacements.items():
                script_text = script_text.replace(key, val)

        return {
            "type": "physical_pretext",
            "template": pretext["name"],
            "operator": {
                "name": operator_name,
                "cover_identity": pretext["name"],       
                "appearance": pretext["appearance"],       
                "props": pretext["props"],                 
            },
            "script": script_text,
            "target_areas": pretext["target_areas"],       
            "objectives": pretext["objectives"],
            "urgency_level": self.urgency,
            "preparation_notes": [
                "Acquire appropriate uniform and props for the cover identity",
                f"Print work orders with {self.company_name} address and building management logo",
                "Research building layout via Google Maps and public records",
                "Identify security checkpoints, badge readers, and camera positions",
                "Know the name of building management or facilities contact in case questioned"
            ],
        }

    # ───────────────────────────────────────────────────────
    #  METHOD 4: generate_full_scenario
    # ───────────────────────────────────────────────────────
    #
    # This method:
    # 1. Generates a random operation name (e.g., "Operation SHADOW GATE").
    # 2. Selects a seasonal hook based on the current quarter.
    # 3. Builds phishing, vishing, and physical scenarios.
    # 4. Adds recon tasks and OPSEC notes.
    # 5. Returns everything as one dict.

    def generate_full_scenario(self) -> dict:
        """Generate a complete multi-vector attack scenario."""
        # TODO: Your code here
        operation_name = f"Operation {random.choice(['SHADOW', 'IRON', 'SILVER', 'GOLDEN', 'CRIMSON'])} {random.choice(['GATE', 'SPEAR', 'WAVE', 'FANG', 'BLADE'])}"
        quarter = _get_quarter()
        seasonal_hook = random.choice(SEASONAL_HOOKS[quarter])
        phishing_scenario = self.generate_phishing_email()
        social_scenario = self.generate_vishing_script()
        physical_scenario = self.generate_physical_pretext()

        return {
            "operation_name": operation_name,
            "quarter": quarter,
            "target_company": self.company_name,
            "industry": self.industry["name"],
            "seasonal_hook": seasonal_hook,
            "phishing": phishing_scenario,
            "social": social_scenario,
            "physical": physical_scenario,
            "recon_tasks": [
                f"Research {self.company_name} employees and organizational structure",
                f"Identify key personnel in {self.industry['departments']} departments",
                f"Map internal network topology and critical systems",
                f"Identify public-facing services and potential attack vectors"
            ],
            "opsec_notes": [
                "Use VPN and burner infrastructure for all communications",
                "Register lookalike domains at least 30 days prior",
                "Warm up email domain with legitimate traffic before phishing",
                "Use separate devices for each engagement phase",
                "Document everything for the final report"
            ],
        }
