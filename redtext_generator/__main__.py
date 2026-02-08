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
    format_vishing_script,
    format_physical_pretext,
    format_full_scenario,
    export_json,
    export_markdown,
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
        "vishing": "Building vishing script",
        "physical": "Preparing physical pretext",
        "full": "Assembling full attack scenario",
    }
    loading_animation(messages.get(args.command, "Generating"), 1.5)

    if args.command == "phishing":
        data = gen.generate_phishing_email(template_id=args.template)
        output = format_phishing_email(data)
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


def main():
    parser = argparse.ArgumentParser(
        prog="redtext-gen",
        description="Redtext — Social Engineering Scenario Builder for Red Teams",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  redtext-gen phishing --industry finance --urgency high\n"
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

    for name, desc in [("phishing", "Generate phishing email"), ("vishing", "Generate vishing call script"),
                       ("physical", "Generate physical access pretext"), ("full", "Generate full attack scenario")]:
        add_common_args(subparsers.add_parser(name, help=desc))

    args = parser.parse_args()

    if not args.command:
        print(BANNER)
        parser.print_help()
        sys.exit(0)

    if not getattr(args, "no_banner", False):
        print(BANNER)

    if args.command == "list":
        cmd_list(args)
    else:
        if not getattr(args, "no_disclaimer", False):
            print(DISCLAIMER)
        cmd_generate(args)


if __name__ == "__main__":
    main()