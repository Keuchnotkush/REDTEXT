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

No external dependencies. No API keys. Pure Python.

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
│   └── formatters.py        # Terminal display (ANSI colors) + JSON/Markdown export
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
└── README.md
```

## Roadmap

- [ ] SMS/Smishing templates
- [ ] QR code phishing scenarios
- [ ] Interactive TUI mode
- [ ] HTML email export
- [ ] GoPhish integration
- [ ] Localization (FR, ES, DE)
- [ ] AI-powered scenario customization

## Legal

This tool is provided for educational and authorized security testing purposes only. The authors are not responsible for any misuse or damage caused by this tool. Always obtain proper written authorization before conducting social engineering engagements.

## License

GPL v3 License — see [LICENSE](LICENSE) for details.

---

Built by [@keuchnotkush](https://github.com/keuchnotkush)
