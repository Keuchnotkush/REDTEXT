"""
Output formatters for terminal display and file export.
"""

import json
import os
import re
import time
import sys

def loading_animation(message: str = "Generating scenario", duration: float = 1.5):
    """Display a loading animation."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r  {_c(frames[i % len(frames)], Colors.RED)} {_c(message + '...', Colors.DIM)}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r  {_c('✓', Colors.GREEN)} {_c(message + ' — done', Colors.DIM)}\n\n")
    sys.stdout.flush()

# ═══════════════════════════════════════════════════════════════
#  ANSI COLORS
# ═══════════════════════════════════════════════════════════════

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    PURPLE = "\033[35m"


def _c(text: str, color: str) -> str:
    return f"{color}{text}{Colors.RESET}"


def _header(title: str, width: int = 70) -> str:
    line = "═" * width
    return f"\n{_c(line, Colors.DIM)}\n  {_c(title, Colors.BOLD + Colors.CYAN)}\n{_c(line, Colors.DIM)}"


def _field(label: str, value: str, indent: int = 4) -> str:
    pad = " " * indent
    return f"{pad}{_c(label + ':', Colors.GREEN)} {value}"


def _list_items(items: list, indent: int = 6) -> str:
    pad = " " * indent
    return "\n".join(f"{pad}{_c('•', Colors.DIM)} {item}" for item in items)


def _strip_ansi(text: str) -> str:
    return re.sub(r'\033\[[0-9;]*m', '', text)


# ═══════════════════════════════════════════════════════════════
#  TERMINAL FORMATTERS
# ═══════════════════════════════════════════════════════════════

def format_phishing_email(data: dict) -> str:
    lines = []
    lines.append(_header("PHISHING EMAIL SCENARIO"))
    lines.append("")
    lines.append(_field("Template", data["template"]))
    lines.append(_field("Attacker Persona", data["attacker_persona"]))
    lines.append(_field("Urgency", _c(data["urgency_level"].upper(), Colors.RED if data["urgency_level"] in ("high", "critical") else Colors.YELLOW)))
    lines.append("")
    lines.append(_field("Target Name", data["target"]["name"]))
    lines.append(_field("Target Dept", data["target"]["department"]))
    lines.append(_field("Target Company", data["target"]["company"]))
    lines.append("")
    lines.append(_field("Subject", _c(data["subject"], Colors.WHITE + Colors.BOLD)))
    lines.append("")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for line in data["body"].split("\n"):
        lines.append(f"    {line}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")
    return "\n".join(lines)


def format_vishing_script(data: dict) -> str:
    lines = []
    lines.append(_header("📞 VISHING CALL SCRIPT"))
    lines.append("")
    lines.append(_field("Template", data["template"]))
    lines.append(_field("Caller", data["caller"]))
    lines.append(_field("Urgency", _c(data["urgency_level"].upper(), Colors.RED if data["urgency_level"] in ("high", "critical") else Colors.YELLOW)))
    lines.append("")
    lines.append(_field("Target Name", data["target"]["name"]))
    lines.append(_field("Target Dept", data["target"]["department"]))
    lines.append(_field("Target Company", data["target"]["company"]))
    lines.append("")

    for section in ["opening", "escalation", "objective", "red_flags_to_avoid"]:
        label = section.replace("_", " ").upper()
        lines.append(f"  {_c('▸ ' + label, Colors.BOLD + Colors.YELLOW)}")
        lines.append(f"    {_c('─' * 60, Colors.DIM)}")
        for line in data["script"][section].split("\n"):
            lines.append(f"    {line}")
        lines.append(f"    {_c('─' * 60, Colors.DIM)}")
        lines.append("")

    lines.append(f"  {_c('▸ PREPARATION', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["preparation_notes"]))
    lines.append("")
    return "\n".join(lines)


def format_smishing_message(data: dict) -> str:
    lines = []
    lines.append(_header("SMS/SMISHING SCENARIO"))
    lines.append("")
    lines.append(_field("Template", data["template"]))
    lines.append(_field("Attacker Persona", data["attacker_persona"]))
    lines.append(_field("Urgency", _c(data["urgency_level"].upper(), Colors.RED if data["urgency_level"] in ("high", "critical") else Colors.YELLOW)))
    lines.append("")
    lines.append(_field("Target Name", data["target"]["name"]))
    lines.append(_field("Target Dept", data["target"]["department"]))
    lines.append(_field("Target Company", data["target"]["company"]))
    lines.append("")
    lines.append(_field("Short Code", data["short_code"]))
    lines.append(_field("Malicious Link", _c(data["malicious_link"], Colors.RED)))
    lines.append("")
    lines.append(f"  {_c('▸ SMS MESSAGE', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append(f"    {data['message']}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")
    return "\n".join(lines)


def format_physical_pretext(data: dict) -> str:
    lines = []
    lines.append(_header("🏢 PHYSICAL ACCESS PRETEXT"))
    lines.append("")
    lines.append(_field("Template", data["template"]))
    lines.append(_field("Operator", data["operator"]["name"]))
    lines.append(_field("Cover", data["operator"]["cover_identity"]))
    lines.append(_field("Appearance", data["operator"]["appearance"]))
    lines.append("")

    lines.append(f"  {_c('▸ PROPS', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["operator"]["props"]))
    lines.append("")

    lines.append(f"  {_c('▸ SCRIPT', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for line in data["script"].split("\n"):
        lines.append(f"    {line}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ TARGET AREAS', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["target_areas"]))
    lines.append("")

    lines.append(f"  {_c('▸ OBJECTIVES', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["objectives"]))
    lines.append("")

    lines.append(f"  {_c('▸ PREPARATION', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["preparation_notes"]))
    lines.append("")
    return "\n".join(lines)


def format_full_scenario(data: dict) -> str:
    lines = []
    lines.append("")
    lines.append(_c("  ╔══════════════════════════════════════════════════════════════╗", Colors.RED))
    lines.append(_c("  ║", Colors.RED) + _c(f"  {data['operation_name']:^58}", Colors.BOLD + Colors.WHITE) + _c("║", Colors.RED))
    lines.append(_c("  ║", Colors.RED) + _c(f"  {'FULL ATTACK SCENARIO':^58}", Colors.DIM) + _c("║", Colors.RED))
    lines.append(_c("  ╚══════════════════════════════════════════════════════════════╝", Colors.RED))
    lines.append("")
    lines.append(_field("Target", data["target_company"]))
    lines.append(_field("Industry", data["industry"]))
    lines.append(_field("Season", data["seasonal_hook"]))
    lines.append("")

    lines.append(f"  {_c('▸ PHASE 1: RECONNAISSANCE', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["recon_tasks"]))
    lines.append("")

    lines.append(f"  {_c('▸ PHASE 2: PHISHING', Colors.BOLD + Colors.YELLOW)}")
    lines.append(format_phishing_email(data["phishing"]))

    lines.append(f"  {_c('▸ PHASE 3: VISHING', Colors.BOLD + Colors.YELLOW)}")
    lines.append(format_vishing_script(data["social"]))

    lines.append(f"  {_c('▸ PHASE 4: PHYSICAL ACCESS', Colors.BOLD + Colors.YELLOW)}")
    lines.append(format_physical_pretext(data["physical"]))

    lines.append(_header("🔒 OPSEC NOTES"))
    lines.append(_list_items(data["opsec_notes"]))
    lines.append("")
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════
#  FILE EXPORT
# ═══════════════════════════════════════════════════════════════

def export_json(data: dict, filepath: str) -> str:
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else ".", exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, default=str)
    return filepath


def export_markdown(data: dict, filepath: str) -> str:
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else ".", exist_ok=True)

    if data.get("type") == "phishing_email":
        content = format_phishing_email(data)
    elif data.get("type") == "smishing":
        content = format_smishing_message(data)
    elif data.get("type") == "vishing_script":
        content = format_vishing_script(data)
    elif data.get("type") == "physical_pretext":
        content = format_physical_pretext(data)
    elif "operation_name" in data:
        content = format_full_scenario(data)
    else:
        content = json.dumps(data, indent=2)

    clean = _strip_ansi(content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# RedTEXT Generator Report\n\n")
        f.write(f"```\n{clean}\n```\n")
        f.write("\n---\n*Generated by RedTEXT Generator | For authorized red team use only*\n")
    return filepath