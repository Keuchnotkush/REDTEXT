"""
Blue-team defense playbook generation.

Turns any REDTEXT attack scenario into a defender's playbook: the telemetry to
collect, detection controls to verify, user-facing warning signs, incident
response steps, and debrief talking points — all mapped to the scenario's
MITRE ATT&CK techniques.

This module is purely defensive. It consumes the ``mitre_attack`` data that the
generator already attaches to every scenario and emits guidance for the blue
team. It produces no offensive content of its own, so it is safe to share with
defenders who should never see the attacker-side pretext.
"""

# ═══════════════════════════════════════════════════════════════
#  TECHNIQUE → TELEMETRY / DATA SOURCES
# ═══════════════════════════════════════════════════════════════
#
# Keyed by the base ATT&CK technique ID (the part before any sub-technique
# dot, e.g. "T1566" covers T1566.001/.002/...). These are the log sources and
# sensors a defender needs in place to have any chance of catching the vector.

TECHNIQUE_DATA_SOURCES = {
    "T1566": [
        "Email gateway and message-tracking logs",
        "Web proxy and DNS resolution logs",
        "User-reported phishing mailbox",
    ],
    "T1078": [
        "IdP / SSO sign-in logs",
        "Impossible-travel and anomalous-logon analytics",
    ],
    "T1204": [
        "Process-creation telemetry (EDR / Sysmon Event ID 1)",
        "Browser download history",
    ],
    "T1059": [
        "PowerShell script-block and module logging (Event ID 4104)",
        "Command-line process auditing",
    ],
    "T1110": [
        "Authentication failure logs",
        "SIEM correlation of auth attempts across accounts",
    ],
    "T1534": [
        "Internal email-flow logs",
        "Mailbox audit logging",
    ],
    "T1556": [
        "IdP configuration-change logs",
        "MFA enrollment and method-change events",
    ],
    "T1195": [
        "Software deployment / patch-management logs",
        "Code-signing and checksum verification events",
    ],
    "T1199": [
        "Third-party / vendor remote-access logs",
    ],
    "T1111": [
        "MFA provider logs",
        "Token issuance and reuse analytics",
    ],
    "T1557": [
        "Network session logs",
        "TLS / proxy inspection logs",
    ],
    "T1056": [
        "Web-portal access logs",
    ],
    "T1200": [
        "Network access control (802.1X) events",
        "New-device DHCP and switch-port logs",
        "Physical access / badge-reader logs",
    ],
    "T1091": [
        "USB device-insertion events (endpoint)",
    ],
    "T1040": [
        "Switch port-mirroring and NAC alerts",
    ],
    "T1589": ["External attack-surface and brand monitoring"],
    "T1590": ["DNS query logs", "External attack-surface monitoring"],
    "T1591": ["Threat-intel and brand-mention monitoring"],
    "T1592": ["Web-server access logs", "Scanning / fingerprinting alerts"],
    "T1593": ["Social-media and open-web monitoring"],
    "T1595": ["IDS/IPS scan-detection alerts", "WAF fingerprinting alerts"],
    "T1558": [
        "Active Directory Kerberos ticket events (Event ID 4769)",
        "Service-principal-name query monitoring",
    ],
    "T1562": [
        "EDR tamper-protection alerts",
        "Security-tool state-change events",
    ],
    "T1218": [
        "Process creation with command-line auditing",
        "Network connections from signed system binaries",
    ],
    "T1105": [
        "Proxy / firewall egress logs",
        "File-download telemetry",
    ],
    "T1071": [
        "Network-flow (NetFlow / Zeek) logs",
        "TLS metadata and JA3/JA3S fingerprints",
        "Web proxy logs",
    ],
    "T1573": [
        "TLS inspection logs",
        "Certificate-transparency monitoring",
    ],
    "T1571": ["Firewall allow/deny logs by port"],
    "T1568": ["DNS query logs", "Newly-observed-domain feeds"],
    "T1090": [
        "CDN access logs",
        "SNI vs Host-header mismatch analysis",
    ],
    "T1048": ["DLP alerts", "Off-hours egress flow analytics"],
    "T1567": ["CASB cloud-application logs", "DLP alerts"],
    "T1030": ["Large/chunked-transfer flow analytics"],
}

_DEFAULT_DATA_SOURCES = [
    "Endpoint detection & response (EDR) telemetry",
    "SIEM-aggregated authentication and network logs",
    "User-reported phishing / suspicious-activity mailbox",
]


# ═══════════════════════════════════════════════════════════════
#  VECTOR → USER-FACING WARNING SIGNS
# ═══════════════════════════════════════════════════════════════

VECTOR_RED_FLAGS = {
    "phishing_email": [
        "Sender domain differs from the real one by a character or a TLD",
        "Urgent deadline or a threat of losing access",
        "Link hostname does not match the brand it claims to be",
        "Unexpected attachment, or a request to 'enable content'",
        "Generic greeting or subtle grammar and formatting errors",
    ],
    "smishing": [
        "Unknown short code or number claiming to be a known brand",
        "Shortened or mismatched link inside the text message",
        "Request to pay a small 'fee' or to 'verify' urgently",
        "Message arrives with no context — no order, no login attempt",
    ],
    "quishing": [
        "A QR code where the real process would use an app or 802.1X",
        "A sticker or printout placed over existing signage",
        "The QR code leads to a login page you did not expect",
        "No URL preview is shown before the page loads",
    ],
    "vishing_script": [
        "Caller pressures you to act before you can verify them",
        "Request to disable security tools or read back a one-time code",
        "Caller claims to be IT but asks for credentials or remote access",
        "Refuses to let you call back through the official directory",
    ],
    "physical_pretext": [
        "Visitor without a verified work order or an escort",
        "Requests access to server rooms, wiring closets, or desks",
        "Vague answers about who authorized the visit",
        "Brings tools or bags into sensitive areas unaccompanied",
    ],
    "recon": [
        "Spike in profile views or connection requests to key staff",
        "Systematic crawling of careers and about pages",
        "SMTP address-probing (VRFY/RCPT) against the mail gateway",
        "Scanning or fingerprinting of public-facing assets",
    ],
    "c2": [
        "Regular, fixed-interval outbound connections (beaconing)",
        "Connections to newly registered or uncategorized domains",
        "Unusual DNS volume or abnormally long subdomain labels",
        "Off-hours outbound transfers to cloud storage",
    ],
}


# ═══════════════════════════════════════════════════════════════
#  VECTOR → INCIDENT RESPONSE STEPS
# ═══════════════════════════════════════════════════════════════

VECTOR_RESPONSE = {
    "phishing_email": [
        "Preserve the email (full headers + body) and pull delivery logs for every recipient.",
        "Contain: block the sender, the URLs, and any lookalike domain at the gateway and proxy.",
        "Identify who clicked or submitted credentials from proxy and IdP sign-in logs.",
        "Force a password reset and revoke active sessions/tokens for affected accounts.",
        "Hunt for inbox rules, OAuth grants, and follow-on logins created after the click.",
        "Debrief the targeted group and reinforce the one-click reporting path.",
    ],
    "smishing": [
        "Capture the message, sender ID, and link, then report the number to the carrier.",
        "Block the destination domain at the mobile proxy / MDM and on the web gateway.",
        "Check whether any recipient entered credentials or a one-time code.",
        "Reset credentials and revoke sessions for anyone who interacted with the link.",
        "Remind staff that the real brand's app — not an SMS link — is the source of truth.",
    ],
    "quishing": [
        "Recover and photograph the physical QR code / signage as evidence.",
        "Sweep the area for other tampered codes and remove them.",
        "Block the destination domain and review portal sign-in logs for the landing page.",
        "Reset credentials for anyone who authenticated through the fake page.",
        "Verify the legitimate process (app or 802.1X) is clearly signposted where codes appeared.",
    ],
    "vishing_script": [
        "Have the targeted user report the call details to the help desk immediately.",
        "Verify no remote-access session, password reset, or tool change was performed.",
        "If any action was taken, revoke sessions, reset credentials, and re-enable defenses.",
        "Review help-desk and PAM logs for related calls to other staff.",
        "Reaffirm the callback-through-the-directory rule and no-credentials-by-phone policy.",
    ],
    "physical_pretext": [
        "Alert physical security and locate / escort the visitor out.",
        "Review badge-reader and camera footage for the areas accessed.",
        "Sweep accessed areas and network ports for rogue or added devices.",
        "Validate the work order with building management and the named sponsor.",
        "Re-brief reception and staff on escort and work-order verification.",
    ],
    "recon": [
        "Characterize the activity from web, DNS, and mail-gateway logs.",
        "Reduce exposed attack surface and tighten public-profile data where possible.",
        "Add the observed sources and patterns to monitoring and threat-intel watchlists.",
        "Warn high-value targets (executives, admins) to expect follow-on social engineering.",
    ],
    "c2": [
        "Isolate the suspected host from the network while preserving volatile evidence.",
        "Block the C2 and backup domains/IPs at the firewall, proxy, and DNS.",
        "Triage the host: persistence, injected processes, and lateral-movement attempts.",
        "Rotate credentials and secrets exposed on the affected host.",
        "Reimage from a known-good baseline before returning the host to service.",
    ],
}


# Human-readable labels for each attack vector.
VECTOR_LABELS = {
    "phishing_email": "Phishing Email",
    "smishing": "Smishing (SMS)",
    "quishing": "QR Code Phishing (Quishing)",
    "vishing_script": "Vishing Call",
    "physical_pretext": "Physical Access Pretext",
    "recon": "Reconnaissance",
    "c2": "Command and Control",
    "full": "Full Multi-Vector Attack",
}

# General awareness points, always included in the debrief.
_GENERAL_AWARENESS = [
    "Verify through a second, trusted channel before acting on any urgent request.",
    "Urgency and authority are the two levers every one of these pretexts pulls.",
    "Reporting a suspicious contact early is always better than staying silent.",
]


# ═══════════════════════════════════════════════════════════════
#  INTERNAL HELPERS
# ═══════════════════════════════════════════════════════════════

def _base_technique_id(technique_id):
    """Return the base ATT&CK ID, dropping any sub-technique suffix."""
    return technique_id.split(".")[0]


def _dedupe(items):
    """De-duplicate a list while preserving first-seen order."""
    return list(dict.fromkeys(items))


def _vectors_in(scenario):
    """Return the ordered list of attack-vector keys present in a scenario."""
    if "operation_name" in scenario and scenario.get("type") != "defense_playbook":
        vectors = []
        for phase_key in ("phishing", "smishing", "social", "physical"):
            sub = scenario.get(phase_key)
            if isinstance(sub, dict) and sub.get("type"):
                vectors.append(sub["type"])
        return vectors
    vector = scenario.get("type")
    return [vector] if vector else []


def _collect_detection(scenario):
    """Pull (should_detect, often_fails) from a scenario's MITRE data.

    Handles both single scenarios (``detection``) and full scenarios
    (``detection_analysis``).
    """
    mitre = scenario.get("mitre_attack", {}) or {}
    det = mitre.get("detection_analysis") or mitre.get("detection") or {}
    should = list(det.get("should_detect", []))
    fails = list(det.get("often_fails", []))
    return should, fails


def data_sources_for(techniques):
    """Map a list of (id, name) techniques to the telemetry needed to catch them."""
    sources = []
    for tid, _name in techniques:
        sources.extend(TECHNIQUE_DATA_SOURCES.get(_base_technique_id(tid), []))
    sources = _dedupe(sources)
    return sources or list(_DEFAULT_DATA_SOURCES)


# ═══════════════════════════════════════════════════════════════
#  PUBLIC API
# ═══════════════════════════════════════════════════════════════

def build_defense_playbook(scenario):
    """Build a blue-team defense playbook from any generated scenario.

    Args:
        scenario: a scenario dict produced by ``RedtextGenerator`` (any vector,
            including a full multi-vector scenario).

    Returns:
        A dict with ``type`` ``"defense_playbook"`` describing the detection,
        response, and awareness guidance for that scenario.
    """
    mitre = scenario.get("mitre_attack", {}) or {}
    techniques = list(mitre.get("techniques", []))
    should_detect, known_gaps = _collect_detection(scenario)

    vectors = _vectors_in(scenario)
    is_full = "operation_name" in scenario and scenario.get("type") != "defense_playbook"
    vector_key = "full" if is_full else (vectors[0] if vectors else "phishing_email")

    red_flags = []
    response_steps = []
    for vec in vectors:
        red_flags.extend(VECTOR_RED_FLAGS.get(vec, []))
        response_steps.extend(VECTOR_RESPONSE.get(vec, []))
    red_flags = _dedupe(red_flags)
    response_steps = _dedupe(response_steps)

    if is_full:
        tactic = " → ".join(mitre.get("tactics", [])) or "Multiple"
    else:
        tactic = mitre.get("tactic", "N/A")

    target = scenario.get("target", {}) or {}
    company = (
        scenario.get("target_company")
        or target.get("company")
        or "the target organization"
    )

    return {
        "type": "defense_playbook",
        "vector": vector_key,
        "vector_label": VECTOR_LABELS.get(vector_key, vector_key),
        "target_company": company,
        "tactic": tactic,
        "techniques": techniques,
        "data_sources": data_sources_for(techniques),
        "detection_controls": _dedupe(should_detect),
        "known_gaps": _dedupe(known_gaps),
        "user_red_flags": red_flags,
        "response_steps": response_steps,
        "awareness_points": list(_GENERAL_AWARENESS),
        "source_scenario": scenario.get("template", scenario.get("operation_name", "")),
        "language": scenario.get("language", "en"),
    }
