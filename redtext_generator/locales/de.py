"""Deutsche Sprachstrings für REDTEXT."""

STRINGS = {
    "meta": {
        "language_name": "Deutsch",
        "language_code": "de",
    },

    # ── Industries ─────────────────────────────────────────────
    "industries": {
        "tech": {
            "name": "Technologie",
            "departments": ["Entwicklung", "DevOps", "IT", "Sicherheit"],
            "jargon": ["Sprint-Planung", "CI/CD-Pipeline", "SSO-Integration", "Incident Response"],
            "pain_points": ["Produktionsausfälle", "Zugangsdatenrotation", "Bereitschaftsüberlastung"],
        },
        "finance": {
            "name": "Finanzdienstleistungen",
            "departments": ["Buchhaltung", "Risikomanagement", "Compliance", "IT", "Handelsabteilung", "Interne Revision"],
            "jargon": ["Geschäftsquartal", "regulatorische Compliance", "Prüfpfad", "Risikobewertung", "KYC-Prüfung", "Geldwäscheprävention", "SOX-Prüfung"],
            "pain_points": ["regulatorische Fristen", "Betrugsprävention", "Datenschutzverletzungen"],
        },
        "healthcare": {
            "name": "Gesundheitswesen",
            "departments": ["Patientenakten", "Abrechnung", "IT", "Compliance"],
            "jargon": ["DSGVO-Konformität", "Patientenportal", "KIS-System", "klinischer Workflow"],
            "pain_points": ["Patientendatensicherheit", "Systemausfälle", "behördliche Prüfungen"],
        },
        "government": {
            "name": "Öffentlicher Dienst",
            "departments": ["Sicherheit", "IT", "Compliance", "Betrieb"],
            "jargon": ["Verschlusssachen", "Sicherheitsüberprüfung", "BSI-Grundschutz", "ISO-27001-Standards", "Maßnahmenplan-Umsetzung", "Betriebsfreigabe"],
            "pain_points": ["Datenklassifizierung", "Zugriffskontrollprobleme", "Compliance-Prüfungen"],
        },
        "education": {
            "name": "Bildungswesen",
            "departments": ["IT", "Studierendensekretariat", "Studienfinanzierung", "Studierendenservice"],
            "jargon": ["Kursverwaltung", "Campus-Management-System", "virtuelle Lernumgebung", "Einschreibungszyklus"],
            "pain_points": ["Phishing-Angriffe auf Studierende", "Zugangsdatendiebstahl", "Systemausfälle während der Einschreibung"],
        },
        "manufacturing": {
            "name": "Fertigung",
            "departments": ["Betrieb", "IT", "Lieferkette", "Qualitätskontrolle"],
            "jargon": ["Produktionslinie", "Lieferkettenunterbrechung", "Qualitätssicherung", "Lagerumschlag", "SCADA-System", "SPS-Firmware"],
            "pain_points": ["Produktionsstillstand", "Lieferkettenangriffe", "Diebstahl geistigen Eigentums"],
        },
        "retail": {
            "name": "Einzelhandel",
            "departments": ["Vertrieb", "IT", "Kundenservice", "Logistik"],
            "jargon": ["Kassensystem", "Kundenbeziehungsmanagement", "Lieferkettenlogistik", "Lagerumschlag", "PCI-DSS-Konformität"],
            "pain_points": ["Zahlungskartenvorfälle", "Zugangsdatendiebstahl bei Mitarbeitenden", "Lieferkettenunterbrechungen"],
        },
    },

    # ── Personas ───────────────────────────────────────────────
    "personas": {
        "it_support": {
            "name": "IT-Support-Techniker",
            "titles": ["IT-Support-Spezialist", "Helpdesk-Analyst", "Systemadministrator", "Desktop-Support-Techniker"],
            "pretexts": [
                "Ihr Passwort läuft in 2 Stunden ab – setzen Sie es jetzt über dieses Portal zurück, um eine Kontosperrung zu vermeiden",
                "Wir installieren ein kritisches Sicherheitsupdate für {software} – bitte führen Sie das angehängte Installationsprogramm aus oder gewähren Sie Fernzugriff",
                "Ihr Konto wurde wegen verdächtiger Anmeldeaktivitäten markiert – bestätigen Sie Ihre Identität, um eine Sperrung zu verhindern",
                "Geplante MFA-Registrierung für Ihre Abteilung – schließen Sie die Registrierung bis Geschäftsschluss ab, da sonst Ihr Zugang eingeschränkt wird",
                "VPN-Konfigurationsaktualisierung erforderlich – laden Sie das neue Profil über diesen Link herunter, bevor Ihr Fernzugriff gesperrt wird",
                "Ihr Arbeitsplatzrechner hat unseren letzten Sicherheitsscan nicht bestanden – wir benötigen Fernzugriff zur Behebung vor dem nächsten Prüfzyklus",
            ],
        },
        "vendor": {
            "name": "Externer Dienstleister",
            "titles": ["Technical Account Manager", "Customer Success Engineer", "Integrationsspezialist"],
            "pretexts": [
                "Ihre {software}-Lizenz läuft in 48 Stunden ab – bestätigen Sie die Verlängerung umgehend",
                "Kritische Sicherheitslücke in {software} entdeckt – wir müssen Ihren Arbeitsbereich sichern und zurücksetzen",
                "Ihre {software}-Integration verursacht Systemkonflikte – wir müssen Ihre Daten übertragen, um das Problem zu beheben",
                "Dringendes Sicherheitsupdate für {software} – Ihre Genehmigung zur Installation wird benötigt",
                "Ihre {software}-Umgebung hat unseren Compliance-Scan nicht bestanden – wir benötigen Fernzugriff zur Behebung",
            ],
        },
        "executive": {
            "name": "Geschäftsführung / Vorstandsebene",
            "titles": ["CEO", "CFO", "CTO", "COO", "VP Operations"],
            "pretexts": [
                "Senden Sie mir den vierteljährlichen Sicherheitsbericht vor meinem Meeting – ich brauche ihn innerhalb einer Stunde",
                "Bearbeiten Sie die beigefügten Überweisungsanweisungen diskret – wir können uns keinen Informationsabfluss leisten",
                "Ich habe bereits mit {name} darüber gesprochen – ich brauche eine sofortige Bearbeitung",
                "Vertrauliche Übernahmeprüfung – Finanzdaten müssen bis Geschäftsschluss vorliegen",
                "Genehmigung einer Lieferantenzahlung – Überweisung vor 15:00 Uhr heute, Details im Anhang",
            ],
        },
        "auditor": {
            "name": "Externer Prüfer",
            "titles": ["Audit-Manager", "Compliance-Prüfer", "Risikobewertungsspezialist", "Sicherheitsgutachter"],
            "pretexts": [
                "Wir führen eine DSGVO-Compliance-Prüfung durch – wir benötigen gespeicherte Nutzerdaten und exemplarische personenbezogene Daten bis Mitternacht, andernfalls drohen dem Unternehmen rechtliche Schritte wegen Nichteinhaltung",
                "Von ATOS beauftragt zur Prüfung der Zugriffsprotokolle und Verifizierung privilegierter Kontoaktivitäten – bei Nichtbereitstellung bis morgen früh wird dies als Prüfungsausnahme vermerkt und an den Vorstand eskaliert",
                "Wir führen eine Lohnabrechnungs-Compliance-Prüfung durch – wir benötigen alle relevanten Tabellen dieses Quartals bis morgen Nachmittag, andernfalls wird eine Vor-Ort-Prüfung durch die Finanzbehörde ausgelöst",
                "Jährliche Sicherheitsprüfung – wir benötigen aktuelle Firewall-Konfigurationen und Admin-Zugangslisten innerhalb von 24 Stunden",
                "Nachverfolgung der Drittanbieter-Risikobewertung – Ihre Compliance-Dokumentation ist überfällig und blockiert die Zertifizierungsverlängerung",
            ],
        },
        "new_employee": {
            "name": "Neuer Mitarbeiter",
            "titles": ["Neue Fachkraft", "Kürzlich Versetzter", "Auftragnehmer (erster Tag)", "Praktikant"],
            "pretexts": [
                "Neuer Mitarbeiter aus der Netzwerkabteilung – könnten Sie bitte den angehängten Geschwindigkeitstest ausführen, um die Standortleistung zu bewerten",
                "Mein Ausweis funktioniert nicht am Serverraum – mein Vorgesetzter {name} hat mich gebeten, nach Feierabend die RJ45-Kabel zu tauschen",
                "Mein Konto wird gerade aktiviert – könnten Sie mir den Netzwerkinfrastrukturplan weiterleiten, damit ich außerhalb der Arbeitszeiten beginnen kann",
                "Mein Vorgesetzter {name} sagte, ich soll Sie um vorübergehenden Zugang bitten – die IT hat mein Konto noch nicht eingerichtet",
                "Erster Tag und ich komme nicht auf {software} – ich brauche temporäre Zugangsdaten für die Einführungsschulung um 14:00 Uhr",
            ],
        },
        "physical": {
            "name": "Physischer Eindringling",
            "titles": ["Klimatechniker", "Lieferfahrer", "Wartungstechniker", "Telekommunikationstechniker", "Brandschutzinspektor"],
            "pretexts": [
                "Ich bin hier, um den Versammlungsraum für die Renovierungen im Q4 zu dokumentieren",
                "Lieferung eines Smart-Druckers für die Personalabteilung – der Vorgesetzte hat eine Direktlieferung ins Büro angeordnet",
                "Wartung der zentralen Stromversorgung – fehlerhafte Kabel wurden vom Standortverwalter gemeldet, der mich vor Ort angefordert hat",
                "Geplante Netzwerkkabelinstallation gemäß Arbeitsauftrag #{wo_number} – die Hausverwaltung hat den Zugang genehmigt",
                "Jährliche Zertifizierung der Brandschutzanlage – ich benötige Zugang zu allen Etagen einschließlich Serverraum",
            ],
        },
    },

    # ── Urgency triggers ──────────────────────────────────────
    "urgency_triggers": {
        "low": [
            "Wenn Sie die Gelegenheit haben",
            "Bitte prüfen Sie dies bei Gelegenheit",
            "Schauen Sie sich das gerne an, wenn es Ihnen zeitlich passt",
            "Keine Eile, aber bitte sehen Sie es sich bei Gelegenheit an",
        ],
        "medium": [
            "Bis Geschäftsschluss heute",
            "Bitte bis morgen erledigen",
            "Dies muss vor dem Wochenende bearbeitet werden",
            "Bitte priorisieren Sie diese Aufgabe",
        ],
        "high": [
            "Dies muss innerhalb der nächsten 30 Minuten geschehen",
            "Dies erfordert sofortige Aufmerksamkeit",
            "Bitte erledigen Sie dies innerhalb der nächsten Stunde",
            "Dringende Aufgabe – bitte handeln Sie jetzt",
        ],
        "critical": [
            "Es findet gerade ein Sicherheitsvorfall statt und Ihr Konto ist noch nicht kompromittiert",
            "Gemäß dringendem Vorstandsbeschluss – alle Führungskräfte müssen ihre Zugangsdaten bis Mitternacht erneut verifizieren",
            "Zur Erfüllung einer BaFin-Anfrage prüfen und übermitteln Sie die Berichte dieses Quartals umgehend",
            "Prüfen und senden Sie die in der ersten Woche von Q2 unterzeichneten Verträge – ein Mangel wurde festgestellt und Kunden drohen mit rechtlichen Schritten",
        ],
    },

    # ── Seasonal hooks ────────────────────────────────────────
    "seasonal_hooks": {
        "q1": [
            "Jährliche Anmeldung zur Sicherheitsschulung",
            "Steuersaison – Einreichung von Unterlagen und Lohnsteuerbescheinigungen",
            "Jährliche Durchsetzung der Passwortrichtlinie",
            "Frist für den Q1-Finanzbericht rückt näher",
        ],
        "q2": [
            "Halbjährliche Compliance-Prüfung",
            "Onboarding der Sommerpraktikanten – IT-Zugangsanfragen",
            "Vierteljährliche Hinweise zur Softwarelizenz-Verlängerung",
            "Passwortrichtlinien-Nachverfolgung für im Q1 erstellte Konten",
        ],
        "q3": [
            "Vorbereitung auf die Jahresabschlussprüfung",
            "Notfallwiederherstellungsübung",
            "Gespräche zur Verlängerung auslaufender Lieferantenverträge",
            "Q3-Leistungsbeurteilungszyklus – Genehmigungen durch Vorgesetzte",
        ],
        "q4": [
            "Feiertagsplanung – dringend vor Betriebsschließung",
            "Jahresend-Compliance-Frist – letzte Einreichungen",
            "Jahresabschlussberichterstattung",
            "Sicherheitsschulungen zur Weihnachtszeit",
        ],
    },

    # ── Phishing templates ────────────────────────────────────
    "phishing_templates": [
        {
            "id": "credential_harvest",
            "name": "Zugangsdaten-Abfrage",
            "subject_lines": [
                "Handlungsbedarf: Bestätigen Sie Ihr {software}-Konto",
                "Sicherheitswarnung: Ungewöhnliche Aktivitäten in Ihrem {software}-Konto festgestellt",
                "Sofortiger Handlungsbedarf: Bestätigen Sie Ihre {software}-Kontodaten",
                "Warnung: {software}-Kontosperrung – Jetzt verifizieren",
            ],
            "body": "Guten Tag {first_name},\n\n{urgency_opening}\n\nBitte bestätigen Sie Ihre Identität über den folgenden Link:\n\n{phishing_link}\n\nWenn Sie dies nicht innerhalb von {deadline} abschließen, wird Ihr Zugang zu {software} vorübergehend gesperrt.\n\n{signature}",
        },
        {
            "id": "malicious_attachment",
            "name": "Schädlicher Anhang",
            "subject_lines": [
                "Wichtig: {document_name} – Prüfung erforderlich",
                "Aktualisierung {department}: Bitte prüfen Sie das angehängte Dokument",
                "Vertraulich: {document_name} – Nur für Sie bestimmt",
                "Handlungsbedarf: {document_name} prüfen und unterschreiben",
            ],
            "body": "Guten Tag {first_name},\n\n{urgency_opening}\n\nIm Anhang finden Sie das {document_type}, das Ihre sofortige Prüfung erfordert. Dieses Dokument wurde von der Leitung der Abteilung {department} freigegeben und wird an alle betroffenen Mitarbeitenden verteilt.\n\n\U0001f4ce {attachment_note}\n\nBitte prüfen, unterschreiben und bis {deadline} zurücksenden. Sollten Sie Probleme beim Öffnen haben, aktivieren Sie bitte die Makros, wenn Sie dazu aufgefordert werden – dies ist gemäß unserer Dokumentensicherheitsrichtlinie erforderlich.\n\n{signature}",
        },
        {
            "id": "bec_wire",
            "name": "CEO-Betrug (Überweisungsbetrug)",
            "subject_lines": [
                "Vertraulich – Dringende Zahlung erforderlich",
                "AW: Lieferantenzahlung – Aktualisierte Bankverbindung",
                "Kurze Bitte – Bitte diskret behandeln",
                "{executive_name} – Dringende Überweisungsanforderung",
            ],
            "body": "Guten Tag {first_name},\n\nIch brauche Sie für eine dringende und vertrauliche Angelegenheit. Wir stehen kurz vor dem Abschluss eines vertraulichen Geschäfts und ich benötige eine Überweisung noch vor Geschäftsschluss.\n\nBitte veranlassen Sie Folgendes:\n\n    Betrag: {amount} EUR\n    Bank: {bank_name}\n    Konto: {account_placeholder}\n    Verwendungszweck: {reference}\n\nDies muss bis {deadline} abgeschlossen sein. Besprechen Sie dies bitte mit niemandem, bis das Geschäft abgeschlossen ist – wir können uns keinen Informationsabfluss leisten.\n\nIch habe dies bereits mit der Rechtsabteilung abgestimmt. Bestätigen Sie bitte nach Erledigung.\n\n{executive_signature}",
        },
        {
            "id": "callback_phishing",
            "name": "Rückruf-Phishing (Vishing-Vorbereitung)",
            "subject_lines": [
                "Abonnementverlängerung – Belastung von {amount} EUR verarbeitet",
                "Auftragsbestätigung #{invoice_number}",
                "Ihrem Konto wurden {amount} EUR belastet",
                "Quittung für kürzlichen Kauf – {software} Enterprise-Lizenz",
            ],
            "body": "Sehr geehrte/r {first_name},\n\ndiese E-Mail bestätigt Ihren kürzlichen Kauf:\n\n    Transaktions-ID: {transaction_id}\n    Datum: {date}\n    Beschreibung: {software} Enterprise-Lizenz – Jährliche Verlängerung\n    Betrag: {amount} EUR\n\nWenn Sie diese Transaktion autorisiert haben, ist keine Aktion erforderlich.\n\nWenn Sie diese Abbuchung NICHT autorisiert haben, kontaktieren Sie umgehend unser Support-Team, um eine vollständige Rückerstattung anzufordern:\n\n    Telefon: {callback_number}\n    Erreichbar rund um die Uhr – Geben Sie bei Ihrem Anruf bitte Ihre Transaktions-ID an\n\nBitte beachten Sie: Rückerstattungsanträge müssen innerhalb von 48 Stunden nach der Abbuchung eingereicht werden.\n\n{generic_signature}",
        },
    ],

    # ── Smishing templates ────────────────────────────────────
    "smishing_templates": [
        {
            "id": "account_verify",
            "name": "Kontoverifizierung",
            "messages": [
                "[{company}] Ihr Konto wurde aufgrund verdächtiger Aktivitäten gesperrt. Jetzt verifizieren, um den Zugang wiederherzustellen: {smishing_link}",
                "[{company}] WARNUNG: Ungewöhnliche Anmeldung bei Ihrem {software}-Konto erkannt. Bestätigen Sie Ihre Identität: {smishing_link}",
                "[{company}] Ihre Zugangsdaten laufen heute ab. Sofort aktualisieren, um Unterbrechungen zu vermeiden: {smishing_link}",
            ],
        },
        {
            "id": "package_delivery",
            "name": "Paketzustellung",
            "messages": [
                "[{carrier}] Ihr Paket konnte nicht zugestellt werden. Lieferung hier umplanen: {smishing_link}",
                "[{carrier}] Zustellversuch – Adressbestätigung erforderlich. Hier aktualisieren: {smishing_link}",
                "[{carrier}] Paket #{tracking_id} wird im Lager zurückgehalten. Zollgebühr von {small_fee} EUR zur Freigabe zahlen: {smishing_link}",
            ],
        },
        {
            "id": "mfa_code",
            "name": "MFA / Bestätigungscode",
            "messages": [
                "Ihr {software}-Bestätigungscode lautet {mfa_code}. Falls Sie diesen nicht angefordert haben, sichern Sie Ihr Konto: {smishing_link}",
                "[{company}] Sicherheitscode: {mfa_code}. Falls das nicht Sie waren, melden Sie den unbefugten Zugriff: {smishing_link}",
                "{software}-Anmeldeversuch erkannt. Ihr Einmalcode lautet {mfa_code}. Nicht Sie? Jetzt handeln: {smishing_link}",
            ],
        },
        {
            "id": "payment_alert",
            "name": "Zahlungs- / Bankwarnung",
            "messages": [
                "[{bank_name}] Eine Zahlung von {amount} EUR wurde Ihrem Konto belastet. Falls nicht autorisiert, hier anfechten: {smishing_link}",
                "[{bank_name}] BETRUGSWARNUNG: Ausstehende Transaktion über {amount} EUR. Genehmigen oder ablehnen: {smishing_link}",
                "[{company}] Ihre Gehaltsüberweisung von {amount} EUR ist fehlgeschlagen. Bankverbindung aktualisieren: {smishing_link}",
            ],
        },
    ],

    # ── Quishing templates ────────────────────────────────────
    "quishing_templates": [
        {
            "id": "wifi_portal",
            "name": "Gäste-WLAN-Portal",
            "pretext_text": "GÄSTE-WLAN-ZUGANG\n\nScannen Sie den QR-Code unten, um sich mit dem {company}-Gäste-Netzwerk zu verbinden.\nEine gültige Firmen-E-Mail-Adresse ist zur Authentifizierung erforderlich.\n\nNetzwerk: {company}-Gast\nSupport: {support_email}",
            "delivery_methods": ["Laminiertes Poster in der Empfangshalle", "Tischaufsteller im Konferenzraum", "Aufkleber am Empfangstresen", "Digitale Beschilderung im Wartebereich"],
            "placement_suggestions": ["Empfangshalle und Rezeption", "Konferenzräume", "Wartebereiche für Besucher", "Co-Working-Bereiche", "Kantine und Pausenräume"],
            "objectives": [
                "Firmen-E-Mail-Zugangsdaten über gefälschtes Captive Portal abgreifen",
                "MFA-Tokens über Echtzeit-Phishing-Proxy abfangen",
                "Geräteinformationen von verbindenden Clients erfassen",
                "Man-in-the-Middle-Position im Datenverkehr des Opfers etablieren",
            ],
        },
        {
            "id": "parking_payment",
            "name": "Parkgebührenautomat",
            "pretext_text": "PARKGEBÜHR BEZAHLEN\n\nScannen, um die Parkgebühr zu bezahlen – kontaktlos und schnell.\nAkzeptiert: Visa, Mastercard, Apple Pay\n\nZone: {parking_zone}\nTarif: {parking_rate} EUR/Std.\nParkplatz: {company} Gebäude {department}",
            "delivery_methods": ["Aufkleber über dem echten QR-Code am Parkautomaten", "Flugblatt an Windschutzscheiben im Parkhaus", "Schild am Parkhauseingang", "Gedruckte Karte am Kassenautomaten hinterlegt"],
            "placement_suggestions": ["Firmenparkhaus", "Besucherparkplatz", "Parkautomaten in der Nähe des Zielgebäudes", "Mitarbeiterparkhaus"],
            "objectives": [
                "Zahlungskartendaten über gefälschte Zahlungsseite abgreifen",
                "Persönliche Informationen erfassen (Name, E-Mail, Telefon)",
                "Zahlungsdaten mit Mitarbeiteridentitäten für gezielte Nachverfolgung verknüpfen",
                "Physisches Sicherheitsbewusstsein der Mitarbeitenden im Parkbereich testen",
            ],
        },
        {
            "id": "document_access",
            "name": "Zugriff auf geteiltes Dokument",
            "pretext_text": "VERTRAULICH – NUR FÜR {department}\n\nScannen für Zugriff auf: {document_name}\nGeteilt von: {sender_name}, {sender_title}\n\nDieses Dokument erfordert eine {software}-Authentifizierung.\nLink gültig bis: {deadline}",
            "delivery_methods": ["Gedrucktes Memo auf Schreibtischen oder in Postfächern", "Als Bild in einer Phishing-E-Mail eingebettet", "Am internen schwarzen Brett ausgehängt", "Einer gedruckten Besprechungsagenda beigelegt"],
            "placement_suggestions": ["Abteilungsdrucker-Ablagen", "Gemeinsame Postfächer und Ablagefächer", "Konferenztische vor Besprechungen", "Am Team-schwarzen-Brett ausgehängt", "Im Pausenraum hinterlegt"],
            "objectives": [
                "SSO-/Firmen-Zugangsdaten über gefälschte Anmeldeseite abgreifen",
                "Schadsoftware über gefälschten Dokumenten-Download verbreiten",
                "Sitzungs-Tokens über Phishing-Proxy abfangen",
                "Reaktion der Mitarbeitenden auf physische Social-Engineering-Artefakte testen",
            ],
        },
        {
            "id": "employee_verify",
            "name": "Mitarbeiterausweis-Verifizierung",
            "pretext_text": "HINWEIS: OBLIGATORISCHE AUSWEIS-VERIFIZIERUNG\n\nAlle Mitarbeitenden der Abteilung {department} müssen überprüfen, ob ihr Ausweis aktiv ist.\nScannen Sie den QR-Code unten und melden Sie sich mit Ihren {software}-Zugangsdaten an.\n\nFrist: {deadline}\nBei Nichtbefolgung wird der Zugang vorübergehend gesperrt.\n\nIT-Sicherheit – {company}",
            "delivery_methods": ["An Kartenlesern und Gebäudeeingängen angebracht", "Gedruckter Aushang im Aufzug oder Treppenhaus", "Aushang im Pausenraum", "Von Social Engineer in Sicherheitsuniform verteilt"],
            "placement_suggestions": ["Gebäudeeingang am Kartenleser", "Aufzugvorräume auf jeder Etage", "Pausenräume und Küchen", "Schwarzes Brett der Personalabteilung", "In der Nähe von Türen mit Zugangsbeschränkung"],
            "objectives": [
                "Mitarbeiter-Zugangsdaten durch Dringlichkeit und Autorität abgreifen",
                "Standorte von Kartenlesern und Zugangsverhalten der Mitarbeitenden erfassen",
                "Befolgung ungeprüfter Sicherheitshinweise testen",
                "Namen und Abteilungsinformationen aus Formulareinreichungen sammeln",
            ],
        },
    ],

    # ── Vishing scripts ───────────────────────────────────────
    "vishing_scripts": [
        {
            "id": "it_support_call",
            "name": "IT-Support-Anruf",
            "opening": "[ANRUFER]: Guten Tag, hier spricht {caller_name} vom IT-Support der {company}.\nIch rufe an, weil wir {issue} auf Ihrem Arbeitsplatzrechner festgestellt haben.\nSpreche ich mit {target_name} aus der Abteilung {department}?",
            "escalation": "[ANRUFER]: Ich verstehe Ihre Bedenken vollkommen – wir haben heute schon viele Anfragen dazu erhalten.\nLassen Sie mich Ihr Ticket aufrufen... Ja, ich sehe Ticket #{ticket_number}, erstellt heute um {time} Uhr.\n{manager_name} aus Ihrer Abteilung hat dieses Wartungsfenster genehmigt.\nIch muss nur ein paar Dinge auf Ihrer Seite überprüfen, damit wir das schnell lösen können.\nMöchten Sie, dass ich Sie auf Ihrem Festnetztelefon zurückrufe, oder können wir das jetzt klären?",
            "objective": "ZIEL: Zielperson dazu bringen:\n  - Benutzername und Mitarbeiter-ID zu bestätigen\n  - Eine URL für eine 'Fernwartungssitzung' aufzurufen\n  - Einen Bestätigungscode vorzulesen (abgefangenes MFA-Token)\n  - Den Endpoint-Schutz vorübergehend für das 'Patching' zu deaktivieren\n  - Ein per E-Mail gesendetes Diagnose-Tool (Payload) auszuführen",
            "red_flags_to_avoid": "GLAUBWÜRDIGKEIT BEWAHREN:\n  \u2717 Nicht direkt nach Passwörtern fragen – bitten Sie um ein 'Zurücksetzen über unser Portal'\n  \u2717 Nicht drängen – echter IT-Support ist geduldig und methodisch\n  \u2717 Nicht defensiv werden bei Nachfragen – bieten Sie einen Rückruf zur Verifizierung an\n  \u2717 Keine Fachbegriffe verwenden, die die Zielperson nicht verstehen würde\n  \u2713 Echte Abteilung und Vorgesetztennamen verwenden (aus OSINT)\n  \u2713 Tatsächlich verwendete Software referenzieren\n  \u2713 Gefälschte Anrufer-ID passend zur IT-Abteilung des Unternehmens verwenden\n  \u2713 Rückrufnummer bereitstellen, die auf Ihre Infrastruktur weiterleitet",
        },
        {
            "id": "vendor_support_call",
            "name": "Dienstleister-Support-Anruf",
            "opening": "[ANRUFER]: Guten {time_of_day}, hier spricht {caller_name} vom {vendor_name}-Support.\nIch rufe wegen einer kritischen Sicherheitsmitteilung an, die Ihre {software}-Installation betrifft.\nKönnte ich bitte mit der zuständigen Person für Ihre {software}-Umgebung sprechen?",
            "escalation": "[ANRUFER]: Ich verstehe, dass Sie das verifizieren müssen. Selbstverständlich – genau deshalb rufe ich an.\nWir haben eine Schwachstelle identifiziert – CVE-{cve_year}-{cve_id} – die Ihre Version betrifft.\nMir wurde aufgetragen, Prioritätskunden beim Patchen zu unterstützen, bevor die öffentliche Bekanntmachung am {disclosure_date} erfolgt.\nIch kann Ihnen die offizielle Sicherheitsmitteilung sofort per E-Mail senden, wenn Sie möchten.\nKönnten Sie in der Zwischenzeit bestätigen, welche Version Sie aktuell einsetzen, damit ich prüfen kann, ob Sie betroffen sind?",
            "objective": "ZIEL: Zielperson dazu bringen:\n  - Softwareversion und Installationsdetails zu bestätigen\n  - Fernzugriff für 'Notfall-Patching' zu gewähren\n  - Ein per E-Mail gesendetes 'Verifizierungs-Tool' (Payload) auszuführen\n  - Admin-Zugangsdaten für die 'Patch-Installation' bereitzustellen\n  - Sicherheitskontrollen zu deaktivieren, die das 'Update' blockieren würden",
            "red_flags_to_avoid": "GLAUBWÜRDIGKEIT BEWAHREN:\n  \u2717 Keine gefälschten CVE-Nummern verwenden – aktuelle echte für die Software recherchieren\n  \u2717 Nicht sofort auf Admin-Zugang drängen – schrittweise hinarbeiten\n  \u2717 Nicht vorgeben, das Setup zu kennen, ohne OSINT durchgeführt zu haben\n  \u2713 Tatsächliche Softwareversion referenzieren (aus Stellenanzeigen, Shodan, Wappalyzer)\n  \u2713 Verifizierungs-E-Mail anbieten (von Ihrer gefälschten Domain)\n  \u2713 Bereit sein, die Schwachstelle technisch zu erklären\n  \u2713 Die echten Support-Prozesse des Anbieters kennen, um sie nachzuahmen",
        },
        {
            "id": "executive_impersonation_call",
            "name": "Anruf mit Geschäftsführer-Identität",
            "opening": "[ANRUFER]: {target_name}? Hier spricht {executive_name}.\nIch bin gerade zwischen zwei Besprechungen, aber ich brauche Sie für eine dringende Sache.\nHaben Sie kurz einen Moment?",
            "escalation": "[ANRUFER]: Hören Sie, ich kann jetzt nicht ins Detail gehen, weil\ndies vertraulich ist. Wir schließen gerade ein Geschäft ab und ich brauche, dass {action}\nnoch vor {deadline} veranlasst wird. Ich habe bereits mit {department_head} darüber gesprochen.\nIch schicke Ihnen die Details gleich nach diesem Anruf per E-Mail.\nKönnen Sie sich darum kümmern, sobald Sie die Mail erhalten? Ich verlasse mich auf Sie.",
            "objective": "ZIEL: Zielperson dazu bringen:\n  - Eine Überweisung oder Zahlung zu veranlassen\n  - Vertrauliche Finanzdokumente weiterzugeben\n  - Normale Genehmigungsverfahren aufgrund wahrgenommener Autorität zu umgehen\n  - Zugangsdaten weiterzuleiten oder Systemzugriff zu gewähren\n  - Einen Anhang in der Folge-E-Mail zu öffnen (Payload-Übermittlung)",
            "red_flags_to_avoid": "GLAUBWÜRDIGKEIT BEWAHREN:\n  \u2717 Nicht versuchen ohne Studium der Sprechweise der Führungskraft (YouTube, Podcasts, Bilanzpressekonferenzen)\n  \u2717 Nichts verlangen, was außerhalb der tatsächlichen Befugnisse der Zielperson liegt\n  \u2717 Nicht aggressiv sein – echte Führungskräfte delegieren, sie drohen Untergebenen nicht\n  \u2717 Nicht von unbekannter Nummer anrufen – die echte Nummer der Führungskraft oder Bürodurchwahl fälschen\n  \u2713 Terminplan der Führungskraft recherchieren und echte Ereignisse referenzieren\n  \u2713 Echte laufende Projekte erwähnen (aus LinkedIn, Pressemitteilungen, Geschäftsberichten)\n  \u2713 Kurz halten – Führungskräfte führen keine langen Telefonate\n  \u2713 Nachverfolgung per E-Mail für Payload-Übermittlung nach Vertrauensaufbau am Telefon",
        },
    ],

    # ── Physical pretexts ─────────────────────────────────────
    "physical_pretexts": [
        {
            "id": "hvac_technician",
            "name": "Klimatechniker",
            "appearance": "Firmenpoloshirt oder Arbeitsuniform, Werkzeuggürtel, Klemmbrett mit Arbeitsaufträgen, Schutzbrille, Sicherheitsschuhe",
            "props": [
                "Gedruckter Arbeitsauftrag mit Firmenadresse und Logo der Hausverwaltung",
                "Multimeter und grundlegende Klimatechnik-Werkzeuge",
                "Taschenlampe",
                "Allgemeiner Klimatechnik-Firmenausweis mit Foto",
                "Warnweste",
            ],
            "script": "Ich bin hier für die geplante Klimaanlageninspektion auf Etage {floor}.\nDie Hausverwaltung sollte letzte Woche eine Mitteilung gesendet haben – ich kann Ihnen den Arbeitsauftrag zeigen.\nIch benötige Zugang zum Serverraum, um die Kühleinheiten zu überprüfen.\nWir haben Temperaturwarnungen aus diesem Gebäude erhalten, und niemand möchte,\ndass Geräte am Wochenende überhitzen.",
            "target_areas": ["Serverräume", "Netzwerkschränke", "Technikräume", "Dachzugang", "Kellerinfrastruktur"],
            "objectives": [
                "Ein bösartiges Netzwerkgerät platzieren (LAN Turtle, Raspberry Pi, WiFi Pineapple)",
                "Etiketten und IP-Konfigurationen von Netzwerkgeräten fotografieren",
                "Auf ungesperrte Arbeitsplatzrechner im Serverraum zugreifen",
                "Physische Sicherheitskontrollen erfassen (Kameras, Kartenleser, Schlösser)",
                "Durch gesicherte Türen folgen, während Ausrüstung getragen wird",
            ],
        },
        {
            "id": "fire_inspector",
            "name": "Brandschutzinspektor",
            "appearance": "Business-Casual mit Warnweste, Klemmbrett, Kamera, offiziell aussehender laminierter Ausweis",
            "props": [
                "Brandschutz-Prüfliste (gedruckt, offiziell aussehend)",
                "Kamera zur 'Dokumentation der Feuerlöscher-Standorte'",
                "Ausweis mit allgemeinem Brandschutzfirmen-Namen und Foto",
                "Maßband",
                "Taschenlampe",
            ],
            "script": "Guten Tag, mein Name ist {name} von {fire_safety_company}. Wir führen die jährliche\nPrüfung der Brandschutzanlage für dieses Gebäude durch. Ich benötige Zugang zu\nallen Etagen einschließlich der Sicherheitsbereiche, um die Feuerlöscher-Standorte\nzu überprüfen und die Sprinkleranlage zu inspizieren. Dies ist gemäß Brandschutzverordnung\nvorgeschrieben und die Hausverwaltung hat den Termin eingeplant. Bei wem melde ich mich an?",
            "target_areas": ["Alle Etagen einschließlich Sicherheitsbereiche", "Serverräume (Brandschutzanlagen)", "Treppenhäuser und Notausgänge", "Elektroräume", "Vorstandsetagen"],
            "objectives": [
                "Uneingeschränkten Gebäudezugang mit plausibel klingender Befugnis erlangen",
                "Bürogrundrisse, Kamerastandorte und Kartenleser-Positionen fotografieren",
                "Physische Sicherheitsreaktion auf eine unbekannte Person in Sicherheitsbereichen testen",
                "Zugang zu Serverräumen unter Brandschutzvorwand erlangen",
                "Nicht abgeschlossene Büros und unbeaufsichtigte Arbeitsplatzrechner identifizieren",
            ],
        },
        {
            "id": "delivery_driver",
            "name": "Lieferdienst / Kurier",
            "appearance": "Freizeitkleidung, mit Markenkartons (Amazon, DHL, UPS), ggf. mit Sackkarre für größere Lieferungen",
            "props": [
                "Markenversandkartons (Amazon, DHL oder ähnlich)",
                "Klemmbrett mit gedrucktem Lieferschein mit dem Namen der Zielperson",
                "Sackkarre für große Paketlieferungen",
                "In Paketen versteckte USB-Drop-Geräte",
                "Gedrucktes Versandetikett mit korrekter Firmenadresse",
            ],
            "script": "Lieferung für {target_name} in der Abteilung {department}. Man hat mir gesagt, ich soll\ndirekt an den Schreibtisch liefern – es ist als zerbrechlich und vertraulich gekennzeichnet,\ndaher kann ich es nicht einfach am Empfang abgeben. Ich brauche die persönliche Unterschrift.\nKann mich jemand hinbringen? Ich habe noch weitere Lieferungen und bin etwas\nin Eile.",
            "target_areas": ["Empfang und Eingangshalle", "Poststelle", "Büro oder Schreibtisch der Zielperson", "Gemeinschaftsbereiche und Pausenräume"],
            "objectives": [
                "Empfangssicherheit umgehen, indem seriös aussehende Pakete getragen werden",
                "Zugang zu internen Bürobereichen hinter dem Empfang erlangen",
                "USB-Geräte in Gemeinschaftsbereichen oder auf Schreibtischen hinterlassen",
                "Ausweissysteme, Türcodes und Sicherheitsverfahren beobachten",
                "Ein Paket mit einem bösartigen Gerät an eine bestimmte Person ausliefern",
            ],
        },
        {
            "id": "telecom_technician",
            "name": "Telekommunikationstechniker",
            "appearance": "Marken-Poloshirt oder -Jacke des Anbieters, Werkzeuggürtel, Kabeltester, Laptoptasche, Schutzhelm bei Betreten von Technikbereichen",
            "props": [
                "Uniform oder Poloshirt mit Anbieter-Branding",
                "Kabeltester und Ethernet-Crimpwerkzeug",
                "Laptop mit Netzwerkdiagnose-Software",
                "Gedruckter Arbeitsauftrag mit Verweis auf gemeldete Verbindungsprobleme",
                "Ausweis mit Logo des Telekommunikationsanbieters",
            ],
            "script": "Guten Tag, ich komme von {isp_name}. Wir haben ein Ticket wegen wiederkehrender\nVerbindungsprobleme auf dieser Etage erhalten. Ich muss den Netzwerkschrank überprüfen\nund die Verkabelung bis zum Übergabepunkt verfolgen. Das sollte nicht länger als\n30 Minuten dauern. Kann mir jemand zeigen, wo der Netzwerkschrank ist?\nIch muss außerdem mein Diagnosegerät anschließen, um einige Tests durchzuführen.",
            "target_areas": ["Netzwerkschränke und Patchfelder", "Serverräume", "Übergabepunkt / Telekommunikationsraum", "Verkabelungszugang unter Schreibtischen"],
            "objectives": [
                "Einen Netzwerk-Tap oder ein bösartiges Gerät im Netzwerkschrank platzieren",
                "Ein Gerät an einen aktiven Netzwerkport für Fernzugriff anschließen",
                "Netzwerktopologie und Kabelbeschriftungen fotografieren",
                "Interne Netzwerkinfrastruktur und VLAN-Konfigurationen erfassen",
                "Unverschlüsselten Netzwerkverkehr oder unsichere Protokolle identifizieren",
            ],
        },
    ],

    # ── Psychological principles ──────────────────────────────
    "psych_principles": {
        "authority": {
            "name": "Autorität",
            "description": "Menschen befolgen Anweisungen von wahrgenommenen Autoritätspersonen",
            "application": "Führungskräfte, IT-Administratoren, Prüfer oder Behördenvertreter nachahmen",
            "example": "Der CISO hat mich gebeten, heute alle Konten in Ihrer Abteilung zu überprüfen.",
        },
        "urgency": {
            "name": "Dringlichkeit / Verknappung",
            "description": "Zeitdruck verringert kritisches Denken",
            "application": "Künstliche Fristen setzen, auf laufende Vorfälle oder ablaufende Zugänge verweisen",
            "example": "Ihr Konto wird in 30 Minuten gesperrt, wenn Sie es nicht verifizieren.",
        },
        "social_proof": {
            "name": "Sozialer Beweis",
            "description": "Menschen orientieren sich am Verhalten anderer",
            "application": "Auf Kolleginnen und Kollegen verweisen, die bereits mitgemacht haben",
            "example": "Alle in Ihrer Abteilung haben das bereits erledigt – Sie sind die letzte Person.",
        },
        "reciprocity": {
            "name": "Reziprozität",
            "description": "Menschen fühlen sich verpflichtet, Gefälligkeiten zu erwidern",
            "application": "Der Zielperson zuerst bei etwas helfen, dann die eigentliche Bitte äußern",
            "example": "Ich habe gerade Ihr Druckerproblem behoben. Übrigens, könnten Sie mich in den Serverraum lassen?",
        },
        "liking": {
            "name": "Sympathie / Beziehungsaufbau",
            "description": "Menschen kooperieren eher mit Personen, die ihnen sympathisch sind",
            "application": "Durch Smalltalk und gemeinsame Interessen Vertrauen aufbauen, bevor die Bitte geäußert wird",
            "example": "Sie fahren auch gerne Rad? Apropos, eine kurze Bitte – könnten Sie etwas für mich prüfen?",
        },
        "commitment": {
            "name": "Konsistenz / Bindung",
            "description": "Wer einmal einer kleinen Bitte zugestimmt hat, stimmt auch größeren zu",
            "application": "Mit harmlosen Fragen beginnen und schrittweise zu sensiblen Anfragen eskalieren",
            "example": "Könnten Sie Ihre Abteilung bestätigen? Sehr gut. Und Ihre Position? Perfekt. Könnten Sie nun noch Ihre Mitarbeiter-ID für unsere Unterlagen verifizieren?",
        },
    },

    # ── Fake documents ────────────────────────────────────────
    "fake_documents": [
        "Q4_Finanzbericht_2025.xlsx",
        "Aktualisierung_Passwortrichtlinie.docx",
        "Lieferantenvertrag_Verlaengerungshinweis.pdf",
        "Interne_Sicherheitspruefung_Ergebnisse.pptx",
        "Vertrauliche_Kundenliste.xlsx",
        "Vorstandssitzung_Tagesordnung.docx",
        "IT_Support_Ticket.pdf",
        "Lohnabrechnung_Compliance_Pruefung_2025.xlsx",
        "Kritisches_Software_Patch_Installationsanleitung.docx",
        "Phishing_Simulationsbericht.pdf",
        "Aktualisierung_Incident_Response_Plan.docx",
        "Onboarding_Checkliste_Mitarbeiter.xlsx",
        "Lieferanten_Sicherheitsbewertung.pdf",
        "Jaehrliche_Sicherheitsschulung_Anmeldung.docx",
        "Bonusstruktur_2025.xlsx",
        "Organigramm_2025.pptx",
        "Kuendigungen_Q1_2026.docx",
        "Persoenliche_Leistungsbeurteilung_2025.xlsx",
    ],

    # ── Generator hardcoded strings ───────────────────────────
    "generator": {
        "signature_closing": "Mit freundlichen Grüßen",
        "billing_department": "Rechnungsabteilung, {company}",
        "attachment_prefix": "Anhang",
        "deadlines": ["24 Stunden", "bis Geschäftsschluss heute", "bis 16:00 Uhr heute", "bis Freitag"],
        "deadlines_vishing": ["bis Feierabend", "bis morgen", "bis Mittag"],
        "deadlines_quishing": ["24 Stunden", "bis Geschäftsschluss heute", "bis Freitag 17:00 Uhr"],
        "document_types": ["Dokument", "Tabelle", "Bericht", "Rechnung"],
        "vishing_issues": [
            "ungewöhnliche Anmeldeaktivitäten",
            "einen fehlgeschlagenen Sicherheitsscan",
            "nicht gepatchte Software-Schwachstellen",
            "auffälligen Netzwerkverkehr",
        ],
        "vishing_actions": ["Überweisung", "Datenübertragung", "Passwortzurücksetzung"],
        "time_of_day": ["Morgen", "Tag", "Abend"],
        "preparation_notes_vishing": [
            "LinkedIn der Zielperson auf Rollenbestätigung prüfen (OSINT)",
            "Verifizieren, dass {software} tatsächlich eingesetzt wird (Stellenanzeigen, Shodan prüfen)",
            "Anrufer-ID fälschen, um bekannte Nummern von {company} nachzuahmen",
            "Gefälschte Ticketnummer vorbereiten, falls die Zielperson verifizieren möchte",
        ],
        "preparation_notes_physical": [
            "Geeignete Uniform und Requisiten für die Tarnidentität beschaffen",
            "Arbeitsaufträge mit {company}-Adresse und Logo der Hausverwaltung drucken",
            "Gebäudegrundriss über Google Maps und öffentliche Unterlagen recherchieren",
            "Sicherheitskontrollpunkte, Kartenleser und Kamerapositionen identifizieren",
            "Namen der Hausverwaltung oder des Facility-Managements kennen, falls Rückfragen kommen",
        ],
        "recon_tasks": [
            "Mitarbeitende und Organisationsstruktur von {company} recherchieren",
            "Schlüsselpersonen in den Abteilungen {departments} identifizieren",
            "Interne Netzwerktopologie und kritische Systeme erfassen",
            "Öffentlich erreichbare Dienste und potenzielle Angriffsvektoren identifizieren",
        ],
        "opsec_notes": [
            "VPN und Wegwerf-Infrastruktur für sämtliche Kommunikation verwenden",
            "Ähnlich klingende Domains mindestens 30 Tage im Voraus registrieren",
            "E-Mail-Domain vor dem Phishing mit legitimem Verkehr aufwärmen",
            "Für jede Einsatzphase separate Geräte verwenden",
            "Alles für den Abschlussbericht dokumentieren",
        ],
        "first_names": [
            "Thomas", "Anna", "Stefan", "Claudia", "Martin", "Sabine",
            "Andreas", "Julia", "Markus", "Katharina", "Christian", "Monika",
            "Michael", "Sandra", "Peter", "Nicole", "Tobias", "Susanne",
        ],
        "last_names": [
            "Müller", "Schmidt", "Schneider", "Fischer", "Weber",
            "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann",
            "Koch", "Richter", "Klein", "Wolf", "Neumann",
        ],
        "months": [
            "Januar", "Februar", "März", "April", "Mai", "Juni",
            "Juli", "August", "September", "Oktober", "November", "Dezember",
        ],
    },
}
