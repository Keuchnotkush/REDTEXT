# Contributing to Redtext Generator

## ⚠️ Ethics First

All contributions must align with the project's ethical guidelines:
- Templates and scenarios are for **authorized engagements only**
- No contributions that facilitate actual fraud or unauthorized access
- All pretexts must include educational value (IoCs, red flags, defense notes)

## How to Contribute

### Adding New Templates

The easiest way to contribute is adding new scenarios to `templates.py`:

**New Industry**
```python
"energy": {
    "name": "Energy / Utilities",
    "departments": ["Operations", "IT/OT", "Compliance", "SCADA Engineering"],
    "software": ["OSIsoft PI", "GE iFIX", "Schneider Electric", "ABB Ability"],
    "jargon": ["NERC CIP compliance", "load balancing", "grid stability", "outage management"],
    "pain_points": ["OT/IT convergence", "legacy SCADA vulnerabilities", "regulatory audits"],
}
```

**New Persona**
```python
"recruiter": {
    "name": "Recruiter / HR Representative",
    "titles": ["Technical Recruiter", "HR Business Partner"],
    "pretexts": [
        "reaching out about an open position - need you to review the job description attached",
        "your application has been shortlisted - complete this assessment to proceed",
    ],
}
```

**New Phishing Template, Vishing Script, or Physical Pretext**
- Follow the existing structure exactly
- Include all required fields
- Use `{placeholder}` syntax for dynamic values
- Test with `python -m redtext_generator phishing --template your_template_id`

### Adding Features

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test all generation modes:
```bash
python -m redtext_generator phishing -i finance -u high
python -m redtext_generator vishing -p vendor -c "Test Corp"
python -m redtext_generator physical -i healthcare
python -m redtext_generator full -i tech -u critical
python -m redtext_generator list
```
5. Commit with a descriptive message: `git commit -m "feat: add recruiter persona"`
6. Push and open a PR

### Code Style

- Python 3.8+ compatible
- No external dependencies — stdlib only
- Use type hints where possible
- Follow existing naming conventions
- Keep templates realistic but clearly fictional

### Ideas for Contributions

- [ ] New industries (energy, legal, hospitality, transportation)
- [ ] New personas (recruiter, law enforcement, insurance adjuster)
- [ ] More phishing templates (QR code phishing, SMS/smishing)
- [ ] Localization (templates in French, Spanish, German)
- [ ] Interactive TUI mode with `curses`
- [ ] HTML email export with realistic formatting
- [ ] Integration with GoPhish for campaign deployment

## Quick Sanity Check

You can run a minimal check without a test suite:
```bash
python -c "from redtext_generator.generator import RedtextGenerator as G; print(G().generate_phishing_email()['subject'])"
```

Optional compile check:
```bash
python -m compileall redtext_generator
```

## Design Guidelines

- Keep templates as data in `redtext_generator/templates.py`
- Keep generator logic in `redtext_generator/generator.py`
- Prefer fictional names, domains, and identifiers
- Maintain ASCII in new content unless a non-ASCII character is required

## Adding Templates

1. Add a new entry to the relevant list in `redtext_generator/templates.py` with a unique `id` and `name`
2. Ensure any new `{placeholders}` are supported in `redtext_generator/generator.py`
3. Keep outputs realistic but clearly fictional

## Adding a New Generator Method

1. Add a method on `RedtextGenerator` that returns a structured `dict`
2. Use existing helpers like `_random_name()` and `_random_id()` for consistency
3. Add any new template catalog to `redtext_generator/templates.py`
4. Update README usage examples if you add a new public method

## Reporting Issues

Open an issue with:
- What you ran (full command)
- What you expected
- What happened instead
- Python version (`python --version`)

## Submitting Changes

1. Run the sanity checks above
2. Make sure documentation reflects any new options or placeholders
3. Open a PR with a clear description and example output

## License

By contributing, you agree that your contributions will be licensed under the GPL v3 License.