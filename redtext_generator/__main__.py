#!/usr/bin/env python3
"""
Redtext Generator CLI
Social Engineering Scenario Builder for Authorized Red Team Operations
"""

import argparse
import sys
import random

from .generator import RedtextGenerator
from .formatters import (
    format_phishing_email,
    format_smishing_message,
    format_quishing_scenario,
    format_vishing_script,
    format_physical_pretext,
    format_full_scenario,
    export_json,
    export_markdown,
    export_html,
    loading_animation,
    Colors,
    _c,
)
from .templates import INDUSTRIES, PERSONAS, URGENCY_TRIGGERS, PSYCH_PRINCIPLES


BANNER = f"""
{Colors.RED}
  ██████╗ ███████╗██████╗ ████████╗███████╗██╗  ██╗████████╗
  ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
  ██████╔╝█████╗  ██║  ██║   ██║   █████╗   ╚███╔╝    ██║
  ██╔══██╗██╔══╝  ██║  ██║   ██║   ██╔══╝   ██╔██╗    ██║
  ██║  ██║███████╗██████╔╝   ██║   ███████╗██╔╝ ██╗   ██║
  ╚═╝  ╚═╝╚══════╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝
       {Colors.YELLOW} ██████╗ ███████╗███╗   ██╗
       ██╔════╝ ██╔════╝████╗  ██║
       ██║  ███╗█████╗  ██╔██╗ ██║
       ██║   ██║██╔══╝  ██║╚██╗██║
       ╚██████╔╝███████╗██║ ╚████║
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝{Colors.RESET}

  {Colors.RED}╔══════════════════════════════════════════════════════════╗
  ║{Colors.RESET} {Colors.BOLD}  ◢◤ SOCIAL ENGINEERING SCENARIO BUILDER ◢◤{Colors.RESET}             {Colors.RED}║
  ║{Colors.RESET}                                                          {Colors.RED}║
  ║{Colors.RESET}  {Colors.DIM}  ▸ Phishing Emails    ▸ Vishing Scripts{Colors.RESET}              {Colors.RED}║
  ║{Colors.RESET}  {Colors.DIM}  ▸ SMS/Smishing        ▸ QR/Quishing{Colors.RESET}                   {Colors.RED}║
  ║{Colors.RESET}  {Colors.DIM}  ▸ Physical Pretexts   ▸ Full Attack Scenarios{Colors.RESET}       {Colors.RED}║
  ║{Colors.RESET}                                                          {Colors.RED}║
  ║{Colors.RESET}  {Colors.YELLOW}  "Some data is too dangerous to record."{Colors.RESET}            {Colors.RED}║
  ║{Colors.RESET}  {Colors.DIM}                          — SCP-2521{Colors.RESET}                  {Colors.RED}║
  ╚══════════════════════════════════════════════════════════╝{Colors.RESET}
  {Colors.DIM}v1.0.0 | @keuchnotkush | For authorized use only{Colors.RESET}
"""

DISCLAIMER = f"""
{Colors.RED}{Colors.BOLD}  ⚠  DISCLAIMER  ⚠  {Colors.RESET}

{Colors.YELLOW}  This tool is designed for AUTHORIZED red team operations,
  security awareness training, and penetration testing ONLY.

  Unauthorized use of social engineering techniques is ILLEGAL
  and UNETHICAL. Always obtain written authorization before
  conducting any social engineering engagement.

  The authors assume NO liability for misuse of this tool.{Colors.RESET}
"""


def cmd_list(args):
    """List available options."""
    loading_animation("Loading available options", 2.0)
    print(_c("\n  Available Industries:", Colors.BOLD + Colors.PURPLE))
    for key, val in INDUSTRIES.items():
        depts = ", ".join(val["departments"][:3])
        print(f"    {_c(key, Colors.YELLOW):30s} {val['name']} ({depts}...)")

    print(_c("\n  Available Personas:", Colors.BOLD + Colors.PURPLE))
    for key, val in PERSONAS.items():
        titles = ", ".join(val["titles"][:2])
        print(f"    {_c(key, Colors.YELLOW):30s} {val['name']} ({titles}...)")

    print(_c("\n  Urgency Levels:", Colors.BOLD + Colors.PURPLE))
    for key, val in URGENCY_TRIGGERS.items():
        print(f"    {_c(key, Colors.YELLOW):30s} e.g. \"{val[0]}\"")

    print(_c("\n  Psychological Principles:", Colors.BOLD + Colors.PURPLE))
    for key, val in PSYCH_PRINCIPLES.items():
        print(f"    {_c(key, Colors.YELLOW):30s} {val['description']}")
    print()


def cmd_generate(args):
    """Generate a redtext scenario."""
    gen = RedtextGenerator(
        industry=args.industry,
        urgency=args.urgency,
        persona=args.persona,
        company_name=args.company,
    )

    if args.seed is not None:
        random.seed(args.seed)

    messages = {
        "phishing": "Crafting phishing email",
        "smishing": "Crafting smishing message",
        "quishing": "Generating QR phishing scenario",
        "vishing": "Building vishing script",
        "physical": "Preparing physical pretext",
        "full": "Assembling full attack scenario",
    }
    loading_animation(messages.get(args.command, "Generating"), 1.5)

    if args.command == "phishing":
        data = gen.generate_phishing_email(template_id=args.template)
        output = format_phishing_email(data)
    elif args.command == "smishing":
        data = gen.generate_smishing_message(template_id=args.template)
        output = format_smishing_message(data)
    elif args.command == "quishing":
        data = gen.generate_quishing_scenario(template_id=args.template)
        output = format_quishing_scenario(data)
    elif args.command == "vishing":
        data = gen.generate_vishing_script(script_id=args.template)
        output = format_vishing_script(data)
    elif args.command == "physical":
        data = gen.generate_physical_pretext(pretext_id=args.template)
        output = format_physical_pretext(data)
    elif args.command == "full":
        data = gen.generate_full_scenario()
        output = format_full_scenario(data)
    else:
        print(_c("  Unknown command. Use --help for usage.", Colors.RED))
        return

    print(output)

    if args.export_json:
        path = export_json(data, args.export_json)
        print(_c(f"\n  ✓ Exported JSON: {path}", Colors.YELLOW))

    if args.export_md:
        path = export_markdown(data, args.export_md)
        print(_c(f"\n  ✓ Exported Markdown: {path}", Colors.YELLOW))

    if args.export_html:
        path = export_html(data, args.export_html)
        print(_c(f"\n  ✓ Exported HTML: {path}", Colors.YELLOW))


def cmd_gophish(args):
    """Dispatch GoPhish sub-subcommands."""
    subcmd = getattr(args, "gophish_command", None)
    if not subcmd:
        print(_c("  Use 'redtext-gen gophish --help' for available commands.", Colors.YELLOW))
        return

    if subcmd == "setup":
        _gophish_setup()
    elif subcmd == "templates":
        _gophish_templates(args)
    elif subcmd == "push":
        _gophish_push(args)
    elif subcmd == "campaign":
        _gophish_campaign(args)
    elif subcmd == "status":
        _gophish_status(args)


def _gophish_setup():
    """Interactive setup for GoPhish connection."""
    from .config import save_gophish_config

    print(_c("\n  GoPhish API Configuration\n", Colors.BOLD + Colors.CYAN))
    api_url = input("  GoPhish URL [https://localhost:3333]: ").strip() or "https://localhost:3333"
    api_key = input("  API Key: ").strip()
    verify_ssl_input = input("  Verify SSL? [Y/n]: ").strip().lower()
    verify_ssl = verify_ssl_input not in ("n", "no", "false", "0")

    if not api_key:
        print(_c("  Error: API key is required.", Colors.RED))
        return

    path = save_gophish_config(api_url, api_key, verify_ssl)
    print(_c(f"\n  Configuration saved to {path}", Colors.GREEN))


def _gophish_error(err):
    """Print a contextual error message for GoPhish failures."""
    from .gophish import GoPhishAPIError

    if isinstance(err, ValueError):
        print(_c(f"  Config error: {err}", Colors.RED))
        print(_c("    Run 'redtext-gen gophish setup' to configure.", Colors.DIM))
    elif isinstance(err, GoPhishAPIError):
        print(_c(f"  API error: {err}", Colors.RED))
        if err.status_code == 401:
            print(_c("    Check your API key — it may be invalid or expired.", Colors.DIM))
        elif err.status_code == 404:
            print(_c("    Resource not found — verify the name exists in GoPhish.", Colors.DIM))
        elif err.status_code and err.status_code >= 500:
            print(_c("    GoPhish server error — check the server logs.", Colors.DIM))
        elif "Connection error" in str(err) or "Connection refused" in str(err):
            print(_c("    Is GoPhish running? Check the URL and port.", Colors.DIM))
    else:
        print(_c(f"  Error: {err}", Colors.RED))


def _gophish_templates(args):
    """List templates from GoPhish server."""
    from .config import load_gophish_config
    from .gophish import GoPhishClient, GoPhishAPIError

    try:
        config = load_gophish_config(args)
        client = GoPhishClient(config["api_url"], config["api_key"], config["verify_ssl"])
        templates = client.get_templates()
    except (ValueError, GoPhishAPIError) as e:
        _gophish_error(e)
        return

    print(_c("\n  GoPhish Templates:\n", Colors.BOLD + Colors.CYAN))
    if not templates:
        print(_c("  No templates found.", Colors.DIM))
        return
    for t in templates:
        print(f"    {_c(str(t.get('id', '?')), Colors.YELLOW):>10s}  {t.get('name', 'Unnamed')}")
    print()


def _gophish_push(args):
    """Generate a phishing scenario and push it as a GoPhish template."""
    from .config import load_gophish_config
    from .gophish import GoPhishClient, GoPhishAPIError
    from .gophish_bridge import phishing_to_template

    gen = RedtextGenerator(
        industry=args.industry, urgency=args.urgency,
        persona=args.persona, company_name=args.company,
    )

    if args.seed is not None:
        random.seed(args.seed)

    loading_animation("Crafting phishing template", 1.5)
    phishing_data = gen.generate_phishing_email(template_id=args.template)
    template_payload = phishing_to_template(phishing_data, template_name=args.name)

    print(format_phishing_email(phishing_data))
    print(_c(f"  Pushing as GoPhish template: {template_payload['name']}", Colors.YELLOW))

    try:
        config = load_gophish_config(args)
        client = GoPhishClient(config["api_url"], config["api_key"], config["verify_ssl"])
        result = client.create_template(
            name=template_payload["name"],
            subject=template_payload["subject"],
            text=template_payload["text"],
            html=template_payload["html"],
        )
    except (ValueError, GoPhishAPIError) as e:
        _gophish_error(e)
        return

    print(_c(f"\n  Template created (ID: {result.get('id', 'unknown')})", Colors.GREEN))


def _gophish_campaign(args):
    """Create a full GoPhish campaign."""
    from .config import load_gophish_config
    from .gophish import GoPhishClient, GoPhishAPIError
    from .gophish_bridge import build_campaign_config, parse_targets_csv

    try:
        config = load_gophish_config(args)
        client = GoPhishClient(config["api_url"], config["api_key"], config["verify_ssl"])

        if args.targets_csv:
            loading_animation("Parsing targets CSV", 0.5)
            try:
                targets = parse_targets_csv(args.targets_csv)
            except (ValueError, FileNotFoundError, PermissionError) as csv_err:
                print(_c(f"  CSV error: {csv_err}", Colors.RED))
                print(_c("    Expected columns: email, first_name, last_name, position", Colors.DIM))
                return
            client.create_group(args.group_name, targets)
            print(_c(f"  Created group '{args.group_name}' with {len(targets)} targets", Colors.GREEN))

        campaign_name = args.campaign_name or f"REDTEXT Campaign - {args.template_name}"
        campaign_config = build_campaign_config(
            scenario_name=campaign_name,
            template_name=args.template_name,
            group_name=args.group_name,
            smtp_name=args.smtp_name,
            landing_page=args.page_name,
            url=args.url,
            launch_date=args.launch_date,
        )

        loading_animation("Creating campaign", 1.0)
        result = client.create_campaign(**campaign_config)
    except (ValueError, GoPhishAPIError) as e:
        _gophish_error(e)
        return

    print(_c(f"\n  Campaign created (ID: {result.get('id', 'unknown')})", Colors.GREEN))
    if args.launch_date:
        print(_c(f"  Scheduled for: {args.launch_date}", Colors.YELLOW))
    else:
        print(_c("  Campaign launched immediately.", Colors.YELLOW))


def _gophish_status(args):
    """Display campaign results."""
    from .config import load_gophish_config
    from .gophish import GoPhishClient, GoPhishAPIError

    try:
        config = load_gophish_config(args)
        client = GoPhishClient(config["api_url"], config["api_key"], config["verify_ssl"])
        results = client.get_campaign_results(args.campaign_id)
    except (ValueError, GoPhishAPIError) as e:
        _gophish_error(e)
        return

    print(_c(f"\n  Campaign {args.campaign_id} Results:\n", Colors.BOLD + Colors.CYAN))
    stats = results.get("stats", {})
    if stats:
        for key, val in stats.items():
            label = key.replace("_", " ").title()
            print(f"    {_c(label + ':', Colors.GREEN)} {val}")
    else:
        for key, val in results.items():
            if isinstance(val, (str, int, float)):
                label = key.replace("_", " ").title()
                print(f"    {_c(label + ':', Colors.GREEN)} {val}")
    print()


def main():
    parser = argparse.ArgumentParser(
        prog="redtext-gen",
        description="Redtext — Social Engineering Scenario Builder for Red Teams",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  redtext-gen phishing --industry finance --urgency high\n"
               "  redtext-gen smishing --industry finance --urgency critical\n"
               "  redtext-gen quishing --industry tech --urgency high\n"
               "  redtext-gen vishing --persona vendor --company 'Acme Corp'\n"
               "  redtext-gen physical --industry healthcare\n"
               "  redtext-gen full --industry tech --urgency critical\n"
               "  redtext-gen list\n",
    )

    parser.add_argument("--no-banner", action="store_true", help="Suppress the banner")
    parser.add_argument("--no-disclaimer", action="store_true", help="Suppress the disclaimer")

    subparsers = parser.add_subparsers(dest="command", help="Generation mode")
    subparsers.add_parser("list", help="List available industries, personas, and options")

    def add_common_args(p):
        p.add_argument("-i", "--industry", default="tech", choices=list(INDUSTRIES.keys()),
                       help="Target industry (default: tech)")
        p.add_argument("-u", "--urgency", default="medium", choices=list(URGENCY_TRIGGERS.keys()),
                       help="Urgency level (default: medium)")
        p.add_argument("-p", "--persona", default="it_support", choices=list(PERSONAS.keys()),
                       help="Attacker persona (default: it_support)")
        p.add_argument("-c", "--company", default="Target Corp",
                       help="Target company name (default: Target Corp)")
        p.add_argument("-t", "--template", default=None,
                       help="Specific template ID to use")
        p.add_argument("-s", "--seed", type=int, default=None,
                       help="Random seed for reproducible output")
        p.add_argument("--export-json", default=None, metavar="FILE",
                       help="Export scenario as JSON")
        p.add_argument("--export-md", default=None, metavar="FILE",
                       help="Export scenario as Markdown")
        p.add_argument("--export-html", default=None, metavar="FILE",
                       help="Export scenario as HTML report")

    for name, desc in [("phishing", "Generate phishing email"), ("smishing", "Generate smishing (SMS) message"),
                       ("quishing", "Generate QR code phishing scenario"),
                       ("vishing", "Generate vishing call script"),
                       ("physical", "Generate physical access pretext"), ("full", "Generate full attack scenario")]:
        add_common_args(subparsers.add_parser(name, help=desc))

    # ── GoPhish integration subcommands ────────────────────────
    gophish_parser = subparsers.add_parser("gophish", help="GoPhish integration commands")
    gophish_sub = gophish_parser.add_subparsers(dest="gophish_command")

    gophish_sub.add_parser("setup", help="Configure GoPhish API connection")
    gophish_sub.add_parser("templates", help="List templates from GoPhish server")

    push_parser = gophish_sub.add_parser("push", help="Generate and push phishing template to GoPhish")
    add_common_args(push_parser)
    push_parser.add_argument("--name", default=None, help="Override template name in GoPhish")
    push_parser.add_argument("--gophish-url", default=None, help="GoPhish API URL")
    push_parser.add_argument("--gophish-key", default=None, help="GoPhish API key")
    push_parser.add_argument("--no-verify-ssl", action="store_true", help="Skip SSL certificate verification")

    camp_parser = gophish_sub.add_parser("campaign", help="Create a GoPhish campaign")
    camp_parser.add_argument("--template-name", required=True, help="GoPhish template name")
    camp_parser.add_argument("--group-name", required=True, help="GoPhish target group name")
    camp_parser.add_argument("--smtp-name", required=True, help="GoPhish SMTP profile name")
    camp_parser.add_argument("--page-name", required=True, help="GoPhish landing page name")
    camp_parser.add_argument("--url", required=True, help="Phishing URL")
    camp_parser.add_argument("--targets-csv", default=None, help="CSV file to auto-create target group")
    camp_parser.add_argument("--launch-date", default=None, help="Campaign launch date (ISO 8601)")
    camp_parser.add_argument("--campaign-name", default=None, help="Campaign name (auto-generated if omitted)")
    camp_parser.add_argument("--gophish-url", default=None, help="GoPhish API URL")
    camp_parser.add_argument("--gophish-key", default=None, help="GoPhish API key")
    camp_parser.add_argument("--no-verify-ssl", action="store_true", help="Skip SSL certificate verification")

    status_parser = gophish_sub.add_parser("status", help="Get campaign results")
    status_parser.add_argument("campaign_id", type=int, help="Campaign ID")
    status_parser.add_argument("--gophish-url", default=None, help="GoPhish API URL")
    status_parser.add_argument("--gophish-key", default=None, help="GoPhish API key")
    status_parser.add_argument("--no-verify-ssl", action="store_true", help="Skip SSL certificate verification")

    args = parser.parse_args()

    if not args.command:
        print(BANNER)
        parser.print_help()
        sys.exit(0)

    if not getattr(args, "no_banner", False):
        print(BANNER)

    if args.command == "list":
        cmd_list(args)
    elif args.command == "gophish":
        cmd_gophish(args)
    else:
        if not getattr(args, "no_disclaimer", False):
            print(DISCLAIMER)
        cmd_generate(args)


if __name__ == "__main__":
    main()