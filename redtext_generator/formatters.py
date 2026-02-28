"""
Output formatters for terminal display and file export.
"""

import html as html_mod
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
#  HTML EXPORT HELPERS
# ═══════════════════════════════════════════════════════════════

_HTML_CSS = """\
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #1a1a1a; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 40px 20px; }
.report { max-width: 800px; margin: 0 auto; }
.report-header { text-align: center; border-bottom: 2px solid #c0392b; padding-bottom: 20px; margin-bottom: 30px; }
.report-header h1 { color: #c0392b; font-size: 28px; letter-spacing: 2px; }
.report-header .subtitle { color: #888; font-size: 14px; margin-top: 5px; }
.section { background: #222; border: 1px solid #333; border-radius: 6px; padding: 20px; margin-bottom: 20px; }
.section-title { color: #e74c3c; font-size: 18px; font-weight: bold; margin-bottom: 15px; border-bottom: 1px solid #333; padding-bottom: 8px; }
.field { margin-bottom: 8px; }
.field .label { color: #27ae60; font-weight: bold; display: inline-block; min-width: 160px; }
.field .value { color: #e0e0e0; }
.urgency-high, .urgency-critical { color: #e74c3c; font-weight: bold; text-transform: uppercase; }
.urgency-medium { color: #f39c12; font-weight: bold; text-transform: uppercase; }
.urgency-low { color: #27ae60; text-transform: uppercase; }
ul.items { list-style: none; padding-left: 10px; }
ul.items li { margin-bottom: 4px; }
ul.items li::before { content: '\\2022'; color: #666; margin-right: 8px; }
.text-block { background: #1a1a1a; border: 1px solid #444; border-radius: 4px; padding: 15px; margin: 10px 0; white-space: pre-wrap; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; line-height: 1.6; }
.email-preview { background: #fff; color: #333; border-radius: 6px; overflow: hidden; margin: 10px 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
.email-preview .email-header { background: #f5f5f5; padding: 15px 20px; border-bottom: 1px solid #ddd; }
.email-preview .email-header .from-line, .email-preview .email-header .to-line { margin-bottom: 4px; font-size: 13px; color: #555; }
.email-preview .email-header .subject-line { font-size: 16px; color: #222; font-weight: bold; margin-top: 8px; }
.email-preview .email-body { padding: 20px; font-size: 14px; line-height: 1.6; color: #333; white-space: pre-wrap; }
.footer { text-align: center; margin-top: 30px; padding-top: 15px; border-top: 1px solid #333; color: #555; font-size: 12px; }
.phase-label { color: #f39c12; font-size: 16px; font-weight: bold; margin: 20px 0 10px 0; }
.op-banner { text-align: center; background: #c0392b; color: #fff; padding: 15px; border-radius: 6px; margin-bottom: 25px; }
.op-banner h2 { font-size: 22px; letter-spacing: 3px; }
.op-banner .op-subtitle { font-size: 13px; opacity: 0.8; margin-top: 5px; }
.qr-block { font-family: monospace; font-size: 6px; line-height: 6px; letter-spacing: 1px; background: #fff; color: #000; padding: 10px; display: inline-block; border-radius: 4px; }
"""


def _h(text):
    """HTML-escape text to prevent XSS in exported reports."""
    return html_mod.escape(str(text))


def _html_field(label, value):
    """Render a label: value field row in HTML."""
    return f'<div class="field"><span class="label">{_h(label)}:</span> <span class="value">{_h(value)}</span></div>'


def _html_urgency(level):
    """Render urgency with appropriate CSS class."""
    css = f"urgency-{level}" if level in ("high", "critical", "medium", "low") else ""
    return f'<span class="{css}">{_h(level)}</span>'


def _html_list(items):
    """Render a list of items as an HTML unordered list."""
    lis = "\n".join(f"  <li>{_h(item)}</li>" for item in items)
    return f'<ul class="items">\n{lis}\n</ul>'


def _html_text_block(text):
    """Render a block of preformatted text."""
    return f'<div class="text-block">{_h(text)}</div>'


def _html_section(title, content):
    """Wrap content in a titled section card."""
    return (
        f'<div class="section">\n'
        f'  <div class="section-title">{_h(title)}</div>\n'
        f'  {content}\n'
        f'</div>'
    )


def _html_page(body):
    """Wrap body content in a full HTML document with embedded CSS."""
    return (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>REDTEXT Report</title>\n'
        '<style>\n'
        f'{_HTML_CSS}'
        '</style>\n'
        '</head>\n'
        '<body>\n'
        '<div class="report">\n'
        '  <div class="report-header">\n'
        '    <h1>REDTEXT</h1>\n'
        '    <div class="subtitle">Social Engineering Scenario Report</div>\n'
        '  </div>\n'
        f'  {body}\n'
        '  <div class="footer">Generated by REDTEXT Generator &mdash; For authorized red team use only</div>\n'
        '</div>\n'
        '</body>\n'
        '</html>'
    )


# ── HTML renderers (one per scenario type) ────────────────────

def _html_render_phishing(data):
    """Render phishing email as HTML with email preview and metadata."""
    meta_parts = [
        _html_field("Template", data["template"]),
        _html_field("Attacker Persona", data["attacker_persona"]),
        f'<div class="field"><span class="label">Urgency:</span> {_html_urgency(data["urgency_level"])}</div>',
        _html_field("Target Name", data["target"]["name"]),
        _html_field("Target Dept", data["target"]["department"]),
        _html_field("Target Company", data["target"]["company"]),
    ]
    meta_section = _html_section("RED TEAM METADATA", "\n".join(meta_parts))

    company_slug = data["target"]["company"].lower().replace(" ", "")
    from_addr = f'{_h(data["attacker_persona"])} &lt;noreply@{_h(company_slug)}.com&gt;'
    target_slug = data["target"]["name"].lower().replace(" ", ".")
    to_addr = f'{_h(data["target"]["name"])} &lt;{_h(target_slug)}@{_h(company_slug)}.com&gt;'

    email_preview = (
        '<div class="email-preview">\n'
        '  <div class="email-header">\n'
        f'    <div class="from-line"><strong>From:</strong> {from_addr}</div>\n'
        f'    <div class="to-line"><strong>To:</strong> {to_addr}</div>\n'
        f'    <div class="subject-line">{_h(data["subject"])}</div>\n'
        '  </div>\n'
        f'  <div class="email-body">{_h(data["body"])}</div>\n'
        '</div>'
    )
    preview_section = _html_section("EMAIL PREVIEW", email_preview)

    return meta_section + "\n" + preview_section


def _html_render_smishing(data):
    """Render smishing scenario as HTML."""
    parts = [
        _html_field("Template", data["template"]),
        _html_field("Attacker Persona", data["attacker_persona"]),
        f'<div class="field"><span class="label">Urgency:</span> {_html_urgency(data["urgency_level"])}</div>',
        _html_field("Target Name", data["target"]["name"]),
        _html_field("Target Dept", data["target"]["department"]),
        _html_field("Target Company", data["target"]["company"]),
        _html_field("Short Code", data["short_code"]),
        _html_field("Malicious Link", data["malicious_link"]),
    ]
    meta = _html_section("SMS/SMISHING SCENARIO", "\n".join(parts))
    msg = _html_section("SMS MESSAGE", _html_text_block(data["message"]))
    return meta + "\n" + msg


def _html_render_quishing(data):
    """Render quishing scenario as HTML."""
    parts = [
        _html_field("Template", data["template"]),
        _html_field("Attacker Persona", data["attacker_persona"]),
        f'<div class="field"><span class="label">Urgency:</span> {_html_urgency(data["urgency_level"])}</div>',
        _html_field("Target Name", data["target"]["name"]),
        _html_field("Target Dept", data["target"]["department"]),
        _html_field("Target Company", data["target"]["company"]),
        _html_field("Delivery Method", data["delivery_method"]),
        _html_field("Malicious Link", data["malicious_link"]),
    ]
    meta = _html_section("QR CODE PHISHING (QUISHING) SCENARIO", "\n".join(parts))
    pretext = _html_section("PRETEXT (TEXT NEAR QR CODE)", _html_text_block(data["pretext_text"]))
    qr = _html_section("QR CODE", f'<div class="qr-block">{_h(data["qr_ascii"])}</div>')
    placement = _html_section("PLACEMENT SUGGESTIONS", _html_list(data["placement_suggestions"]))
    objectives = _html_section("OBJECTIVES", _html_list(data["objectives"]))
    return "\n".join([meta, pretext, qr, placement, objectives])


def _html_render_vishing(data):
    """Render vishing script as HTML."""
    parts = [
        _html_field("Template", data["template"]),
        _html_field("Caller", data["caller"]),
        f'<div class="field"><span class="label">Urgency:</span> {_html_urgency(data["urgency_level"])}</div>',
        _html_field("Target Name", data["target"]["name"]),
        _html_field("Target Dept", data["target"]["department"]),
        _html_field("Target Company", data["target"]["company"]),
    ]
    meta = _html_section("VISHING CALL SCRIPT", "\n".join(parts))

    sections = []
    for key in ["opening", "escalation", "objective", "red_flags_to_avoid"]:
        label = key.replace("_", " ").upper()
        sections.append(_html_section(label, _html_text_block(data["script"][key])))

    prep = _html_section("PREPARATION", _html_list(data["preparation_notes"]))
    return "\n".join([meta] + sections + [prep])


def _html_render_physical(data):
    """Render physical pretext as HTML."""
    parts = [
        _html_field("Template", data["template"]),
        _html_field("Operator", data["operator"]["name"]),
        _html_field("Cover", data["operator"]["cover_identity"]),
        _html_field("Appearance", data["operator"]["appearance"]),
    ]
    meta = _html_section("PHYSICAL ACCESS PRETEXT", "\n".join(parts))
    props = _html_section("PROPS", _html_list(data["operator"]["props"]))
    script = _html_section("SCRIPT", _html_text_block(data["script"]))
    areas = _html_section("TARGET AREAS", _html_list(data["target_areas"]))
    objectives = _html_section("OBJECTIVES", _html_list(data["objectives"]))
    prep = _html_section("PREPARATION", _html_list(data["preparation_notes"]))
    return "\n".join([meta, props, script, areas, objectives, prep])


def _html_render_full(data):
    """Render full attack scenario as HTML."""
    banner = (
        '<div class="op-banner">\n'
        f'  <h2>{_h(data["operation_name"])}</h2>\n'
        '  <div class="op-subtitle">FULL ATTACK SCENARIO</div>\n'
        '</div>'
    )

    info_parts = [
        _html_field("Target", data["target_company"]),
        _html_field("Industry", data["industry"]),
        _html_field("Season", data["seasonal_hook"]),
    ]
    info = _html_section("OPERATION DETAILS", "\n".join(info_parts))

    recon = '<div class="phase-label">PHASE 1: RECONNAISSANCE</div>\n'
    recon += _html_section("RECON TASKS", _html_list(data["recon_tasks"]))

    phishing = '<div class="phase-label">PHASE 2: PHISHING</div>\n'
    phishing += _html_render_phishing(data["phishing"])

    vishing = '<div class="phase-label">PHASE 3: VISHING</div>\n'
    vishing += _html_render_vishing(data["social"])

    physical = '<div class="phase-label">PHASE 4: PHYSICAL ACCESS</div>\n'
    physical += _html_render_physical(data["physical"])

    opsec = _html_section("OPSEC NOTES", _html_list(data["opsec_notes"]))
    return "\n".join([banner, info, recon, phishing, vishing, physical, opsec])


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


def format_quishing_scenario(data: dict) -> str:
    lines = []
    lines.append(_header("QR CODE PHISHING (QUISHING) SCENARIO"))
    lines.append("")
    lines.append(_field("Template", data["template"]))
    lines.append(_field("Attacker Persona", data["attacker_persona"]))
    lines.append(_field("Urgency", _c(data["urgency_level"].upper(), Colors.RED if data["urgency_level"] in ("high", "critical") else Colors.YELLOW)))
    lines.append("")
    lines.append(_field("Target Name", data["target"]["name"]))
    lines.append(_field("Target Dept", data["target"]["department"]))
    lines.append(_field("Target Company", data["target"]["company"]))
    lines.append("")
    lines.append(_field("Delivery Method", data["delivery_method"]))
    lines.append(_field("Malicious Link", _c(data["malicious_link"], Colors.RED)))
    lines.append("")

    lines.append(f"  {_c('▸ PRETEXT (TEXT NEAR QR CODE)', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for line in data["pretext_text"].split("\n"):
        lines.append(f"    {line}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ QR CODE', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for line in data["qr_ascii"].split("\n"):
        lines.append(f"    {line}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ PLACEMENT SUGGESTIONS', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["placement_suggestions"]))
    lines.append("")

    lines.append(f"  {_c('▸ OBJECTIVES', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["objectives"]))
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
    elif data.get("type") == "quishing":
        content = format_quishing_scenario(data)
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


def export_html(data: dict, filepath: str) -> str:
    """Export scenario data as a self-contained HTML report.

    Dispatches to the appropriate HTML renderer based on data['type']
    or the presence of 'operation_name' (full scenario). Wraps in a
    complete HTML document with embedded CSS.
    """
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else ".", exist_ok=True)

    if data.get("type") == "phishing_email":
        body = _html_render_phishing(data)
    elif data.get("type") == "smishing":
        body = _html_render_smishing(data)
    elif data.get("type") == "quishing":
        body = _html_render_quishing(data)
    elif data.get("type") == "vishing_script":
        body = _html_render_vishing(data)
    elif data.get("type") == "physical_pretext":
        body = _html_render_physical(data)
    elif "operation_name" in data:
        body = _html_render_full(data)
    else:
        body = _html_section("RAW DATA", f"<pre>{_h(json.dumps(data, indent=2))}</pre>")

    page = _html_page(body)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(page)
    return filepath