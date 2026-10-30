# Security Policy

## Scope and Intent

REDTEXT Generator is a **defensive security and security-awareness tool**. It
produces *fictional* social-engineering scenarios (phishing copy, vishing
scripts, physical pretexts) for use in **authorized** red-team engagements,
penetration tests, and training. It does not exploit systems, deliver payloads,
or harvest credentials on its own.

This document covers two things:

1. How to report a vulnerability in the tool itself.
2. The acceptable-use boundary for the project.

## Reporting a Vulnerability

If you find a security issue in REDTEXT's own code (for example: a code-injection
path through template rendering, an SSRF via the GoPhish client, an unsafe file
write during export, or a secrets-handling flaw in `config.py`), please report it
privately rather than opening a public issue.

- Use GitHub's **[Private Vulnerability Reporting](https://github.com/keuchnotkush/redtext-generator/security/advisories/new)**
  ("Report a vulnerability" under the Security tab), **or**
- Open a minimal public issue that says only "security report — please open a
  private channel" without technical detail, and a maintainer will follow up.

Please include:

- Affected version / commit
- A description of the issue and its impact
- Steps to reproduce (a minimal command or input)
- Any suggested remediation

**Response targets** (best-effort, volunteer-maintained project):

| Stage | Target |
|-------|--------|
| Acknowledgement | within 5 business days |
| Triage / severity assessment | within 10 business days |
| Fix or mitigation plan | depends on severity |

We will credit reporters in the release notes unless you prefer to remain
anonymous.

## Supported Versions

Only the latest released version on the `main` branch receives security fixes.

| Version | Supported |
|---------|-----------|
| 2.1.x   | ✅ |
| < 2.1   | ❌ |

## Acceptable Use

REDTEXT is licensed under GPL-3.0 and provided for lawful, authorized use only.
The following are **out of scope** and will not be accepted as contributions or
supported by maintainers:

- Real malware, exploit payloads, or command-and-control tooling
- Features whose primary purpose is evading detection for unauthorized attacks
- Scenarios targeting specific real individuals or organizations without their
  documented authorization
- Any request to weaponize the tool against a non-consenting target

If you are conducting an engagement, obtain **written authorization** before use.
See the disclaimer in [README.md](README.md) and the ethics section in
[CONTRIBUTING.md](CONTRIBUTING.md).
