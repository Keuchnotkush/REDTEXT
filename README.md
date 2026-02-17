# 🔴 Redtext Generator

**Social Engineering Scenario Builder for Authorized Red Team Operations**
```
  ██████╗ ███████╗██████╗ ████████╗███████╗██╗  ██╗████████╗
  ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
  ██████╔╝█████╗  ██║  ██║   ██║   █████╗   ╚███╔╝    ██║
  ██╔══██╗██╔══╝  ██║  ██║   ██║   ██╔══╝   ██╔██╗    ██║
  ██║  ██║███████╗██████╔╝   ██║   ███████╗██╔╝ ██╗   ██║
  ╚═╝  ╚═╝╚══════╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝
       ██████╗ ███████╗███╗   ██╗
       ██╔════╝ ██╔════╝████╗  ██║
       ██║  ███╗█████╗  ██╔██╗ ██║
       ██║   ██║██╔══╝  ██║╚██╗██║
       ╚██████╔╝███████╗██║ ╚████║
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
  ╔══════════════════════════════════════════════════════════╗
  ◢◤ SOCIAL ENGINEERING SCENARIO BUILDER ◢◤                ║
  ║                                                          ║
  ║    ▸ Physical Pretexts   ▸ Full Attack Scenarios         ║
  ║    ▸ Phishing Emails    ▸ Vishing Scripts                ║
  ║                                                          ║
  ║  {Colors.YELLOW}  "Some data is too dangerous to record."║
  ║                            — SCP-2521                    ║
  ╚══════════════════════════════════════════════════════════╝
  v1.0.0 | @keuchnotkush | For authorized use only
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
```

> ⚠️ **This tool is designed for AUTHORIZED red team operations, security awareness training, and penetration testing ONLY. Unauthorized use of social engineering techniques is illegal and unethical. Always obtain written authorization before conducting any social engineering engagement.**

## What is Redtext?

Redtext generates realistic social engineering scenarios for red team engagements. Feed it a target industry, attacker persona, and urgency level — it outputs ready-to-use phishing emails, vishing call scripts, and physical access pretexts with dynamically generated names, companies, and details.

No external dependencies. Pure Python. Optional GoPhish integration for live campaign deployment.

## Installation
```bash
git clone https://github.com/keuchnotkush/redtext-generator.git
cd redtext-generator
```

That's it. No `pip install` required — runs on Python 3.8+ with stdlib only.

## Usage
```bash
# Generate a phishing email targeting finance with high urgency
python -m redtext_generator phishing --industry finance --urgency high

# Generate a smishing (SMS phishing) message targeting finance
python -m redtext_generator smishing --industry finance --urgency critical

# Generate a QR code phishing (quishing) scenario with ASCII QR
python -m redtext_generator quishing --industry tech --urgency high

# Generate a vishing script as a vendor impersonator
python -m redtext_generator vishing --persona vendor --company "Acme Corp"

# Generate a physical access pretext for healthcare
python -m redtext_generator physical --industry healthcare

# Generate a complete multi-phase attack scenario
python -m redtext_generator full --industry tech --urgency critical --company "Target Inc"

# List all available industries, personas, and options
python -m redtext_generator list
```

## Generation Modes

| Mode | Command | Output |
|------|---------|--------|
| 📧 Phishing | `phishing` | Email with subject, body, IoCs |
| 📱 Smishing | `smishing` | SMS message with malicious link, short code |
| 📲 Quishing | `quishing` | QR code scenario with ASCII QR, pretext, placement |
| 📞 Vishing | `vishing` | Call script with opening, escalation, objectives |
| 🏢 Physical | `physical` | Cover identity, props, script, target areas |
| ⚔️ Full | `full` | Multi-phase attack: recon → phishing → vishing → physical |
| 📋 List | `list` | All available options |

## Options

| Flag | Short | Description | Default |
|------|-------|-------------|---------|
| `--industry` | `-i` | Target industry | `tech` |
| `--urgency` | `-u` | Urgency level | `medium` |
| `--persona` | `-p` | Attacker persona | `it_support` |
| `--company` | `-c` | Target company name | `Target Corp` |
| `--template` | `-t` | Specific template ID | random |
| `--seed` | `-s` | Random seed (reproducible output) | none |
| `--export-json` | | Export as JSON file | none |
| `--export-md` | | Export as Markdown file | none |
| `--no-banner` | | Suppress ASCII banner | false |
| `--no-disclaimer` | | Suppress disclaimer | false |

## Supported Industries

| Key | Industry | Example Software |
|-----|----------|-----------------|
| `tech` | Technology | Jira, GitHub, Slack, AWS, Okta |
| `finance` | Financial Services | Bloomberg, SAP, Oracle Financials |
| `healthcare` | Healthcare | Epic, Cerner, Meditech, McKesson |
| `government` | Government | Splunk, Tenable, Archer, Salesforce Gov |
| `education` | Education | Canvas, Blackboard, Banner, Zoom |
| `manufacturing` | Manufacturing | Siemens S7, Rockwell, SAP, Wonderware |
| `retail` | Retail | Shopify, Square, Magento, Oracle Retail |

## Attacker Personas

| Key | Persona | Use Case |
|-----|---------|----------|
| `it_support` | IT Support Technician | Credential harvesting, remote access |
| `vendor` | Third-Party Vendor | Software exploitation, supply chain |
| `executive` | C-Suite Impersonation | BEC, wire fraud, authority abuse |
| `auditor` | External Auditor | Document theft, compliance pressure |
| `new_employee` | New Employee | Physical access, credential requests |
| `physical` | Physical Intruder | Building access, device planting |

## Psychological Principles

Every generated scenario leverages [Cialdini's Principles of Influence](https://en.wikipedia.org/wiki/Robert_Cialdini):

| Principle | How Redtext Uses It |
|-----------|-------------------|
| **Authority** | Executive impersonation, auditor pressure |
| **Urgency** | Artificial deadlines, active breach claims |
| **Social Proof** | "Everyone in your department already completed this" |
| **Reciprocity** | Help first, then request access |
| **Liking** | Rapport building before the ask |
| **Commitment** | Small asks escalating to sensitive requests |

## GoPhish Integration

Redtext integrates with [GoPhish](https://getgophish.com/) to push generated scenarios directly into live phishing campaigns.

### Setup
```bash
# Configure GoPhish API connection (saved to ~/.config/redtext/config.ini)
python -m redtext_generator gophish setup
```

You can also configure via environment variables (`REDTEXT_GOPHISH_URL`, `REDTEXT_GOPHISH_KEY`) or CLI flags (`--gophish-url`, `--gophish-key`).

### Commands
```bash
# List existing GoPhish templates
python -m redtext_generator gophish templates

# Generate a phishing scenario and push it as a GoPhish template
python -m redtext_generator gophish push --industry finance --urgency high

# Push with a custom template name
python -m redtext_generator gophish push --industry tech --name "Q1 Security Audit"

# Create a full campaign (requires existing template, SMTP profile, landing page, and group)
python -m redtext_generator gophish campaign \
  --template-name "Q1 Security Audit" \
  --group-name "Engineering Team" \
  --smtp-name "Relay1" \
  --page-name "O365 Login" \
  --url "https://phish.example.com"

# Create a campaign with auto-created target group from CSV
python -m redtext_generator gophish campaign \
  --template-name "Q1 Security Audit" \
  --group-name "New Targets" \
  --targets-csv targets.csv \
  --smtp-name "Relay1" \
  --page-name "O365 Login" \
  --url "https://phish.example.com" \
  --launch-date "2025-03-01T09:00:00+00:00"

# Check campaign results
python -m redtext_generator gophish status 42
```

### Target CSV Format
```csv
email,first_name,last_name,position
alice@corp.com,Alice,Smith,Engineer
bob@corp.com,Bob,Jones,Manager
```

### SSL Verification

GoPhish often runs on self-signed certificates. Use `--no-verify-ssl` to skip verification:
```bash
python -m redtext_generator gophish templates --no-verify-ssl
```

Or set `verify_ssl = false` in your config file during `gophish setup`.

## Export
```bash
# Export as JSON
python -m redtext_generator phishing -i finance -u high --export-json scenario.json

# Export as Markdown
python -m redtext_generator full -i tech -u critical --export-md report.md

# Both
python -m redtext_generator full --export-json out.json --export-md out.md
```

## Project Structure
```
redtext-generator/
├── redtext_generator/
│   ├── __init__.py          # Package metadata
│   ├── __main__.py          # CLI entry point (argparse)
│   ├── templates.py         # Industries, personas, email/vishing/physical templates
│   ├── generator.py         # Core engine — assembles scenarios from templates
│   ├── formatters.py        # Terminal display (ANSI colors) + JSON/Markdown export
│   ├── qrencode.py          # Minimal QR code encoder (pure Python)
│   ├── gophish.py           # GoPhish API client (urllib)
│   ├── gophish_bridge.py    # REDTEXT → GoPhish data conversion
│   └── config.py            # Config management (INI + env vars + CLI)
├── tests/
│   ├── test_generator.py
│   ├── test_formatters.py
│   ├── test_cli.py
│   ├── test_templates.py
│   ├── test_qrencode.py     # QR encoder tests
│   └── test_gophish.py      # GoPhish integration tests
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
└── README.md
```

## Roadmap

- [x] SMS/Smishing templates
- [x] QR code phishing scenarios
- [ ] Interactive TUI mode
- [ ] HTML email export
- [x] GoPhish integration
- [ ] Localization (FR, ES, DE)
- [ ] AI-powered scenario customization

## Legal

This tool is provided for educational and authorized security testing purposes only. The authors are not responsible for any misuse or damage caused by this tool. Always obtain proper written authorization before conducting social engineering engagements.

## License

GPL v3 License — see [LICENSE](LICENSE) for details.

---

Built by [@keuchnotkush](https://github.com/keuchnotkush)
