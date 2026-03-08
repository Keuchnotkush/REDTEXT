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
    opsec_section = _html_render_opsec(data.get("opsec_checklist"))
    mitre_section = _html_render_mitre(data.get("mitre_attack"))

    return meta_section + "\n" + preview_section + "\n" + opsec_section + "\n" + mitre_section


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
    opsec = _html_render_opsec(data.get("opsec_checklist"))
    mitre = _html_render_mitre(data.get("mitre_attack"))
    return meta + "\n" + msg + "\n" + opsec + "\n" + mitre


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
    opsec = _html_render_opsec(data.get("opsec_checklist"))
    mitre = _html_render_mitre(data.get("mitre_attack"))
    return "\n".join([meta, pretext, qr, placement, objectives, opsec, mitre])


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
    opsec = _html_render_opsec(data.get("opsec_checklist"))
    mitre = _html_render_mitre(data.get("mitre_attack"))
    return "\n".join([meta] + sections + [prep, opsec, mitre])


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
    mitre = _html_render_mitre(data.get("mitre_attack"))
    opsec = _html_render_opsec(data.get("opsec_checklist"))
    return "\n".join([meta, props, script, areas, objectives, prep, opsec, mitre])


def _html_render_recon(data):
    """Render recon plan as HTML."""
    parts = [
        _html_field("Template", data["template"]),
        _html_field("Target Company", data["target"]["company"]),
        _html_field("Industry", data["target"]["industry"]),
    ]
    meta = _html_section("RECONNAISSANCE PLAN", "\n".join(parts))
    desc = _html_section("DESCRIPTION", f'<p>{_h(data["description"])}</p>')
    tech = _html_section("TARGET TECHNOLOGY STACK", _html_list(data["target"]["software"]))
    depts = _html_section("TARGET DEPARTMENTS", _html_list(data["target"]["departments"]))

    passive_items = "\n".join(f'  <li><strong>{i}.</strong> {_h(t)}</li>' for i, t in enumerate(data["passive_tasks"], 1))
    passive = _html_section("PASSIVE RECONNAISSANCE", f'<ul class="items">\n{passive_items}\n</ul>')

    active_items = "\n".join(f'  <li><strong>{i}.</strong> {_h(t)}</li>' for i, t in enumerate(data["active_tasks"], 1))
    active = _html_section("ACTIVE RECONNAISSANCE", f'<ul class="items">\n{active_items}\n</ul>')

    tool_items = "\n".join(f'  <li><strong>{_h(n)}</strong> — {_h(d)}</li>' for n, d in data["tools"])
    tools = _html_section("RECOMMENDED TOOLS", f'<ul class="items">\n{tool_items}\n</ul>')
    deliverables = _html_section("DELIVERABLES", _html_list(data["deliverables"]))
    opsec = _html_render_opsec(data.get("opsec_checklist"))
    mitre = _html_render_mitre(data.get("mitre_attack"))
    return "\n".join([meta, desc, tech, depts, passive, active, tools, deliverables, opsec, mitre])


def _html_render_c2(data):
    """Render C2 scenario as HTML."""
    parts = [
        _html_field("Template", data["template"]),
        _html_field("Protocol", data["protocol"]),
        _html_field("Target Company", data["target"]["company"]),
        _html_field("C2 Domain", data["c2_domain"]),
        _html_field("Backup Domain", data["backup_domain"]),
    ]
    meta = _html_section("COMMAND AND CONTROL PLAN", "\n".join(parts))
    desc = _html_section("DESCRIPTION", f'<p>{_h(data["description"])}</p>')

    infra_items = "\n".join(f'  <li><strong>{i}.</strong> {_h(s)}</li>' for i, s in enumerate(data["infrastructure"], 1))
    infra = _html_section("INFRASTRUCTURE SETUP", f'<ul class="items">\n{infra_items}\n</ul>')

    bc = data["beacon_config"]
    bc_parts = []
    for k, v in bc.items():
        if isinstance(v, list):
            v = ", ".join(v)
        bc_parts.append(_html_field(k.replace("_", " ").title(), str(v)))
    beacon = _html_section("BEACON CONFIGURATION", "\n".join(bc_parts))
    cover = _html_section("COVER STORY", _html_text_block(data["cover_story"]))
    evasion = _html_section("EVASION NOTES", _html_list(data["evasion_notes"]))
    detect = _html_section("DETECTION SIGNATURES", _html_list(data["detection_signatures"]))
    opsec = _html_render_opsec(data.get("opsec_checklist"))
    mitre = _html_render_mitre(data.get("mitre_attack"))
    return "\n".join([meta, desc, infra, beacon, cover, evasion, detect, opsec, mitre])


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

    phishing = '<div class="phase-label">PHASE 2: INITIAL ACCESS — PHISHING</div>\n'
    phishing += _html_render_phishing(data["phishing"])

    smishing = ""
    if "smishing" in data:
        smishing = '<div class="phase-label">PHASE 3: INITIAL ACCESS — SMISHING</div>\n'
        smishing += _html_render_smishing(data["smishing"])

    vishing = '<div class="phase-label">PHASE 4: CREDENTIAL ACCESS — VISHING</div>\n'
    vishing += _html_render_vishing(data["social"])

    physical = '<div class="phase-label">PHASE 5: LATERAL MOVEMENT — PHYSICAL ACCESS</div>\n'
    physical += _html_render_physical(data["physical"])

    opsec = _html_section("OPSEC NOTES", _html_list(data["opsec_notes"]))
    mitre = _html_render_full_detection(data.get("mitre_attack"))
    parts = [banner, info, recon, phishing]
    if smishing:
        parts.append(smishing)
    parts.extend([vishing, physical, opsec, mitre])
    return "\n".join(parts)


# ═══════════════════════════════════════════════════════════════
#  MITRE ATT&CK FORMATTERS
# ═══════════════════════════════════════════════════════════════

def _format_mitre_section(mitre_data):
    """Format MITRE ATT&CK data for terminal output."""
    if not mitre_data:
        return ""
    lines = []
    lines.append(f"  {_c('▸ MITRE ATT&CK', Colors.BOLD + Colors.MAGENTA)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append(_field("Tactic", mitre_data.get("tactic", "N/A")))
    for tid, tname in mitre_data.get("techniques", []):
        lines.append(f"    {_c(tid, Colors.YELLOW)}  {tname}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    detection = mitre_data.get("detection", {})
    if detection:
        lines.append(f"  {_c('▸ DETECTION ANALYSIS', Colors.BOLD + Colors.MAGENTA)}")
        lines.append(f"    {_c('Should Detect:', Colors.GREEN)}")
        for item in detection.get("should_detect", []):
            lines.append(f"      {_c('✓', Colors.GREEN)} {item}")
        lines.append(f"    {_c('Why It Often Fails:', Colors.RED)}")
        for item in detection.get("often_fails", []):
            lines.append(f"      {_c('✗', Colors.RED)} {item}")
        lines.append("")
    return "\n".join(lines)


def _format_full_detection(mitre_data):
    """Format aggregated detection analysis for full scenario."""
    if not mitre_data:
        return ""
    lines = []
    lines.append(f"  {_c('▸ MITRE ATT&CK COVERAGE', Colors.BOLD + Colors.MAGENTA)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")

    tactics = mitre_data.get("tactics", [])
    if tactics:
        lines.append(_field("Tactics", " → ".join(tactics)))

    for tid, tname in mitre_data.get("techniques", []):
        lines.append(f"    {_c(tid, Colors.YELLOW)}  {tname}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    det = mitre_data.get("detection_analysis", {})
    if det:
        lines.append(_header("DETECTION GAP ANALYSIS"))
        lines.append("")
        lines.append(f"    {_c('What Should Detect This Attack:', Colors.GREEN)}")
        for item in det.get("should_detect", []):
            lines.append(f"      {_c('✓', Colors.GREEN)} {item}")
        lines.append("")
        lines.append(f"    {_c('Why Detection Often Fails:', Colors.RED)}")
        for item in det.get("often_fails", []):
            lines.append(f"      {_c('✗', Colors.RED)} {item}")
        lines.append("")
    return "\n".join(lines)


def _html_render_mitre(mitre_data):
    """Render MITRE ATT&CK section as HTML."""
    if not mitre_data:
        return ""
    techs = "\n".join(
        f'  <li><strong>{_h(tid)}</strong> — {_h(tname)}</li>'
        for tid, tname in mitre_data.get("techniques", [])
    )
    tech_list = f'<ul class="items">\n{techs}\n</ul>'
    meta = _html_field("Tactic", mitre_data.get("tactic", "N/A")) + "\n" + tech_list
    parts = [_html_section("MITRE ATT&CK", meta)]

    detection = mitre_data.get("detection", {})
    if detection:
        det_parts = ['<div class="phase-label">Should Detect</div>']
        det_parts.append(_html_list(detection.get("should_detect", [])))
        det_parts.append('<div class="phase-label">Why It Often Fails</div>')
        det_parts.append(_html_list(detection.get("often_fails", [])))
        parts.append(_html_section("DETECTION ANALYSIS", "\n".join(det_parts)))

    return "\n".join(parts)


def _html_render_full_detection(mitre_data):
    """Render aggregated MITRE data for full scenario HTML."""
    if not mitre_data:
        return ""
    techs = "\n".join(
        f'  <li><strong>{_h(tid)}</strong> — {_h(tname)}</li>'
        for tid, tname in mitre_data.get("techniques", [])
    )
    tactics = mitre_data.get("tactics", [])
    tactic_str = " → ".join(tactics) if tactics else "N/A"
    meta = _html_field("Attack Chain", tactic_str) + "\n" + f'<ul class="items">\n{techs}\n</ul>'
    parts = [_html_section("MITRE ATT&CK COVERAGE", meta)]

    det = mitre_data.get("detection_analysis", {})
    if det:
        det_parts = ['<div class="phase-label">What Should Detect This Attack</div>']
        det_parts.append(_html_list(det.get("should_detect", [])))
        det_parts.append('<div class="phase-label">Why Detection Often Fails</div>')
        det_parts.append(_html_list(det.get("often_fails", [])))
        parts.append(_html_section("DETECTION GAP ANALYSIS", "\n".join(det_parts)))

    return "\n".join(parts)


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
    lines.append(_format_opsec_section(data.get("opsec_checklist")))
    lines.append(_format_mitre_section(data.get("mitre_attack")))
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
    lines.append(_format_opsec_section(data.get("opsec_checklist")))
    lines.append(_format_mitre_section(data.get("mitre_attack")))
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
    lines.append(_format_opsec_section(data.get("opsec_checklist")))
    lines.append(_format_mitre_section(data.get("mitre_attack")))
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
    lines.append(_format_opsec_section(data.get("opsec_checklist")))
    lines.append(_format_mitre_section(data.get("mitre_attack")))
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
    lines.append(_format_opsec_section(data.get("opsec_checklist")))
    lines.append(_format_mitre_section(data.get("mitre_attack")))
    return "\n".join(lines)


def _format_opsec_section(checklist):
    """Format OPSEC checklist for terminal output."""
    if not checklist:
        return ""
    lines = []
    lines.append(f"  {_c('▸ OPSEC CHECKLIST', Colors.BOLD + Colors.MAGENTA)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for item in checklist:
        lines.append(f"    {_c('□', Colors.YELLOW)} {item}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")
    return "\n".join(lines)


def _html_render_opsec(checklist):
    """Render OPSEC checklist as HTML."""
    if not checklist:
        return ""
    items = "\n".join(f'  <li>&#9744; {_h(item)}</li>' for item in checklist)
    content = f'<ul class="items">\n{items}\n</ul>'
    return _html_section("OPSEC CHECKLIST", content)


def format_recon_plan(data: dict) -> str:
    lines = []
    lines.append(_header("RECONNAISSANCE PLAN"))
    lines.append("")
    lines.append(_field("Template", data["template"]))
    lines.append(_field("Target Company", data["target"]["company"]))
    lines.append(_field("Industry", data["target"]["industry"]))
    lines.append("")
    lines.append(f"    {_c(data['description'], Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ TARGET TECHNOLOGY STACK', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["target"]["software"]))
    lines.append("")

    lines.append(f"  {_c('▸ TARGET DEPARTMENTS', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["target"]["departments"]))
    lines.append("")

    lines.append(f"  {_c('▸ PASSIVE RECONNAISSANCE', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for i, task in enumerate(data["passive_tasks"], 1):
        lines.append(f"    {_c(f'{i:2d}.', Colors.GREEN)} {task}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ ACTIVE RECONNAISSANCE', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for i, task in enumerate(data["active_tasks"], 1):
        lines.append(f"    {_c(f'{i:2d}.', Colors.RED)} {task}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ RECOMMENDED TOOLS', Colors.BOLD + Colors.YELLOW)}")
    for tool_name, tool_desc in data["tools"]:
        lines.append(f"    {_c(tool_name, Colors.CYAN):40s} {_c(tool_desc, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ DELIVERABLES', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["deliverables"]))
    lines.append("")
    lines.append(_format_opsec_section(data.get("opsec_checklist")))
    lines.append(_format_mitre_section(data.get("mitre_attack")))
    return "\n".join(lines)


def format_c2_scenario(data: dict) -> str:
    lines = []
    lines.append(_header("COMMAND AND CONTROL PLAN"))
    lines.append("")
    lines.append(_field("Template", data["template"]))
    lines.append(_field("Protocol", data["protocol"]))
    lines.append(_field("Target Company", data["target"]["company"]))
    lines.append(_field("C2 Domain", _c(data["c2_domain"], Colors.RED)))
    lines.append(_field("Backup Domain", _c(data["backup_domain"], Colors.RED)))
    lines.append("")
    lines.append(f"    {_c(data['description'], Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ INFRASTRUCTURE SETUP', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for i, step in enumerate(data["infrastructure"], 1):
        lines.append(f"    {_c(f'{i:2d}.', Colors.GREEN)} {step}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ BEACON CONFIGURATION', Colors.BOLD + Colors.YELLOW)}")
    bc = data["beacon_config"]
    for key, val in bc.items():
        if isinstance(val, list):
            val = ", ".join(val)
        lines.append(_field(key.replace("_", " ").title(), str(val)))
    lines.append("")

    lines.append(f"  {_c('▸ COVER STORY', Colors.BOLD + Colors.YELLOW)}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    for line in data["cover_story"].split("\n"):
        lines.append(f"    {line}")
    lines.append(f"    {_c('─' * 60, Colors.DIM)}")
    lines.append("")

    lines.append(f"  {_c('▸ EVASION NOTES', Colors.BOLD + Colors.YELLOW)}")
    lines.append(_list_items(data["evasion_notes"]))
    lines.append("")

    lines.append(f"  {_c('▸ DETECTION SIGNATURES (for blue team)', Colors.BOLD + Colors.RED)}")
    lines.append(_list_items(data["detection_signatures"]))
    lines.append("")
    lines.append(_format_opsec_section(data.get("opsec_checklist")))
    lines.append(_format_mitre_section(data.get("mitre_attack")))
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

    lines.append(f"  {_c('▸ PHASE 2: INITIAL ACCESS — PHISHING', Colors.BOLD + Colors.YELLOW)}")
    lines.append(format_phishing_email(data["phishing"]))

    if "smishing" in data:
        lines.append(f"  {_c('▸ PHASE 3: INITIAL ACCESS — SMISHING', Colors.BOLD + Colors.YELLOW)}")
        lines.append(format_smishing_message(data["smishing"]))

    lines.append(f"  {_c('▸ PHASE 4: CREDENTIAL ACCESS — VISHING', Colors.BOLD + Colors.YELLOW)}")
    lines.append(format_vishing_script(data["social"]))

    lines.append(f"  {_c('▸ PHASE 5: LATERAL MOVEMENT — PHYSICAL ACCESS', Colors.BOLD + Colors.YELLOW)}")
    lines.append(format_physical_pretext(data["physical"]))

    lines.append(_header("OPSEC NOTES"))
    lines.append(_list_items(data["opsec_notes"]))
    lines.append("")

    lines.append(_format_full_detection(data.get("mitre_attack")))
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
    elif data.get("type") == "recon":
        content = format_recon_plan(data)
    elif data.get("type") == "c2":
        content = format_c2_scenario(data)
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
    elif data.get("type") == "recon":
        body = _html_render_recon(data)
    elif data.get("type") == "c2":
        body = _html_render_c2(data)
    elif "operation_name" in data:
        body = _html_render_full(data)
    else:
        body = _html_section("RAW DATA", f"<pre>{_h(json.dumps(data, indent=2))}</pre>")

    page = _html_page(body)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(page)
    return filepath


def export_report(data: dict, filepath: str) -> str:
    """Export scenario as a structured red team findings report (Markdown)."""
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else ".", exist_ok=True)

    lines = []
    lines.append("# Red Team Findings Report")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    scenario_type = data.get("type", "full scenario")
    if "operation_name" in data:
        lines.append(f"**Operation:** {data['operation_name']}")
        lines.append(f"**Target:** {data.get('target_company', 'N/A')}")
        lines.append(f"**Industry:** {data.get('industry', 'N/A')}")
    elif "target" in data:
        lines.append(f"**Scenario Type:** {scenario_type.replace('_', ' ').title()}")
        lines.append(f"**Target Company:** {data['target'].get('company', 'N/A')}")
    lines.append("")

    # MITRE ATT&CK Coverage
    mitre = data.get("mitre_attack", {})
    if mitre:
        lines.append("## MITRE ATT&CK Coverage")
        lines.append("")
        tactics = mitre.get("tactics", [])
        tactic = mitre.get("tactic", "")
        if tactics:
            lines.append(f"**Attack Chain:** {' → '.join(tactics)}")
        elif tactic:
            lines.append(f"**Tactic:** {tactic}")
        lines.append("")
        lines.append("| Technique ID | Name |")
        lines.append("|-------------|------|")
        for tid, tname in mitre.get("techniques", []):
            lines.append(f"| {tid} | {tname} |")
        lines.append("")

    # Findings
    lines.append("## Findings")
    lines.append("")
    if data.get("type") == "phishing_email":
        lines.append(f"### Finding 1: Phishing Email — {data.get('template', 'N/A')}")
        lines.append(f"- **Severity:** High")
        lines.append(f"- **Subject:** {data.get('subject', 'N/A')}")
        lines.append(f"- **Target:** {data.get('target', {}).get('name', 'N/A')} ({data.get('target', {}).get('department', 'N/A')})")
        lines.append(f"- **Persona:** {data.get('attacker_persona', 'N/A')}")
    elif data.get("type") == "vishing_script":
        lines.append(f"### Finding 1: Vishing Script — {data.get('template', 'N/A')}")
        lines.append(f"- **Severity:** High")
        lines.append(f"- **Caller:** {data.get('caller', 'N/A')}")
        lines.append(f"- **Target:** {data.get('target', {}).get('name', 'N/A')}")
    elif data.get("type") == "recon":
        lines.append(f"### Finding 1: Reconnaissance Plan — {data.get('template', 'N/A')}")
        lines.append(f"- **Severity:** Medium")
        lines.append(f"- **Passive tasks:** {len(data.get('passive_tasks', []))}")
        lines.append(f"- **Active tasks:** {len(data.get('active_tasks', []))}")
    elif data.get("type") == "c2":
        lines.append(f"### Finding 1: C2 Channel — {data.get('template', 'N/A')}")
        lines.append(f"- **Severity:** Critical")
        lines.append(f"- **Protocol:** {data.get('protocol', 'N/A')}")
        lines.append(f"- **C2 Domain:** {data.get('c2_domain', 'N/A')}")
    elif "operation_name" in data:
        finding_num = 1
        for phase_key, phase_name in [("phishing", "Phishing"), ("smishing", "Smishing"),
                                       ("social", "Vishing"), ("physical", "Physical")]:
            if phase_key in data:
                sub = data[phase_key]
                lines.append(f"### Finding {finding_num}: {phase_name} — {sub.get('template', 'N/A')}")
                lines.append(f"- **Severity:** High")
                if "subject" in sub:
                    lines.append(f"- **Subject:** {sub['subject']}")
                lines.append("")
                finding_num += 1
    else:
        lines.append(f"### Finding 1: {scenario_type.replace('_', ' ').title()}")
        lines.append(f"- **Template:** {data.get('template', 'N/A')}")
    lines.append("")

    # Detection Gap Analysis
    det = mitre.get("detection_analysis", mitre.get("detection", {}))
    if det:
        lines.append("## Detection Gap Analysis")
        lines.append("")
        should = det.get("should_detect", [])
        fails = det.get("often_fails", [])
        if should:
            lines.append("### What Should Detect This Attack")
            for item in should:
                lines.append(f"- [x] {item}")
            lines.append("")
        if fails:
            lines.append("### Why Detection Often Fails")
            for item in fails:
                lines.append(f"- [ ] {item}")
            lines.append("")

    # OPSEC Notes
    opsec = data.get("opsec_checklist", data.get("opsec_notes", []))
    if opsec:
        lines.append("## Operator OPSEC Checklist")
        lines.append("")
        for item in opsec:
            lines.append(f"- [ ] {item}")
        lines.append("")

    # Recommendations
    lines.append("## Recommendations")
    lines.append("")
    if det.get("should_detect"):
        lines.append("Based on the detection gap analysis, the following controls should be verified:")
        lines.append("")
        for i, item in enumerate(det.get("should_detect", [])[:5], 1):
            lines.append(f"{i}. {item}")
        lines.append("")

    lines.append("---")
    lines.append("*Generated by REDTEXT Generator | For authorized red team use only*")
    lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return filepath