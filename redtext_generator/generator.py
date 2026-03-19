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
    SMISHING_TEMPLATES,
    QUISHING_TEMPLATES,
    VISHING_SCRIPTS,
    PHYSICAL_PRETEXTS,
    PSYCH_PRINCIPLES,
    FAKE_DOCUMENTS,
    RECON_TEMPLATES,
    C2_TEMPLATES,
    OPSEC_CHECKLISTS,
    get_localized_templates,
)
from .locales import load_locale
from .mitre import get_mitre_data
from . import qrencode


# ═══════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def _random_id(length: int = 6) -> str:
    """Generate a random numeric ID like '482901'."""
    return "".join(random.choices(string.digits, k=length))


def _random_name(strings=None) -> str:
    """Generate a random full name, optionally locale-aware."""
    if strings and "generator" in strings:
        gen = strings["generator"]
        first = random.choice(gen.get("first_names", ["James", "Sarah", "Michael"]))
        last = random.choice(gen.get("last_names", ["Thompson", "Mitchell", "Anderson"]))
    else:
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


def _random_date_near(strings=None) -> str:
    """Generate a random date 1-14 days from now, optionally locale-aware."""
    offset = random.randint(1, 14)
    date = datetime.datetime.now() + datetime.timedelta(days=offset)
    if strings and "generator" in strings:
        months = strings["generator"].get("months")
        if months:
            return f"{date.day} {months[date.month - 1]} {date.year}"
    return date.strftime("%B %d, %Y")


def _build_signature(persona_title: str, company: str = "ACME Corp", strings=None) -> str:
    """Build a realistic email signature, optionally locale-aware."""
    name = _random_name(strings)
    phone = f"+1 ({random.randint(200,999)}) {random.randint(100,999)}-{random.randint(1000,9999)}"
    closing = "Best regards,"
    if strings and "generator" in strings:
        closing = strings["generator"].get("signature_closing", closing)
    return f"""{closing}
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
        language: str = "en",
    ):
        # Load localized templates
        loc = get_localized_templates(language)
        self._industries = loc["INDUSTRIES"]
        self._personas = loc["PERSONAS"]
        self._urgency_triggers = loc["URGENCY_TRIGGERS"]
        self._seasonal_hooks = loc["SEASONAL_HOOKS"]
        self._phishing_templates = loc["PHISHING_TEMPLATES"]
        self._smishing_templates = loc["SMISHING_TEMPLATES"]
        self._quishing_templates = loc["QUISHING_TEMPLATES"]
        self._vishing_scripts = loc["VISHING_SCRIPTS"]
        self._physical_pretexts = loc["PHYSICAL_PRETEXTS"]
        self._psych_principles = loc["PSYCH_PRINCIPLES"]
        self._fake_documents = loc["FAKE_DOCUMENTS"]
        self._recon_templates = loc["RECON_TEMPLATES"]
        self._c2_templates = loc["C2_TEMPLATES"]
        self._opsec_checklists = loc["OPSEC_CHECKLISTS"]
        self._strings = load_locale(language)
        self.language = language

        if industry not in self._industries:
            raise ValueError(f"Unknown industry: {industry}. Choose from: {list(self._industries.keys())}")
        if persona not in self._personas:
            raise ValueError(f"Unknown persona: {persona}. Choose from: {list(self._personas.keys())}")
        if urgency not in self._urgency_triggers:
            raise ValueError(f"Unknown urgency: {urgency}. Choose from: {list(self._urgency_triggers.keys())}")

        # Store selections
        self.industry = self._industries[industry]
        self.industry_key = industry
        self.persona = self._personas[persona]
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
        strings = self._strings
        if template_id:
            template = next((t for t in self._phishing_templates if t["id"] == template_id), None)
            if not template:
                template = random.choice(self._phishing_templates)
        else:
            template = random.choice(self._phishing_templates)

        software = random.choice(self.industry["software"])
        department = random.choice(self.industry["departments"])
        target_name = _random_name(strings)
        first_name = target_name.split()[0]
        urgency_trigger = random.choice(self._urgency_triggers[self.urgency])
        persona_title = random.choice(self.persona["titles"])
        gen = strings.get("generator", {})

        replacements = {
            "{first_name}": first_name,
            "{software}": software,
            "{department}": department,
            "{company}": self.company_name,
            "{urgency_opening}": urgency_trigger,
            "{deadline}": random.choice(gen.get("deadlines", ["24 hours", "end of business today", "4:00 PM today", "Friday"])),
            "{signature}": _build_signature(persona_title, self.company_name, strings),
            "{phishing_link}": f"https://{self.company_name.lower().replace(' ', '')}-verify.com/auth/{_random_id(12)}",
            "{document_name}": random.choice(self._fake_documents),
            "{document_type}": random.choice(gen.get("document_types", ["document", "spreadsheet", "report", "invoice"])),
            "{attachment_note}": f"{gen.get('attachment_prefix', 'Attachment')}: {random.choice(self._fake_documents)}",
            "{executive_name}": _random_name(strings),
            "{executive_signature}": _build_signature(random.choice(self._personas["executive"]["titles"]), self.company_name, strings),
            "{amount}": f"{random.randint(1000, 10000):,}",
            "{bank_name}": random.choice(["Chase Bank", "Wells Fargo", "Bank of America"]),
            "{account_placeholder}": f"XXXX-XXXX-{random.randint(1000, 9999)}",
            "{reference}": f"PO-{_random_id(6)}",
            "{callback_number}": f"1-800-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "{transaction_id}": f"TXN-{_random_id(10)}",
            "{date}": _random_date_near(strings),
            "{invoice_number}": _random_id(8),
            "{generic_signature}": gen.get("billing_department", "Billing Department, {company}").replace("{company}", self.company_name),
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
            "opsec_checklist": self._opsec_checklists.get("phishing", []),
            "mitre_attack": get_mitre_data("phishing_email", template["id"]),
            "language": self.language,
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
        strings = self._strings
        gen = strings.get("generator", {})
        if script_id:
            script = next((s for s in self._vishing_scripts if s["id"] == script_id), None)
            if not script:
                script = random.choice(self._vishing_scripts)
        else:
            script = random.choice(self._vishing_scripts)
        caller = _random_name(strings)
        target_name = _random_name(strings)
        manager_name = _random_name(strings)
        department = random.choice(self.industry["departments"])
        software = random.choice(self.industry["software"])
        replacements = {
            "{caller_name}": caller,
            "{company}": self.company_name,
            "{target_name}": target_name,
            "{department}": department,
            "{manager_name}": manager_name,
            "{software}": software,
            "{issue}": random.choice(gen.get("vishing_issues", ["unusual login activity", "a failed security scan", "unpatched software vulnerabilities", "anomalous network traffic"])),
            "{ticket_number}": f"TCKT-{_random_id(8)}",
            "{time}": f"{random.randint(1, 12)}:{random.choice(['00', '15', '30', '45'])} {random.choice(['AM', 'PM'])}",
            "{time_of_day}": random.choice(gen.get("time_of_day", ["morning", "afternoon", "evening"])),
            "{vendor_name}": random.choice(["Microsoft", "Adobe", "Oracle"]),
            "{cve_year}": random.choice(["2023", "2025"]),
            "{cve_id}": _random_id(5),
            "{disclosure_date}": _random_date_near(strings),
            "{executive_name}": _random_name(strings),
            "{action}": random.choice(gen.get("vishing_actions", ["wire transfer", "data transfer", "password reset"])),
            "{deadline}": random.choice(gen.get("deadlines_vishing", ["end of day", "tomorrow", "by noon"])),
            "{department_head}": _random_name(strings),
        }

        formatted = {}
        for key in ["opening", "escalation", "objective", "red_flags_to_avoid"]:
            text = script[key]
            for placeholder, value in replacements.items():
                text = text.replace(placeholder, value)
            formatted[key] = text

        prep_notes = gen.get("preparation_notes_vishing", [
            "OSINT the target's LinkedIn for role confirmation",
            "Verify {software} is actually used (check job postings, Shodan)",
            "Spoof caller ID to match {company}'s known numbers",
            "Prepare a fake ticket number in case they want to verify",
        ])
        prep_notes = [n.replace("{software}", software).replace("{company}", self.company_name) for n in prep_notes]

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
            "preparation_notes": prep_notes,
            "opsec_checklist": self._opsec_checklists.get("vishing", []),
            "mitre_attack": get_mitre_data("vishing_script", script["id"]),
            "language": self.language,
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
        strings = self._strings
        gen = strings.get("generator", {})
        if pretext_id:
            pretext = next((p for p in self._physical_pretexts if p["id"] == pretext_id), None)
            if not pretext:
                pretext = random.choice(self._physical_pretexts)
        else:
            pretext = random.choice(self._physical_pretexts)
        operator_name = _random_name(strings)
        target_name = _random_name(strings)
        department = random.choice(self.industry["departments"])
        replacements = {
            "{floor}": str(random.randint(1, 12)),
            "{name}": operator_name,
            "{target_name}": target_name,
            "{department}": department,
            "{wo_number}": f"WO-{_random_id(6)}",
            "{isp_name}": random.choice(["Comcast", "AT&T", "Verizon"]),
            "{fire_safety_company}": random.choice(["SafeFire Inc.", "FireGuard Solutions", "FlameSafe Services"]),
            "{area}": random.choice(["the server room HVAC", "3rd floor ventilation", "the east wing electrical panel"]),
            "{company}": self.company_name,
            "{printer_vendor}": random.choice(["Canon", "Ricoh", "Xerox", "HP"]),
            "{printer_model}": random.choice(["ImageRUNNER C3530", "MP C4504", "VersaLink C7030", "LaserJet Pro M428"]),
        }

        script_text = pretext["script"]
        for key, val in replacements.items():
            script_text = script_text.replace(key, val)

        prep_notes = gen.get("preparation_notes_physical", [
            "Acquire appropriate uniform and props for the cover identity",
            "Print work orders with {company} address and building management logo",
            "Research building layout via Google Maps and public records",
            "Identify security checkpoints, badge readers, and camera positions",
            "Know the name of building management or facilities contact in case questioned",
        ])
        prep_notes = [n.replace("{company}", self.company_name) for n in prep_notes]

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
            "preparation_notes": prep_notes,
            "opsec_checklist": self._opsec_checklists.get("physical", []),
            "mitre_attack": get_mitre_data("physical_pretext", pretext["id"]),
            "language": self.language,
        }

    # ───────────────────────────────────────────────────────
    #  METHOD 4: generate_smishing_message
    # ───────────────────────────────────────────────────────
    #
    # This method:
    # 1. Selects a smishing template (uses template_id if provided).
    # 2. Picks a random message variant from the template.
    # 3. Generates target info, short link, and dynamic values.
    # 4. Replaces all {placeholders} in the message.
    # 5. Returns a dict with: type, template name, message,
    #    target info, attacker persona, urgency level,
    #    short code, and malicious link.

    def generate_smishing_message(self, template_id: Optional[str] = None) -> dict:
        """Generate a smishing (SMS phishing) scenario."""
        strings = self._strings
        if template_id:
            template = next((t for t in self._smishing_templates if t["id"] == template_id), None)
            if not template:
                template = random.choice(self._smishing_templates)
        else:
            template = random.choice(self._smishing_templates)

        software = random.choice(self.industry["software"])
        department = random.choice(self.industry["departments"])
        target_name = _random_name(strings)
        first_name = target_name.split()[0]
        persona_title = random.choice(self.persona["titles"])

        short_code = str(random.randint(10000, 99999))
        domain = random.choice(["verify-now.co", "secure-alert.info", "acct-update.net", "pkg-track.com", "confirm-id.org"])
        smishing_link = f"https://{domain}/{_random_id(8)}"

        replacements = {
            "{first_name}": first_name,
            "{company}": self.company_name,
            "{software}": software,
            "{department}": department,
            "{smishing_link}": smishing_link,
            "{carrier}": random.choice(["USPS", "FedEx", "UPS", "DHL"]),
            "{tracking_id}": f"{_random_id(4)}-{_random_id(4)}-{_random_id(4)}",
            "{small_fee}": f"{random.randint(1, 9)}.{random.choice(['49', '95', '99'])}",
            "{mfa_code}": _random_id(6),
            "{bank_name}": random.choice(["Chase", "Wells Fargo", "Bank of America", "Citi"]),
            "{amount}": f"{random.randint(50, 5000):,}",
        }

        message = random.choice(template["messages"])
        for key, val in replacements.items():
            message = message.replace(key, val)

        return {
            "type": "smishing",
            "template": template["name"],
            "message": message,
            "target": {
                "name": target_name,
                "department": department,
                "company": self.company_name,
            },
            "attacker_persona": persona_title,
            "urgency_level": self.urgency,
            "short_code": short_code,
            "malicious_link": smishing_link,
            "opsec_checklist": self._opsec_checklists.get("smishing", []),
            "mitre_attack": get_mitre_data("smishing", template["id"]),
            "language": self.language,
        }

    # ───────────────────────────────────────────────────────
    #  METHOD 5: generate_quishing_scenario
    # ───────────────────────────────────────────────────────
    #
    # This method:
    # 1. Selects a quishing template (uses template_id if provided).
    # 2. Generates a malicious URL and QR code (ASCII art).
    # 3. Replaces {placeholders} in the pretext text.
    # 4. Returns a dict with: type, template name, pretext text,
    #    delivery method, placement, objectives, target info,
    #    attacker persona, urgency level, malicious link, and QR ASCII.

    def generate_quishing_scenario(self, template_id: Optional[str] = None, url: Optional[str] = None) -> dict:
        """Generate a quishing (QR code phishing) scenario."""
        strings = self._strings
        gen = strings.get("generator", {})
        if template_id:
            template = next((t for t in self._quishing_templates if t["id"] == template_id), None)
            if not template:
                template = random.choice(self._quishing_templates)
        else:
            template = random.choice(self._quishing_templates)

        software = random.choice(self.industry["software"])
        department = random.choice(self.industry["departments"])
        target_name = _random_name(strings)
        persona_title = random.choice(self.persona["titles"])

        if url:
            malicious_link = url
        else:
            domain = random.choice(["secure-portal.co", "wifi-connect.net", "pay-verify.com", "doc-access.org", "id-check.info"])
            malicious_link = f"https://{domain}/{_random_id(8)}"

        replacements = {
            "{company}": self.company_name,
            "{software}": software,
            "{department}": department,
            "{support_email}": f"it-support@{self.company_name.lower().replace(' ', '')}.com",
            "{parking_zone}": random.choice(["A", "B", "C", "D"]),
            "{parking_rate}": str(random.randint(2, 8)),
            "{document_name}": random.choice(self._fake_documents),
            "{sender_name}": _random_name(strings),
            "{sender_title}": random.choice(self.persona["titles"]),
            "{deadline}": random.choice(gen.get("deadlines_quishing", ["24 hours", "end of business today", "Friday at 5:00 PM"]) + [_random_date_near(strings)]),
        }

        pretext = template["pretext_text"]
        for key, val in replacements.items():
            pretext = pretext.replace(key, val)

        # Generate QR code
        matrix = qrencode.encode(malicious_link)
        qr_ascii = qrencode.render_ascii(matrix)

        return {
            "type": "quishing",
            "template": template["name"],
            "pretext_text": pretext,
            "delivery_method": random.choice(template["delivery_methods"]),
            "placement_suggestions": template["placement_suggestions"],
            "objectives": template["objectives"],
            "target": {
                "name": target_name,
                "department": department,
                "company": self.company_name,
            },
            "attacker_persona": persona_title,
            "urgency_level": self.urgency,
            "malicious_link": malicious_link,
            "qr_ascii": qr_ascii,
            "opsec_checklist": self._opsec_checklists.get("quishing", []),
            "mitre_attack": get_mitre_data("quishing", template["id"]),
            "language": self.language,
        }

    # ───────────────────────────────────────────────────────
    #  METHOD 6: generate_full_scenario
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
        strings = self._strings
        gen = strings.get("generator", {})
        operation_name = f"Operation {random.choice(['SHADOW', 'IRON', 'SILVER', 'GOLDEN', 'CRIMSON'])} {random.choice(['GATE', 'SPEAR', 'WAVE', 'FANG', 'BLADE'])}"
        quarter = _get_quarter()
        seasonal_hook = random.choice(self._seasonal_hooks[quarter])
        phishing_scenario = self.generate_phishing_email()
        smishing_scenario = self.generate_smishing_message()
        social_scenario = self.generate_vishing_script()
        physical_scenario = self.generate_physical_pretext()

        recon_tasks = gen.get("recon_tasks", [
            "Research {company} employees and organizational structure",
            "Identify key personnel in {departments} departments",
            "Map internal network topology and critical systems",
            "Identify public-facing services and potential attack vectors",
        ])
        depts = str(self.industry["departments"])
        recon_tasks = [t.replace("{company}", self.company_name).replace("{departments}", depts) for t in recon_tasks]

        opsec_notes = gen.get("opsec_notes", [
            "Use VPN and burner infrastructure for all communications",
            "Register lookalike domains at least 30 days prior",
            "Warm up email domain with legitimate traffic before phishing",
            "Use separate devices for each engagement phase",
            "Document everything for the final report",
        ])

        # Aggregate MITRE ATT&CK data from all sub-scenarios
        all_techniques = []
        all_should_detect = []
        all_often_fails = []
        seen_ids = set()
        for sub in [phishing_scenario, smishing_scenario, social_scenario, physical_scenario]:
            mitre = sub.get("mitre_attack", {})
            for t in mitre.get("techniques", []):
                if t[0] not in seen_ids:
                    seen_ids.add(t[0])
                    all_techniques.append(t)
            det = mitre.get("detection", {})
            all_should_detect.extend(det.get("should_detect", []))
            all_often_fails.extend(det.get("often_fails", []))

        # Deduplicate detection items preserving order
        all_should_detect = list(dict.fromkeys(all_should_detect))
        all_often_fails = list(dict.fromkeys(all_often_fails))

        return {
            "operation_name": operation_name,
            "quarter": quarter,
            "target_company": self.company_name,
            "industry": self.industry["name"],
            "seasonal_hook": seasonal_hook,
            "phishing": phishing_scenario,
            "smishing": smishing_scenario,
            "social": social_scenario,
            "physical": physical_scenario,
            "recon_tasks": recon_tasks,
            "opsec_notes": opsec_notes,
            "mitre_attack": {
                "techniques": all_techniques,
                "tactics": ["Reconnaissance", "Initial Access", "Credential Access",
                            "Privilege Escalation", "Lateral Movement", "Collection"],
                "detection_analysis": {
                    "should_detect": all_should_detect,
                    "often_fails": all_often_fails,
                },
            },
            "language": self.language,
        }

    # ───────────────────────────────────────────────────────
    #  METHOD 7: generate_recon_plan
    # ───────────────────────────────────────────────────────

    def generate_recon_plan(self, template_id: Optional[str] = None) -> dict:
        """Generate a reconnaissance plan for the target."""
        strings = self._strings
        if template_id:
            template = next((t for t in self._recon_templates if t["id"] == template_id), None)
            if not template:
                template = random.choice(self._recon_templates)
        else:
            template = random.choice(self._recon_templates)

        software = random.choice(self.industry["software"])
        department = random.choice(self.industry["departments"])

        replacements = {
            "{company}": self.company_name,
            "{software}": software,
            "{department}": department,
        }

        def _replace(text):
            for k, v in replacements.items():
                text = text.replace(k, v)
            return text

        passive = [_replace(t) for t in template["passive_tasks"]]
        active = [_replace(t) for t in template["active_tasks"]]
        deliverables = [_replace(t) for t in template["deliverables"]]

        return {
            "type": "recon",
            "template": template["name"],
            "description": _replace(template["description"]),
            "target": {
                "company": self.company_name,
                "industry": self.industry["name"],
                "departments": self.industry["departments"],
                "software": self.industry["software"],
            },
            "passive_tasks": passive,
            "active_tasks": active,
            "tools": template["tools"],
            "deliverables": deliverables,
            "opsec_checklist": self._opsec_checklists.get("recon", []),
            "mitre_attack": get_mitre_data("recon", template["id"]),
            "language": self.language,
        }

    # ───────────────────────────────────────────────────────
    #  METHOD 8: generate_c2_scenario
    # ───────────────────────────────────────────────────────

    def generate_c2_scenario(self, template_id: Optional[str] = None) -> dict:
        """Generate a C2 infrastructure plan."""
        if template_id:
            template = next((t for t in self._c2_templates if t["id"] == template_id), None)
            if not template:
                template = random.choice(self._c2_templates)
        else:
            template = random.choice(self._c2_templates)

        c2_domain = f"{random.choice(['analytics', 'cdn', 'api', 'static', 'assets'])}-{self.company_name.lower().replace(' ', '')}.{random.choice(['com', 'net', 'io', 'co'])}"
        backup_domain = f"{random.choice(['updates', 'sync', 'telemetry', 'metrics'])}.{random.choice(['cloud-services.net', 'app-delivery.io', 'web-analytics.co'])}"

        return {
            "type": "c2",
            "template": template["name"],
            "protocol": template["protocol"],
            "description": template["description"],
            "target": {
                "company": self.company_name,
                "industry": self.industry["name"],
            },
            "c2_domain": c2_domain,
            "backup_domain": backup_domain,
            "infrastructure": template["infrastructure"],
            "beacon_config": template["beacon_config"],
            "cover_story": template["cover_story"],
            "evasion_notes": template["evasion_notes"],
            "detection_signatures": template["detection_signatures"],
            "opsec_checklist": self._opsec_checklists.get("c2", []),
            "mitre_attack": get_mitre_data("c2", template["id"]),
            "language": self.language,
        }
