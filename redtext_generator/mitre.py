"""
MITRE ATT&CK framework integration for REDTEXT scenarios.
Maps scenario templates to ATT&CK techniques, tactics, and detection analysis.
"""

# ═══════════════════════════════════════════════════════════════
#  ATT&CK PHASE DEFINITIONS
# ═══════════════════════════════════════════════════════════════

ATTACK_PHASES = {
    "recon": "Reconnaissance",
    "initial-access": "Initial Access",
    "execution": "Execution",
    "persistence": "Persistence",
    "privilege-escalation": "Privilege Escalation",
    "defense-evasion": "Defense Evasion",
    "credential-access": "Credential Access",
    "discovery": "Discovery",
    "lateral-movement": "Lateral Movement",
    "collection": "Collection",
    "c2": "Command and Control",
    "exfiltration": "Exfiltration",
}

# Phase → recommended scenario CLI type
PHASE_TO_SCENARIO = {
    "recon": "recon",
    "initial-access": "phishing",
    "execution": "phishing",
    "credential-access": "vishing",
    "privilege-escalation": "vishing",
    "defense-evasion": "phishing",
    "discovery": "physical",
    "lateral-movement": "physical",
    "collection": "physical",
    "c2": "c2",
    "exfiltration": "c2",
}

# ═══════════════════════════════════════════════════════════════
#  SCENARIO → ATT&CK TECHNIQUE MAPPING
# ═══════════════════════════════════════════════════════════════

SCENARIO_TECHNIQUES = {
    "phishing_email": {
        "credential_harvest": {
            "techniques": [
                ("T1566.002", "Phishing: Spearphishing Link"),
                ("T1078", "Valid Accounts"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Email gateway: flag external sender spoofing internal domain",
                    "URL filter: block newly registered or low-reputation domains",
                    "Browser isolation: prevent credential entry on untrusted sites",
                    "FIDO2/WebAuthn: phishing-resistant MFA blocks credential replay",
                ],
                "often_fails": [
                    "Lookalike domains (targetc0rp.com) bypass exact-match filters",
                    "Domains aged 30+ days build enough reputation to pass checks",
                    "Users click 'security' links without inspecting the domain",
                    "Real-time phishing proxy captures and replays MFA tokens",
                ],
            },
        },
        "malicious_attachment": {
            "techniques": [
                ("T1566.001", "Phishing: Spearphishing Attachment"),
                ("T1204.002", "User Execution: Malicious File"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Email gateway: sandbox and detonate attachments before delivery",
                    "EDR: detect macro execution and suspicious child processes",
                    "Application control: block unauthorized executables and scripts",
                    "Network IDS: detect C2 callbacks after document open",
                ],
                "often_fails": [
                    "Password-protected archives bypass gateway sandbox scanning",
                    "Macro-less exploits (DDE, OLE, template injection) evade macro policies",
                    "Signed binaries and LOLBins bypass application control",
                    "Encrypted C2 blends with normal HTTPS traffic",
                ],
            },
        },
        "bec_wire": {
            "techniques": [
                ("T1534", "Internal Spearphishing"),
                ("T1566.002", "Phishing: Spearphishing Link"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Email security: flag display name spoofing with external sender",
                    "Payment controls: dual-authorization for wire transfers over threshold",
                    "Out-of-band verification: callback to known number before processing",
                    "AI email analysis: detect urgency manipulation patterns",
                ],
                "often_fails": [
                    "Compromised mailbox bypasses all email-level controls",
                    "Authority pressure overrides financial controls",
                    "Employees skip verification for perceived executive requests",
                    "BEC uses no malware — purely social, no signatures to detect",
                ],
            },
        },
        "callback_phishing": {
            "techniques": [
                ("T1566.003", "Phishing: Spearphishing via Service"),
                ("T1204.001", "User Execution: Malicious Link"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Email gateway: flag fake invoice/receipt patterns",
                    "Phone system: block known scam callback numbers",
                    "Security awareness: recognize unsolicited charge notifications",
                    "Threat intel: block known callback phishing numbers",
                ],
                "often_fails": [
                    "Callback numbers rotate faster than threat intel updates",
                    "Legitimate-looking invoices create urgency bypassing training",
                    "Phone-based social engineering has no digital signature",
                    "Templates rotate faster than ML models retrain",
                ],
            },
        },
        "supply_chain": {
            "techniques": [
                ("T1195.002", "Supply Chain Compromise: Software Supply Chain"),
                ("T1199", "Trusted Relationship"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Vendor verification: confirm updates through official channels",
                    "Software integrity: verify digital signatures and checksums",
                    "Change management: all updates go through IT approval",
                    "Network monitoring: detect unexpected download sources",
                ],
                "often_fails": [
                    "Trusted vendor domain lowers suspicion and bypasses filters",
                    "Users trust vendor communications without verification",
                    "Emergency patches create urgency bypassing change management",
                    "Spoofed vendor email addresses pass casual inspection",
                ],
            },
        },
        "credential_breach": {
            "techniques": [
                ("T1566.002", "Phishing: Spearphishing Link"),
                ("T1110.004", "Brute Force: Credential Stuffing"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "Email gateway: flag password reset links to non-corporate domains",
                    "Security team: breach notifications come from internal security only",
                    "Password manager: auto-fill won't trigger on fake reset pages",
                    "SIEM: correlate password reset attempts across multiple users",
                ],
                "often_fails": [
                    "Real breach anxiety makes users act impulsively",
                    "Phishing page mimics corporate SSO portal pixel-perfectly",
                    "Users without password managers type credentials on any page",
                    "Breach notifications are common enough to seem legitimate",
                ],
            },
        },
        "password_policy_change": {
            "techniques": [
                ("T1566.002", "Phishing: Spearphishing Link"),
                ("T1110.001", "Brute Force: Password Guessing"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "Email gateway: flag password reset links to non-corporate domains",
                    "SSO monitoring: detect login attempts from unfamiliar infrastructure",
                    "Security awareness: policy changes communicated through official channels",
                    "Password manager: auto-fill only triggers on legitimate SSO domains",
                ],
                "often_fails": [
                    "Password fatigue makes users comply without verifying the source",
                    "Realistic policy language passes casual inspection",
                    "Fear of account lockout creates urgency to comply",
                    "Users type credentials on any page that looks like the SSO portal",
                ],
            },
        },
        "sso_migration": {
            "techniques": [
                ("T1556", "Modify Authentication Process"),
                ("T1078", "Valid Accounts"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "IT comms: SSO migrations announced through verified internal channels",
                    "Email gateway: flag SSO verification links to external domains",
                    "MFA: phishing-resistant MFA blocks credential replay",
                    "SSO monitoring: detect authentication to non-corporate identity providers",
                ],
                "often_fails": [
                    "SSO migrations are plausible and expected events",
                    "Users trust emails referencing executive approval",
                    "Real-time proxy captures and replays MFA tokens",
                    "Deadline pressure prevents verification through IT",
                ],
            },
        },
        "macro_document": {
            "techniques": [
                ("T1204.002", "User Execution: Malicious File"),
                ("T1059.001", "Command and Scripting Interpreter: PowerShell"),
            ],
            "tactic": "Defense Evasion",
            "detection": {
                "should_detect": [
                    "Email gateway: strip or sandbox macro-enabled attachments",
                    "Group Policy: disable macros from untrusted sources",
                    "EDR: detect suspicious child processes from Office applications",
                    "Application control: block unsigned macro execution",
                ],
                "often_fails": [
                    "Protected View bypass instructions override security warnings",
                    "Encrypted/password-protected documents bypass gateway scanning",
                    "Users enable macros when told the document is 'encrypted'",
                    "Macro-less techniques (DDE, template injection) bypass macro policies",
                ],
            },
        },
        "powershell_diagnostic": {
            "techniques": [
                ("T1059.001", "Command and Scripting Interpreter: PowerShell"),
                ("T1204.002", "User Execution: Malicious File"),
            ],
            "tactic": "Execution",
            "detection": {
                "should_detect": [
                    "EDR: flag powershell -ep bypass and download cradle patterns",
                    "AMSI: detect malicious script content at runtime",
                    "Script block logging: capture and alert on suspicious commands",
                    "Application control: constrained language mode for PowerShell",
                ],
                "often_fails": [
                    "Users trust IT-branded emails with 'run this command' instructions",
                    "Encoded commands bypass simple string-matching rules",
                    "AMSI bypass techniques disable runtime inspection",
                    "Administrative privilege escalation via social engineering",
                ],
            },
        },
    },

    "smishing": {
        "account_verify": {
            "techniques": [
                ("T1566", "Phishing"),
                ("T1078", "Valid Accounts"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Mobile security: URL reputation check before loading links",
                    "SMS filtering: block messages from unknown short codes",
                    "Security awareness: verify status through official app",
                    "MDM: restrict browser access to unapproved domains",
                ],
                "often_fails": [
                    "SMS lacks email-level authentication (no SPF/DKIM)",
                    "Short URLs obscure the destination domain",
                    "Mobile browsers show minimal URL bar",
                    "Account lockout fear creates urgency bypassing training",
                ],
            },
        },
        "package_delivery": {
            "techniques": [
                ("T1566", "Phishing"),
                ("T1204.001", "User Execution: Malicious Link"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "SMS filtering: flag messages with suspicious tracking links",
                    "URL reputation: block known smishing domains",
                    "Security awareness: verify delivery through official carrier app",
                ],
                "often_fails": [
                    "Package delivery is universally expected — high success rate",
                    "Small fee requests ($3-9) seem harmless",
                    "Mobile browsers limit URL inspection",
                ],
            },
        },
        "mfa_code": {
            "techniques": [
                ("T1111", "Multi-Factor Authentication Interception"),
                ("T1566", "Phishing"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "MFA policy: legitimate codes never include clickable links",
                    "Security awareness: MFA codes are triggered by user actions only",
                    "SMS filtering: block messages impersonating corporate MFA",
                ],
                "often_fails": [
                    "Real-time proxy captures and replays MFA tokens instantly",
                    "Unexpected MFA prompts cause users to click 'secure' links",
                    "SMS-based MFA is inherently vulnerable to interception",
                ],
            },
        },
        "payment_alert": {
            "techniques": [
                ("T1566", "Phishing"),
                ("T1204.001", "User Execution: Malicious Link"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Banking app: verify transactions through official app",
                    "SMS filtering: flag messages impersonating financial institutions",
                    "Security awareness: banks never request action via SMS links",
                ],
                "often_fails": [
                    "Financial fear triggers immediate action without verification",
                    "Spoofed sender IDs match legitimate bank short codes",
                    "Urgency of potential fraud overrides security training",
                ],
            },
        },
    },

    "quishing": {
        "wifi_portal": {
            "techniques": [
                ("T1557", "Adversary-in-the-Middle"),
                ("T1556", "Modify Authentication Process"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "Network security: official Wi-Fi uses 802.1X, not web portals",
                    "Physical security: unauthorized signage should be reported",
                    "IT awareness: employees know official Wi-Fi process",
                ],
                "often_fails": [
                    "Visitors and new hires don't know the legitimate Wi-Fi process",
                    "QR codes look official when professionally printed",
                    "Captive portals are expected for guest Wi-Fi",
                ],
            },
        },
        "parking_payment": {
            "techniques": [
                ("T1566", "Phishing"),
                ("T1056.003", "Input Capture: Web Portal Capture"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "Physical security: detect tampered QR codes on payment kiosks",
                    "Payment policy: official parking uses known payment apps",
                    "URL inspection: verify domain before entering payment info",
                ],
                "often_fails": [
                    "Stickers over legitimate QR codes are hard to distinguish",
                    "Users in a hurry don't verify payment page authenticity",
                    "Physical QR attacks leave no digital trail until scanned",
                ],
            },
        },
        "document_access": {
            "techniques": [
                ("T1566.001", "Phishing: Spearphishing Attachment"),
                ("T1078", "Valid Accounts"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Physical security: unauthorized documents on desks reported",
                    "SSO monitoring: login attempts from unusual devices",
                    "Security awareness: verify sharing through official channels",
                ],
                "often_fails": [
                    "Physical documents bypass all email/network security controls",
                    "Confidential marking increases urgency and reduces skepticism",
                    "QR codes provide no URL preview before scanning",
                ],
            },
        },
        "employee_verify": {
            "techniques": [
                ("T1566", "Phishing"),
                ("T1078", "Valid Accounts"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "IT comms: official notices come through verified channels only",
                    "Physical security: unauthorized notices near badge readers reported",
                    "Badge system: verification is done through HR, not QR codes",
                ],
                "often_fails": [
                    "Authority of 'IT Security' and suspension threats create compliance",
                    "Employees near badge readers are primed to think about access",
                    "Physical notices in official format bypass digital awareness",
                ],
            },
        },
    },

    "vishing_script": {
        "it_support_call": {
            "techniques": [
                ("T1566.004", "Phishing: Spearphishing Voice"),
                ("T1204.001", "User Execution: Malicious Link"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "IT helpdesk: verify caller via internal directory callback",
                    "Caller ID verification: confirm calls from internal PBX",
                    "Security awareness: IT never asks to disable endpoint protection",
                    "Remote access policy: sessions must be user-initiated",
                ],
                "often_fails": [
                    "Caller ID spoofing makes calls appear from internal IT",
                    "Real ticket numbers and manager names build instant trust",
                    "Targets feel pressure to resolve 'security issues' quickly",
                    "IT support calls are common and don't raise suspicion",
                ],
            },
        },
        "vendor_support_call": {
            "techniques": [
                ("T1566.004", "Phishing: Spearphishing Voice"),
                ("T1199", "Trusted Relationship"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Vendor management: verify contacts through procurement records",
                    "Patch management: all updates go through IT change management",
                    "CVE verification: cross-reference with official databases",
                    "Security policy: never grant remote access on inbound calls",
                ],
                "often_fails": [
                    "Real CVE references and technical accuracy build credibility",
                    "Vulnerability fear creates urgency to act immediately",
                    "Vendor support calls are expected and unsuspicious",
                    "Pre-disclosure urgency bypasses change management",
                ],
            },
        },
        "executive_impersonation_call": {
            "techniques": [
                ("T1566.004", "Phishing: Spearphishing Voice"),
                ("T1534", "Internal Spearphishing"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Out-of-band verification: confirm via secondary channel",
                    "Payment controls: dual-auth for all financial transactions",
                    "Communication policy: no bypassing approval workflows",
                    "Voice verification: callback to known executive number",
                ],
                "often_fails": [
                    "AI voice cloning replicates executive speech patterns",
                    "Authority pressure prevents subordinates from questioning",
                    "Confidentiality framing discourages seeking verification",
                    "Real-time calls don't allow time for analysis",
                ],
            },
        },
        "password_reset_escalation": {
            "techniques": [
                ("T1566.004", "Phishing: Spearphishing Voice"),
                ("T1078.004", "Valid Accounts: Cloud Accounts"),
            ],
            "tactic": "Privilege Escalation",
            "detection": {
                "should_detect": [
                    "IAM policy: access reviews only through official IAM portal",
                    "Callback verification: verify IAM team via internal directory",
                    "PAM: all privilege changes require ticket approval",
                    "Security awareness: IAM never asks for credentials by phone",
                ],
                "often_fails": [
                    "Routine 'quarterly review' framing doesn't trigger alarm",
                    "Targets with admin access feel responsible for compliance",
                    "Fake IAM portal mimics real SSO login page",
                    "MFA fatigue attacks exploit push approval habits",
                ],
            },
        },
        "service_account_audit": {
            "techniques": [
                ("T1566.004", "Phishing: Spearphishing Voice"),
                ("T1078.001", "Valid Accounts: Default Accounts"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "Audit procedures: verify auditors through compliance dept",
                    "Credential policy: service account creds never shared verbally",
                    "Access management: audit requests require formal authorization",
                    "Secret management: credentials in vault, not shared by phone",
                ],
                "often_fails": [
                    "Compliance pressure and audit deadlines create urgency",
                    "SOC2/ISO 27001 references provide authoritative framing",
                    "Service account owners fear non-compliance consequences",
                    "Legitimate audits do require credential verification",
                ],
            },
        },
        "kerberoast_audit": {
            "techniques": [
                ("T1558.003", "Steal or Forge Kerberos Tickets: Kerberoasting"),
                ("T1078.002", "Valid Accounts: Domain Accounts"),
            ],
            "tactic": "Credential Access",
            "detection": {
                "should_detect": [
                    "Identity team: audit requests only through official ticketing system",
                    "Callback verification: verify caller via internal directory",
                    "Secret management: service account credentials never shared verbally",
                    "AD monitoring: detect unusual SPN queries or TGS requests",
                ],
                "often_fails": [
                    "Kerberos audit framing is plausible for security-conscious orgs",
                    "Service account owners feel responsible for compliance",
                    "Fake audit portal harvests credentials through familiar SSO UI",
                    "Technical jargon (SPN, encryption types) builds credibility",
                ],
            },
        },
        "endpoint_override": {
            "techniques": [
                ("T1562.001", "Impair Defenses: Disable or Modify Tools"),
                ("T1204.002", "User Execution: Malicious File"),
            ],
            "tactic": "Defense Evasion",
            "detection": {
                "should_detect": [
                    "EDR: alert on endpoint protection being disabled",
                    "SOC: monitor for defense tool state changes across endpoints",
                    "IT policy: endpoint protection cannot be disabled by end users",
                    "Change management: patches deployed through official channels only",
                ],
                "often_fails": [
                    "Zero-day CVE urgency overrides normal caution",
                    "Users with local admin can disable endpoint protection",
                    "15-minute window framing makes it seem low-risk",
                    "Staying on the phone builds trust and prevents verification",
                ],
            },
        },
        "lolbin_diagnostic": {
            "techniques": [
                ("T1218", "System Binary Proxy Execution"),
                ("T1105", "Ingress Tool Transfer"),
            ],
            "tactic": "Defense Evasion",
            "detection": {
                "should_detect": [
                    "EDR: detect certutil downloading files from external URLs",
                    "Application control: monitor LOLBin usage with network connections",
                    "Network monitoring: detect downloads from uncategorized domains",
                    "Script block logging: capture command-line arguments",
                ],
                "often_fails": [
                    "certutil is a legitimate Windows tool — hard to block outright",
                    "Certificate troubleshooting is a plausible IT scenario",
                    "Commands appear as standard system administration",
                    "Users trust step-by-step instructions from perceived IT staff",
                ],
            },
        },
    },

    "physical_pretext": {
        "hvac_technician": {
            "techniques": [
                ("T1200", "Hardware Additions"),
                ("T1091", "Replication Through Removable Media"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Visitor management: verify work orders with building management",
                    "Physical security: escort all third-party technicians",
                    "Network monitoring: detect new devices on segments",
                    "Badge system: temporary badges with limited access scope",
                ],
                "often_fails": [
                    "HVAC legitimately requires server room access",
                    "Building management and IT security are separate teams",
                    "After-hours maintenance reduces witnesses",
                    "Tool bags conceal rogue devices",
                ],
            },
        },
        "fire_inspector": {
            "techniques": [
                ("T1200", "Hardware Additions"),
                ("T1592", "Gather Victim Host Information"),
            ],
            "tactic": "Discovery",
            "detection": {
                "should_detect": [
                    "Compliance: verify inspections with fire department",
                    "Physical security: validate inspector credentials",
                    "Escort policy: inspectors accompanied at all times",
                    "Camera monitoring: review inspector activity footage",
                ],
                "often_fails": [
                    "Fire code authority creates strong compliance pressure",
                    "All-area access is expected for fire inspections",
                    "Camera for 'documentation' covers photographing sensitive areas",
                    "Safety gear and clipboard make questioning feel rude",
                ],
            },
        },
        "delivery_driver": {
            "techniques": [
                ("T1200", "Hardware Additions"),
                ("T1091", "Replication Through Removable Media"),
            ],
            "tactic": "Initial Access",
            "detection": {
                "should_detect": [
                    "Reception policy: all deliveries processed at front desk",
                    "Physical security: delivery personnel never past lobby",
                    "USB policy: unknown devices reported to security",
                    "Mail room: verify packages against expected deliveries",
                ],
                "often_fails": [
                    "Delivery personnel are common and unsuspicious",
                    "Branded packaging provides instant legitimacy",
                    "'Personal delivery' bypasses front desk",
                    "USB devices in common areas plugged in out of curiosity",
                ],
            },
        },
        "telecom_technician": {
            "techniques": [
                ("T1200", "Hardware Additions"),
                ("T1040", "Network Sniffing"),
            ],
            "tactic": "Collection",
            "detection": {
                "should_detect": [
                    "IT department: verify ISP work orders and tickets",
                    "Physical security: escort to infrastructure areas",
                    "Network monitoring: detect new devices on infra segments",
                    "Port security: 802.1X prevents unauthorized connections",
                ],
                "often_fails": [
                    "ISP technicians legitimately need network closet access",
                    "Connectivity complaints make the pretext believable",
                    "Diagnostic tools cover for plugging in implants",
                    "Many orgs lack 802.1X on infrastructure ports",
                ],
            },
        },
        "copier_technician": {
            "techniques": [
                ("T1200", "Hardware Additions"),
                ("T1557", "Adversary-in-the-Middle"),
            ],
            "tactic": "Lateral Movement",
            "detection": {
                "should_detect": [
                    "IT department: verify printer vendor service schedules",
                    "Physical security: validate vendor credentials at reception",
                    "Network monitoring: detect new devices on printer segments",
                    "Escort policy: vendor technicians accompanied between floors",
                ],
                "often_fails": [
                    "Multi-floor 'batch maintenance' provides broad building access",
                    "Printers are networked but rarely monitored for security",
                    "Connecting laptop to 'push firmware' is expected maintenance",
                    "Print rooms are unmonitored low-traffic areas",
                ],
            },
        },
        "it_asset_inventory": {
            "techniques": [
                ("T1200", "Hardware Additions"),
                ("T1592", "Gather Victim Host Information"),
            ],
            "tactic": "Discovery",
            "detection": {
                "should_detect": [
                    "IT management: verify inventory schedule with IT leadership",
                    "Badge system: asset inventory requires pre-authorized badge",
                    "Physical security: monitor and log all area access",
                    "Endpoint security: detect unauthorized USB connections",
                ],
                "often_fails": [
                    "Desk-by-desk access is legitimately required for inventory",
                    "Prolonged time at each workstation doesn't raise suspicion",
                    "'Photographing asset tags' covers capturing screen contents",
                    "USB barcode scanners cover connecting other USB devices",
                ],
            },
        },
    },

    "recon": {
        "osint_full": {
            "techniques": [
                ("T1589", "Gather Victim Identity Information"),
                ("T1590", "Gather Victim Network Information"),
                ("T1591", "Gather Victim Org Information"),
                ("T1593", "Search Open Websites/Domains"),
            ],
            "tactic": "Reconnaissance",
            "detection": {
                "should_detect": [
                    "Threat intel: monitor for company name mentions in OSINT tools",
                    "Web analytics: detect systematic crawling of careers/about pages",
                    "DNS monitoring: detect zone transfer attempts and enumeration",
                    "LinkedIn: monitor for suspicious connection patterns",
                ],
                "often_fails": [
                    "Passive OSINT generates zero network traffic to the target",
                    "Public information is freely available and cannot be restricted",
                    "Crawling patterns blend with legitimate search engine traffic",
                    "LinkedIn profiling looks identical to recruiting activity",
                ],
            },
        },
        "tech_profiling": {
            "techniques": [
                ("T1592", "Gather Victim Host Information"),
                ("T1590", "Gather Victim Network Information"),
                ("T1595.002", "Active Scanning: Vulnerability Scanning"),
            ],
            "tactic": "Reconnaissance",
            "detection": {
                "should_detect": [
                    "IDS/IPS: detect port scanning and service enumeration",
                    "WAF: flag automated fingerprinting attempts",
                    "SIEM: correlate scanning activity from single source IP",
                    "Threat intel: monitor Shodan/Censys queries targeting org assets",
                ],
                "often_fails": [
                    "Slow scans spread over days evade rate-based detection",
                    "Passive fingerprinting (HTTP headers, DNS) generates no alerts",
                    "Scanner traffic blends with legitimate vulnerability researchers",
                    "Cloud assets are scanned by thousands of bots daily",
                ],
            },
        },
        "personnel_mapping": {
            "techniques": [
                ("T1589.002", "Gather Victim Identity Information: Email Addresses"),
                ("T1591.004", "Gather Victim Org Information: Identify Roles"),
                ("T1593.001", "Search Open Websites/Domains: Social Media"),
            ],
            "tactic": "Reconnaissance",
            "detection": {
                "should_detect": [
                    "LinkedIn: alert on bulk profile viewing from single account",
                    "Email security: detect SMTP VRFY probes",
                    "HR: monitor for suspicious recruiter activity targeting key staff",
                    "Social media monitoring: detect fake profiles connecting to employees",
                ],
                "often_fails": [
                    "LinkedIn viewing looks identical to legitimate recruiting",
                    "Employee info on public profiles cannot be restricted by org",
                    "Social media OSINT requires no interaction with target systems",
                    "Fake profiles with real-looking histories evade detection",
                ],
            },
        },
    },

    "c2": {
        "https_beacon": {
            "techniques": [
                ("T1071.001", "Application Layer Protocol: Web Protocols"),
                ("T1573.002", "Encrypted Channel: Asymmetric Cryptography"),
                ("T1571", "Non-Standard Port"),
            ],
            "tactic": "Command and Control",
            "detection": {
                "should_detect": [
                    "Network monitoring: detect beaconing patterns (fixed intervals)",
                    "TLS inspection: flag certificates from newly registered domains",
                    "Proxy logs: identify unusual user-agent or URI patterns",
                    "JA3/JA3S: fingerprint non-browser TLS implementations",
                ],
                "often_fails": [
                    "HTTPS encryption prevents payload inspection without TLS MITM",
                    "Jitter and sleep variation defeat statistical beacon detection",
                    "Categorized domains bypass web proxy allow-lists",
                    "Malleable C2 profiles mimic legitimate application traffic",
                ],
            },
        },
        "dns_tunnel": {
            "techniques": [
                ("T1071.004", "Application Layer Protocol: DNS"),
                ("T1568", "Dynamic Resolution"),
            ],
            "tactic": "Command and Control",
            "detection": {
                "should_detect": [
                    "DNS monitoring: detect high query volume to single domain",
                    "DNS inspection: flag unusually long subdomain labels",
                    "SIEM: correlate DNS patterns with endpoint activity",
                    "DNS sinkholing: redirect known C2 domains",
                ],
                "often_fails": [
                    "DNS is rarely inspected beyond basic logging",
                    "Split-DNS environments may miss internal-to-external tunneling",
                    "Low-and-slow queries blend with normal DNS resolution",
                    "Many orgs allow unrestricted outbound DNS",
                ],
            },
        },
        "domain_fronting": {
            "techniques": [
                ("T1090.004", "Proxy: Domain Fronting"),
                ("T1071.001", "Application Layer Protocol: Web Protocols"),
            ],
            "tactic": "Command and Control",
            "detection": {
                "should_detect": [
                    "TLS inspection: detect SNI/Host header mismatch",
                    "Proxy logs: flag unusual CDN usage patterns",
                    "Network monitoring: detect POST requests to CDN endpoints",
                    "Threat intel: track known domain fronting CDN distributions",
                ],
                "often_fails": [
                    "CDN traffic is trusted and high-volume — hard to inspect",
                    "TLS inspection requires MITM which many orgs avoid",
                    "Blocking CDN providers would break legitimate services",
                    "SNI/Host mismatch only visible with full TLS termination",
                ],
            },
        },
        "exfil_channel": {
            "techniques": [
                ("T1048.002", "Exfiltration Over Alternative Protocol: Asymmetric Encrypted Non-C2"),
                ("T1567.002", "Exfiltration to Cloud Storage"),
                ("T1030", "Data Transfer Size Limits"),
            ],
            "tactic": "Exfiltration",
            "detection": {
                "should_detect": [
                    "DLP: detect unusual data volumes to cloud storage",
                    "CASB: monitor sanctioned vs unsanctioned cloud app usage",
                    "Network monitoring: flag large outbound transfers during off-hours",
                    "Endpoint: detect compression/encryption before upload",
                ],
                "often_fails": [
                    "Legitimate cloud storage usage makes detection by volume difficult",
                    "Encrypted data prevents content-based DLP inspection",
                    "Small chunks over days blend with normal business uploads",
                    "Personal cloud accounts may not be monitored by CASB",
                ],
            },
        },
    },
}


# ═══════════════════════════════════════════════════════════════
#  PUBLIC API
# ═══════════════════════════════════════════════════════════════

def get_mitre_data(scenario_type, template_id):
    """Get MITRE ATT&CK data for a specific scenario template.

    Returns dict with 'techniques', 'tactic', and 'detection' keys.
    Falls back to generic data if template is not mapped.
    """
    type_map = SCENARIO_TECHNIQUES.get(scenario_type, {})
    data = type_map.get(template_id)
    if data:
        return data
    return {
        "techniques": [("T1566", "Phishing")],
        "tactic": "Initial Access",
        "detection": {
            "should_detect": [
                "Email and network security controls",
                "Security awareness training",
            ],
            "often_fails": [
                "Novel techniques bypass signature-based detection",
                "Human factor remains the weakest link",
            ],
        },
    }


def get_phase_scenario_type(phase):
    """Get the recommended scenario CLI type for an ATT&CK phase."""
    return PHASE_TO_SCENARIO.get(phase, "phishing")
