"""
Pretext templates, personas, and scenario data.
All templates use {placeholder} syntax for dynamic generation.
"""

# ═══════════════════════════════════════════════════════════════
#  TARGET INDUSTRIES
# ═══════════════════════════════════════════════════════════════

INDUSTRIES = {
    "tech": {
        "name": "Technology",
        "departments": ["Engineering", "DevOps", "IT", "Security"],
        "software": ["Jira", "GitHub", "Slack", "AWS Console", "Okta"],
        "jargon": ["sprint planning", "CI/CD pipeline", "SSO integration", "incident response"],
        "pain_points": ["production outages", "credential rotation", "on-call fatigue"],
    },

    "finance": {
        "name": "Financial Services",
        "departments": ["Accounting", "Risk Management", "Compliance", "IT", "Trading Floor", "Internal Audit"],
        "software": ["Bloomberg Terminal", "Salesforce", "SAP", "Oracle Financials", "ServiceNow", "Workday", "NetSuite", "Refinitiv Eikon"],
        "jargon": ["fiscal quarter", "regulatory compliance", "audit trail", "risk assessment", "KYC review", "AML compliance", "SOX audit"],
        "pain_points": ["regulatory deadlines", "fraud prevention", "data breaches"],
    },

    "healthcare": {
        "name": "Healthcare",
        "departments": ["Medical Records", "Billing", "IT", "Compliance"],
        "software": ["Epic", "Cerner", "Meditech", "Kronos", "McKesson"],
        "jargon": ["HIPAA compliance", "patient portal", "EHR system", "clinical workflow"],
        "pain_points": ["patient data security", "system downtime", "regulatory audits"],
    },

    "government": {
        "name": "Government",
        "departments": ["Security", "IT", "Compliance", "Operations"],
        "software": ["Splunk", "Tenable", "Archer", "Salesforce Gov Cloud", "Microsoft 365 GCC", "ServiceNow"],
        "jargon": ["classified information", "security clearance", "FISMA compliance", "NIST standards", "POAM remediation", "authority to operate"],
        "pain_points": ["data classification", "access control issues", "compliance audits"],
    },

    "education": {
        "name": "Education",
        "departments": ["IT", "Admissions", "Financial Aid", "Student Services"],
        "software": ["Blackboard", "Canvas", "Banner", "Zoom", "Google Workspace"],
        "jargon": ["course management", "student information system", "virtual learning environment", "admissions cycle"],
        "pain_points": ["phishing attacks on students", "credential theft", "system outages during enrollment"],
    },

    "manufacturing": {
        "name": "Manufacturing",
        "departments": ["Operations", "IT", "Supply Chain", "Quality Control"],
        "software": ["Siemens S7", "Rockwell", "SAP", "Oracle SCM", "Wonderware"],
        "jargon": ["production line", "supply chain disruption", "quality assurance", "inventory turnover", "SCADA system", "PLC firmware"],
        "pain_points": ["production downtime", "supply chain attacks", "intellectual property theft"],
    },

    "retail": {
        "name": "Retail",
        "departments": ["Sales", "IT", "Customer Service", "Logistics"],
        "software": ["Shopify", "Square", "Salesforce Commerce", "Oracle Retail", "Magento", "Lightspeed"],
        "jargon": ["point of sale", "customer relationship management", "supply chain logistics", "inventory turnover", "PCI DSS compliance"],
        "pain_points": ["payment card breaches", "credential theft from employees", "supply chain disruptions"],
    },
}

# ═══════════════════════════════════════════════════════════════
#  ATTACKER PERSONAS
# ═══════════════════════════════════════════════════════════════

PERSONAS = {
    "it_support": {
        "name": "IT Support Technician",
        "titles": ["IT Support Specialist", "Help Desk Analyst", "Systems Administrator", "Desktop Support Engineer"],
        "pretexts": [
            "your password expires in 2 hours - reset now through this portal to avoid account lockout",
            "deploying a critical {software} security patch - need you to run the attached installer or grant remote access",
            "your account was flagged for suspicious login activity - verify your identity to prevent suspension",
            "scheduled MFA enrollment for your department - complete registration before end of day or access will be restricted",
            "VPN configuration update required - download the new profile from this link before remote access is revoked",
            "your workstation failed our latest security scan - need remote access to remediate before the next audit cycle",
        ],
    },

    "vendor": {
        "name": "Third-Party Vendor",
        "titles": ["Technical Account Manager", "Customer Success Engineer", "Integration Specialist"],
        "pretexts": [
            "your {software} license expires in 48 hours - confirm renewal immediately",
            "critical vulnerability discovered in {software} - need to backup and reset your workspace",
            "your {software} integration is causing system conflicts - need you to transfer your work so we can resolve",
            "urgent security patch for {software} - requires your authorization to deploy",
            "your {software} environment failed our compliance scan - need remote access to remediate",
        ],
    },

    "executive": {
        "name": "Executive / C-Suite Impersonation",
        "titles": ["CEO", "CFO", "CTO", "COO", "VP of Operations"],
        "pretexts": [
            "send me the quarterly security report before my meeting - need it within the hour",
            "handle the attached transfer instructions quietly - we can't afford an information leak",
            "I've already spoken with {name} about this - I need you to process it immediately",
            "confidential acquisition due diligence - need financials before close of business",
            "vendor payment authorization - wire before 3PM today, details attached",
        ],
    },

    "auditor": {
        "name": "External Auditor",
        "titles": ["Audit Manager", "Compliance Auditor", "Risk Assessment Specialist", "Security Assessor"],
        "pretexts": [
            "conducting a GDPR compliance audit - need stored user data records and sample PII logs by midnight or the company faces legal proceedings for non-compliance",
            "sent by ATOS to review access logs and verify privileged account activity - failure to provide by tomorrow morning will be flagged as an audit exception and escalated to the board",
            "conducting a payroll compliance audit - need all relevant spreadsheets from this quarter by tomorrow afternoon or this triggers an on-site inspection by your tax authority",
            "annual security audit - need current firewall configurations and admin access lists within 24 hours",
            "third-party risk assessment follow-up - your vendor compliance documentation is overdue and blocking certification renewal",
        ],
    },

    "new_employee": {
        "name": "New Employee",
        "titles": ["New Hire", "Recent Transfer", "Contractor (First Day)", "Intern"],
        "pretexts": [
            "new hire from the Network branch - need you to run the attached speed test to evaluate on-site performance",
            "my badge won't let me into the server room - my manager {name} told me to change the RJ45 cables after hours",
            "my account is under activation - can you forward the network infrastructure layout so I can start working off hours",
            "my manager {name} said to ask you for temporary access - IT hasn't set up my account yet",
            "first day and I can't access {software} - need temporary credentials for the onboarding training at 2PM",
        ],
    },

    "physical": {
        "name": "Physical Intruder",
        "titles": ["HVAC Technician", "Delivery Driver", "Maintenance Worker", "Telecom Technician", "Fire Safety Inspector"],
        "pretexts": [
            "here to take footage of the assembly room to prepare Q4 renovations",
            "delivering a Smart Printer for HR - manager requested direct delivery to the office",
            "maintenance on core power supplies - faulty cables reported by the site administrator who requested me on-site",
            "scheduled network cable installation per work order #{wo_number} - building management approved access",
            "fire suppression system annual certification - need access to all floors including server room",
        ],
    },
}

# ═══════════════════════════════════════════════════════════════
#  URGENCY TRIGGERS
# ═══════════════════════════════════════════════════════════════

URGENCY_TRIGGERS = {
    "low": [
        "When you get a chance",
        "Please review at your convenience",
        "Feel free to take a look when you have time",
        "No rush, but please review when convenient",
    ],
    "medium": [
        "By end of day today",
        "Please complete by tomorrow",
        "This needs to be addressed before the weekend",
        "Please prioritize this task",
    ],
    "high": [
        "This needs to happen in the next 30 minutes",
        "This requires immediate attention",
        "Please address this within the hour",
        "Important task - please act now",
    ],
    "critical": [
        "A breach is currently occurring and your account has not been compromised yet",
        "Per emergency board resolution - all managers must re-verify credentials before midnight",
        "To comply with SEC inquiry, review and submit this quarter's reports immediately",
        "Review and send the contracts signed during Q2 first week - a flaw has been detected and clients are threatening legal action",
    ],
}

# ═══════════════════════════════════════════════════════════════
#  SEASONAL HOOKS
# ═══════════════════════════════════════════════════════════════

SEASONAL_HOOKS = {
    "q1": [
        "Annual security training enrollment",
        "Tax season document submission - W2/1099 verification",
        "Annual password reset policy enforcement",
        "Q1 financial reporting deadline approaching",
    ],
    "q2": [
        "Mid-year compliance review",
        "Summer intern onboarding batch - IT access requests",
        "Quarterly software license renewal notices",
        "Password reset policy follow-up for accounts created in Q1",
    ],
    "q3": [
        "Pre-audit preparation",
        "Hurricane/disaster recovery drill",
        "Vendor contract renewal discussions for expiring agreements",
        "Q3 performance review cycle - manager approvals",
    ],
    "q4": [
        "Holiday schedule - urgent before office closure",
        "Year-end compliance deadline - final submissions",
        "End-of-year financial reporting",
        "Holiday security awareness training",
    ],
}

# ═══════════════════════════════════════════════════════════════
#  PHISHING EMAIL TEMPLATES
# ═══════════════════════════════════════════════════════════════

PHISHING_TEMPLATES = [
    {
        "id": "credential_harvest",
        "name": "Credential Harvesting",
        "subject_lines": [
            "Action Required: Verify Your {software} Account",
            "Security Alert: Unusual Activity Detected on Your {software} Account",
            "Immediate Action Required: Confirm Your {software} Account Details",
            "{software} Account Suspension Warning - Verify Now",
        ],
        "body": """Hi {first_name},

{urgency_opening}

Please verify your identity by clicking the link below:

{phishing_link}

If you do not complete this within {deadline}, your access to {software} will be temporarily suspended.

{signature}""",
    },
    {
        "id": "malicious_attachment",
        "name": "Malicious Attachment",
        "subject_lines": [
            "Important: {document_name} - Review Required",
            "{department} Update: Please Review Attached Document",
            "Confidential: {document_name} - For Your Eyes Only",
            "Action Required: Review and Sign {document_name}",
        ],
        "body": """Hi {first_name},

{urgency_opening}

Please find the attached {document_type} that requires your immediate review. This document has been approved by {department} leadership and is being distributed to all relevant personnel.

📎 {attachment_note}

Please review, sign, and return by {deadline}. If you have trouble opening the file, please enable macros when prompted — this is required by our document security policy.

{signature}""",
    },
    {
        "id": "bec_wire",
        "name": "Business Email Compromise (Wire Fraud)",
        "subject_lines": [
            "Confidential - Urgent Payment Required",
            "Re: Vendor Payment - Updated Banking Details",
            "Quick Favor - Need This Handled Discreetly",
            "{executive_name} - Urgent Wire Transfer Request",
        ],
        "body": """Hi {first_name},

I need you to handle something urgently and discreetly. We are finalizing a confidential deal and I need a wire transfer processed before close of business.

Please send the following:

    Amount: ${amount}
    Bank: {bank_name}
    Account: {account_placeholder}
    Reference: {reference}

This needs to be completed by {deadline}. Do not discuss this with anyone else until the deal is finalized — we can't afford an information leak.

I've already cleared this with legal. Confirm once done.

{executive_signature}""",
    },
    {
        "id": "callback_phishing",
        "name": "Callback Phishing (Vishing Setup)",
        "subject_lines": [
            "Subscription Renewal - Charge of ${amount} Processed",
            "Order Confirmation #{invoice_number}",
            "Your Account Has Been Charged ${amount}",
            "Receipt for Recent Purchase - {software} Enterprise License",
        ],
        "body": """Dear {first_name},

This email confirms your recent purchase:

    Transaction ID: {transaction_id}
    Date: {date}
    Description: {software} Enterprise License - Annual Renewal
    Amount: ${amount}

If you authorized this transaction, no action is needed.

If you DID NOT authorize this charge, contact our support team immediately to request a full refund:

    Phone: {callback_number}
    Available 24/7 - Reference your Transaction ID when calling

Please note: refund requests must be submitted within 48 hours of the charge.

{generic_signature}""",
    },
]

# ═══════════════════════════════════════════════════════════════
#  VISHING SCRIPTS
# ═══════════════════════════════════════════════════════════════

VISHING_SCRIPTS = [
    {
        "id": "it_support_call",
        "name": "IT Support Call",
        "opening": """[CALLER]: Hi, this is {caller_name} from {company} IT Support.
I'm reaching out because we've detected {issue} on your workstation.
Is this {target_name} from {department}?""",
        "escalation": """[CALLER]: I completely understand your concern - we've been getting a lot of calls about this today.
Let me pull up your ticket... Yes, I can see ticket #{ticket_number} was created at {time} today.
{manager_name} from your department approved this maintenance window.
I just need to verify a few things on your end to get this resolved quickly.
Would you prefer I call back on your desk phone, or can we handle this now?""",
        "objective": """GOAL: Get target to:
  - Confirm their username and employee ID
  - Navigate to a URL for "remote support session"
  - Read back a verification code (intercepted MFA token)
  - Disable endpoint protection temporarily for "patching"
  - Run a diagnostic tool (payload) sent via email""",
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't ask for passwords directly - ask them to "reset through our portal"
  ✗ Don't rush - real IT support is patient and methodical
  ✗ Don't get defensive if questioned - offer to let them verify via callback
  ✗ Don't use technical jargon the target wouldn't understand
  ✓ Use the target's real department and manager names (from OSINT)
  ✓ Reference real software they use
  ✓ Have a spoofed caller ID matching company IT department
  ✓ Offer a callback number that routes to your infrastructure""",
    },
    {
        "id": "vendor_support_call",
        "name": "Vendor Support Call",
        "opening": """[CALLER]: Good {time_of_day}, this is {caller_name} from {vendor_name} support.
I'm calling about a critical security advisory affecting your {software} deployment.
Can I speak with whoever manages your {software} environment?""",
        "escalation": """[CALLER]: I understand you need to verify this. Absolutely - security is why I'm calling.
We've identified a vulnerability - CVE-{cve_year}-{cve_id} - that affects your version.
I've been assigned to help priority customers patch before the public disclosure on {disclosure_date}.
I can send you the official advisory email right now if you'd like to verify.
In the meantime, can you confirm what version you're currently running so I can check if you're affected?""",
        "objective": """GOAL: Get target to:
  - Confirm software version and deployment details
  - Grant remote access for "emergency patching"
  - Run a "verification tool" sent via email (payload)
  - Provide admin credentials for "patch deployment"
  - Disable security controls that would block the "update" """,
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't use fake CVE numbers - research real recent ones for the software
  ✗ Don't pressure for immediate admin access - build up to it
  ✗ Don't claim to know their setup if you haven't done OSINT
  ✓ Reference their actual software version (from job postings, Shodan, Wappalyzer)
  ✓ Offer to send a verification email (from your spoofed domain)
  ✓ Be prepared to explain the vulnerability technically
  ✓ Know the vendor's real support processes so you can mimic them""",
    },
    {
        "id": "executive_impersonation_call",
        "name": "Executive Impersonation Call",
        "opening": """[CALLER]: {target_name}? This is {executive_name}.
I'm between meetings right now but I need you to handle something for me quickly.
Can you talk for a minute?""",
        "escalation": """[CALLER]: Listen, I can't go into all the details right now because
this is confidential. We're closing a deal and I need {action} processed
before {deadline}. I've already spoken with {department_head} about it.
I'm going to send you the details by email right after this call.
Can you take care of this as soon as you get it? I'm counting on you.""",
        "objective": """GOAL: Get target to:
  - Process a wire transfer or payment
  - Share sensitive financial documents
  - Bypass normal approval workflows based on perceived authority
  - Forward credentials or grant system access
  - Open an attachment sent in follow-up email (payload delivery)""",
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't attempt without studying the executive's speech patterns (YouTube, podcasts, earnings calls)
  ✗ Don't ask for things outside the target's actual authority
  ✗ Don't be aggressive - real executives delegate, they don't threaten subordinates
  ✗ Don't call from an unknown number - spoof the executive's real number or office line
  ✓ Research the executive's schedule and reference real events
  ✓ Reference real ongoing projects (from LinkedIn, press releases, SEC filings)
  ✓ Keep it short - executives don't have long phone conversations
  ✓ Create follow-up via email for payload delivery after establishing trust by phone""",
    },
]

# ═══════════════════════════════════════════════════════════════
#  PHYSICAL ACCESS PRETEXTS
# ═══════════════════════════════════════════════════════════════

PHYSICAL_PRETEXTS = [
    {
        "id": "hvac_technician",
        "name": "HVAC Technician",
        "appearance": "Branded polo or uniform shirt, tool belt, clipboard with work orders, safety glasses, steel-toe boots",
        "props": [
            "Printed work order with target company address and building management logo",
            "Multimeter and basic HVAC tools",
            "Flashlight",
            "Generic HVAC company badge with photo",
            "High-vis vest",
        ],
        "script": """I'm here for the scheduled HVAC inspection on floor {floor}.
Building management should have sent a notice last week - I can show you the work order.
I need access to the server room to check the cooling units.
We've been getting temperature alerts from this building and the last thing
anyone wants is equipment overheating over the weekend.""",
        "target_areas": ["Server rooms", "Network closets", "Mechanical rooms", "Rooftop access", "Basement infrastructure"],
        "objectives": [
            "Plant a rogue network device (LAN Turtle, Raspberry Pi, WiFi Pineapple)",
            "Photograph network equipment labels and IP configurations",
            "Access unlocked workstations in server room",
            "Map physical security controls (cameras, badge readers, locks)",
            "Tailgate through secured doors while carrying equipment",
        ],
    },
    {
        "id": "fire_inspector",
        "name": "Fire Safety Inspector",
        "appearance": "Business casual with high-visibility vest, clipboard, camera, official-looking laminated badge",
        "props": [
            "Fire inspection checklist (printed, official-looking)",
            "Camera for 'documentation of extinguisher placements'",
            "Badge with generic fire safety company name and photo",
            "Measuring tape",
            "Flashlight",
        ],
        "script": """Hi, I'm {name} from {fire_safety_company}. We're conducting the annual
fire suppression system inspection for this building. I'll need access to
all floors including restricted areas to verify extinguisher placements
and inspect the sprinkler system. This is required by fire code and
building management has it on the schedule. Who do I check in with?""",
        "target_areas": ["All floors including restricted areas", "Server rooms (fire suppression systems)", "Stairwells and emergency exits", "Electrical rooms", "Executive floors"],
        "objectives": [
            "Gain unrestricted building access with legitimate-sounding authority",
            "Photograph office layouts, security camera positions, and badge reader locations",
            "Test physical security response to an unfamiliar person in restricted areas",
            "Access server rooms under fire suppression pretext",
            "Identify unlocked offices and unattended workstations",
        ],
    },
    {
        "id": "delivery_driver",
        "name": "Delivery / Courier",
        "appearance": "Casual clothing, carrying branded boxes (Amazon, FedEx, UPS), possibly with a hand truck for larger deliveries",
        "props": [
            "Branded shipping boxes (Amazon, FedEx, or similar)",
            "Clipboard with printed delivery manifest showing target's name",
            "Hand truck for large package deliveries",
            "USB drop devices concealed inside packages",
            "Printed shipping label with correct company address",
        ],
        "script": """Delivery for {target_name} in {department}. I was told to deliver
directly to their desk - it's marked fragile and confidential so I can't
just leave it at reception. I need a signature from them personally.
Can someone walk me over? I've got more deliveries to make so I'm
kind of in a rush.""",
        "target_areas": ["Reception and lobby", "Mail room", "Target's office or desk area", "Common areas and break rooms"],
        "objectives": [
            "Bypass lobby security by carrying legitimate-looking packages",
            "Access internal office areas beyond reception",
            "Drop USB devices in common areas or on desks",
            "Observe badge systems, door codes, and security procedures",
            "Deliver a package containing a rogue device to a specific person",
        ],
    },
    {
        "id": "telecom_technician",
        "name": "Telecom / Internet Technician",
        "appearance": "Branded ISP polo or jacket, tool belt, cable tester, laptop bag, hard hat if entering utility areas",
        "props": [
            "ISP-branded uniform or polo shirt",
            "Cable tester and ethernet crimping tools",
            "Laptop with network diagnostic software",
            "Printed work order referencing reported connectivity issues",
            "Badge with ISP company logo",
        ],
        "script": """Hi, I'm from {isp_name}. We received a ticket about intermittent
connectivity issues affecting this floor. I need to check the network
closet and trace the cabling back to the demarc point. It shouldn't
take more than 30 minutes. Can someone show me where the network
closet is? I also need to plug in my diagnostic tool to run some tests.""",
        "target_areas": ["Network closets and wiring panels", "Server rooms", "Demarc point / telecom room", "Under-desk cabling access"],
        "objectives": [
            "Plant a network tap or rogue device in the network closet",
            "Connect a device to a live network port for remote access",
            "Photograph network topology and cable labels",
            "Map internal network infrastructure and VLAN configurations",
            "Identify unencrypted network traffic or insecure protocols",
        ],
    },
]

# ═══════════════════════════════════════════════════════════════
#  PSYCHOLOGICAL PRINCIPLES
# ═══════════════════════════════════════════════════════════════

PSYCH_PRINCIPLES = {
    "authority": {
        "name": "Authority",
        "description": "People comply with perceived authority figures",
        "application": "Impersonate executives, IT admins, auditors, or law enforcement",
        "example": "The CISO asked me to verify all accounts in your department today.",
    },
    "urgency": {
        "name": "Urgency / Scarcity",
        "description": "Time pressure reduces critical thinking",
        "application": "Create artificial deadlines, reference active incidents or expiring access",
        "example": "Your account will be locked in 30 minutes if you don't verify.",
    },
    "social_proof": {
        "name": "Social Proof",
        "description": "People follow what others are doing",
        "application": "Reference colleagues who have already complied",
        "example": "Everyone in your department has already completed this - you're the last one.",
    },
    "reciprocity": {
        "name": "Reciprocity",
        "description": "People feel obligated to return favors",
        "application": "Help the target with something first, then make your real request",
        "example": "I just fixed your printer issue. By the way, can you badge me into the server room?",
    },
    "liking": {
        "name": "Liking / Rapport",
        "description": "People comply more with those they like",
        "application": "Build rapport through small talk and common ground before making requests",
        "example": "Oh you're into cycling too? Anyway, quick favor - can you check something for me?",
    },
    "commitment": {
        "name": "Commitment / Consistency",
        "description": "Once someone agrees to something small, they'll agree to bigger asks",
        "application": "Start with innocent questions and gradually escalate to sensitive requests",
        "example": "Can you confirm your department? Great. And your role? Perfect. Now can you verify your employee ID for our records?",
    },
}

# ═══════════════════════════════════════════════════════════════
#  FAKE DOCUMENT NAMES
# ═══════════════════════════════════════════════════════════════

FAKE_DOCUMENTS = [
    "Q4_Financial_Review_2025.xlsx",
    "Employee_Password_Policy_Update.docx",
    "Vendor_Contract_Renewal_Notice.pdf",
    "Internal_Security_Audit_Findings.pptx",
    "Confidential_Client_List.xlsx",
    "Executive_Board_Meeting_Agenda.docx",
    "IT_Support_Ticket.pdf",
    "HR_Payroll_Compliance_Audit_2025.xlsx",
    "Critical_Software_Patch_Deployment_Instructions.docx",
    "Phishing_Simulation_Report.pdf",
    "Incident_Response_Plan_Update.docx",
    "Employee_Onboarding_Checklist.xlsx",
    "Vendor_Security_Assessment.pdf",
    "Annual_Security_Training_Enrollment.docx",
    "Bonus_Structure_2025.xlsx",
    "Organizational_Chart_2025.pptx",
    "Layoff_Notices_Q1_2026.docx",
    "Personal_Performance_Review_2025.xlsx",
]