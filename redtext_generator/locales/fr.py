"""French locale strings for REDTEXT."""

STRINGS = {
    "meta": {
        "language_name": "Français",
        "language_code": "fr",
    },

    # ── Industries ─────────────────────────────────────────────
    "industries": {
        "tech": {
            "name": "Technologie",
            "departments": ["Ingénierie", "DevOps", "Informatique", "Sécurité"],
            "jargon": ["planification de sprint", "pipeline CI/CD", "intégration SSO", "réponse aux incidents"],
            "pain_points": ["pannes en production", "rotation des identifiants", "fatigue des astreintes"],
        },
        "finance": {
            "name": "Services financiers",
            "departments": ["Comptabilité", "Gestion des risques", "Conformité", "Informatique", "Salle des marchés", "Audit interne"],
            "jargon": ["trimestre fiscal", "conformité réglementaire", "piste d'audit", "évaluation des risques", "revue KYC", "conformité LCB-FT", "audit SOX"],
            "pain_points": ["échéances réglementaires", "prévention de la fraude", "violations de données"],
        },
        "healthcare": {
            "name": "Santé",
            "departments": ["Dossiers médicaux", "Facturation", "Informatique", "Conformité"],
            "jargon": ["conformité HDS", "portail patient", "système DPI", "flux de travail clinique"],
            "pain_points": ["sécurité des données patients", "indisponibilité du système", "audits réglementaires"],
        },
        "government": {
            "name": "Administration publique",
            "departments": ["Sécurité", "Informatique", "Conformité", "Opérations"],
            "jargon": ["informations classifiées", "habilitation de sécurité", "conformité RGS", "normes ANSSI", "remédiation PSSI", "homologation de sécurité"],
            "pain_points": ["classification des données", "problèmes de contrôle d'accès", "audits de conformité"],
        },
        "education": {
            "name": "Éducation",
            "departments": ["Informatique", "Admissions", "Bourses et aides", "Vie étudiante"],
            "jargon": ["gestion des cours", "système d'information étudiant", "environnement numérique de travail", "campagne d'admission"],
            "pain_points": ["attaques de phishing ciblant les étudiants", "vol d'identifiants", "pannes système pendant les inscriptions"],
        },
        "manufacturing": {
            "name": "Industrie manufacturière",
            "departments": ["Opérations", "Informatique", "Chaîne d'approvisionnement", "Contrôle qualité"],
            "jargon": ["ligne de production", "perturbation de la chaîne d'approvisionnement", "assurance qualité", "rotation des stocks", "système SCADA", "firmware PLC"],
            "pain_points": ["arrêt de production", "attaques sur la chaîne d'approvisionnement", "vol de propriété intellectuelle"],
        },
        "retail": {
            "name": "Commerce de détail",
            "departments": ["Ventes", "Informatique", "Service client", "Logistique"],
            "jargon": ["point de vente", "gestion de la relation client", "logistique de la chaîne d'approvisionnement", "rotation des stocks", "conformité PCI DSS"],
            "pain_points": ["violations de données de paiement", "vol d'identifiants des employés", "perturbations de la chaîne d'approvisionnement"],
        },
    },

    # ── Personas ───────────────────────────────────────────────
    "personas": {
        "it_support": {
            "name": "Technicien support informatique",
            "titles": ["Spécialiste support informatique", "Analyste helpdesk", "Administrateur systèmes", "Technicien support poste de travail"],
            "pretexts": [
                "votre mot de passe expire dans 2 heures - réinitialisez-le via ce portail pour éviter le verrouillage de votre compte",
                "déploiement d'un correctif de sécurité critique pour {software} - nous avons besoin que vous exécutiez le programme d'installation ci-joint ou que vous accordiez un accès à distance",
                "votre compte a été signalé pour une activité de connexion suspecte - vérifiez votre identité pour éviter la suspension",
                "inscription MFA planifiée pour votre service - complétez l'enregistrement avant la fin de journée ou votre accès sera restreint",
                "mise à jour de la configuration VPN requise - téléchargez le nouveau profil depuis ce lien avant la révocation de votre accès distant",
                "votre poste de travail a échoué à notre dernière analyse de sécurité - nous avons besoin d'un accès à distance pour remédier au problème avant le prochain cycle d'audit",
            ],
        },
        "vendor": {
            "name": "Fournisseur tiers",
            "titles": ["Responsable de compte technique", "Ingénieur réussite client", "Spécialiste intégration"],
            "pretexts": [
                "votre licence {software} expire dans 48 heures - confirmez le renouvellement immédiatement",
                "vulnérabilité critique découverte dans {software} - nous devons sauvegarder et réinitialiser votre espace de travail",
                "votre intégration {software} provoque des conflits système - nous avons besoin que vous transfériez vos données pour que nous puissions résoudre le problème",
                "correctif de sécurité urgent pour {software} - votre autorisation est requise pour le déploiement",
                "votre environnement {software} a échoué à notre analyse de conformité - nous avons besoin d'un accès à distance pour remédier au problème",
            ],
        },
        "executive": {
            "name": "Usurpation d'identité de dirigeant",
            "titles": ["PDG", "DAF", "DSI", "DG", "VP des opérations"],
            "pretexts": [
                "envoyez-moi le rapport de sécurité trimestriel avant ma réunion - j'en ai besoin dans l'heure",
                "traitez les instructions de virement ci-jointes discrètement - nous ne pouvons pas nous permettre une fuite d'information",
                "j'ai déjà parlé avec {name} à ce sujet - j'ai besoin que vous traitiez cela immédiatement",
                "due diligence confidentielle pour une acquisition - j'ai besoin des données financières avant la fin de journée",
                "autorisation de paiement fournisseur - virement à effectuer avant 15h aujourd'hui, détails en pièce jointe",
            ],
        },
        "auditor": {
            "name": "Auditeur externe",
            "titles": ["Responsable d'audit", "Auditeur de conformité", "Spécialiste en évaluation des risques", "Évaluateur de sécurité"],
            "pretexts": [
                "réalisation d'un audit de conformité RGPD - nous avons besoin des registres de données utilisateurs et des journaux PII d'ici minuit, sous peine de poursuites judiciaires pour non-conformité",
                "mandaté par l'ANSSI pour examiner les journaux d'accès et vérifier l'activité des comptes à privilèges - tout manquement d'ici demain matin sera signalé comme exception d'audit et remonté au conseil d'administration",
                "réalisation d'un audit de conformité de la paie - nous avons besoin de tous les tableurs pertinents de ce trimestre d'ici demain après-midi, faute de quoi un contrôle sur site sera déclenché par l'URSSAF",
                "audit de sécurité annuel - nous avons besoin des configurations de pare-feu actuelles et des listes d'accès administrateur dans les 24 heures",
                "suivi de l'évaluation des risques tiers - votre documentation de conformité fournisseur est en retard et bloque le renouvellement de la certification",
            ],
        },
        "new_employee": {
            "name": "Nouvel employé",
            "titles": ["Nouvelle recrue", "Mutation récente", "Prestataire (premier jour)", "Stagiaire"],
            "pretexts": [
                "nouvelle recrue de l'agence réseau - j'ai besoin que vous exécutiez le test de débit ci-joint pour évaluer les performances sur site",
                "mon badge ne me permet pas d'accéder à la salle serveur - mon responsable {name} m'a demandé de changer les câbles RJ45 après les heures de bureau",
                "mon compte est en cours d'activation - pouvez-vous me transmettre le plan d'infrastructure réseau pour que je puisse commencer à travailler en dehors des heures",
                "mon responsable {name} m'a dit de vous demander un accès temporaire - le service informatique n'a pas encore configuré mon compte",
                "premier jour et je n'arrive pas à accéder à {software} - j'ai besoin d'identifiants temporaires pour la formation d'intégration à 14h",
            ],
        },
        "physical": {
            "name": "Intrus physique",
            "titles": ["Technicien CVC", "Livreur", "Agent de maintenance", "Technicien télécom", "Inspecteur sécurité incendie"],
            "pretexts": [
                "je suis ici pour filmer la salle de réunion afin de préparer les rénovations du T4",
                "livraison d'une imprimante connectée pour les RH - le responsable a demandé une livraison directe au bureau",
                "maintenance des alimentations électriques principales - des câbles défectueux ont été signalés par l'administrateur du site qui m'a demandé d'intervenir",
                "installation de câbles réseau programmée selon le bon de travail n°{wo_number} - la gestion du bâtiment a autorisé l'accès",
                "certification annuelle du système d'extinction incendie - j'ai besoin d'accéder à tous les étages, y compris la salle serveur",
            ],
        },
    },

    # ── Urgency triggers ──────────────────────────────────────
    "urgency_triggers": {
        "low": [
            "Quand vous aurez un moment",
            "Merci de consulter ceci à votre convenance",
            "N'hésitez pas à y jeter un œil quand vous aurez le temps",
            "Rien d'urgent, mais merci de consulter quand cela vous convient",
        ],
        "medium": [
            "D'ici la fin de journée",
            "Merci de compléter ceci d'ici demain",
            "Ceci doit être traité avant le week-end",
            "Merci de prioriser cette tâche",
        ],
        "high": [
            "Ceci doit être fait dans les 30 prochaines minutes",
            "Ceci requiert une attention immédiate",
            "Merci de traiter ceci dans l'heure",
            "Tâche importante - merci d'agir maintenant",
        ],
        "critical": [
            "Une brèche de sécurité est en cours et votre compte n'a pas encore été compromis",
            "Conformément à la résolution d'urgence du conseil - tous les responsables doivent re-vérifier leurs identifiants avant minuit",
            "Pour répondre à l'enquête de l'AMF, consultez et soumettez les rapports de ce trimestre immédiatement",
            "Consultez et envoyez les contrats signés durant la première semaine du T2 - une anomalie a été détectée et les clients menacent d'engager des poursuites",
        ],
    },

    # ── Seasonal hooks ────────────────────────────────────────
    "seasonal_hooks": {
        "q1": [
            "Inscription à la formation annuelle de sensibilisation à la sécurité",
            "Soumission des documents fiscaux - vérification des déclarations annuelles",
            "Application de la politique de réinitialisation annuelle des mots de passe",
            "Échéance de reporting financier du T1 approchante",
        ],
        "q2": [
            "Revue de conformité semestrielle",
            "Intégration des stagiaires d'été - demandes d'accès informatique",
            "Avis de renouvellement trimestriel des licences logicielles",
            "Suivi de la politique de réinitialisation des mots de passe pour les comptes créés au T1",
        ],
        "q3": [
            "Préparation pré-audit",
            "Exercice de reprise après sinistre",
            "Discussions de renouvellement des contrats fournisseurs arrivant à échéance",
            "Cycle d'évaluation de performance T3 - validations des responsables",
        ],
        "q4": [
            "Planning des fêtes - urgent avant la fermeture des bureaux",
            "Échéance de conformité de fin d'année - soumissions finales",
            "Reporting financier de fin d'année",
            "Formation de sensibilisation à la sécurité des fêtes de fin d'année",
        ],
    },

    # ── Phishing templates ────────────────────────────────────
    "phishing_templates": [
        {
            "id": "credential_harvest",
            "name": "Collecte d'identifiants",
            "subject_lines": [
                "Action requise : vérifiez votre compte {software}",
                "Alerte de sécurité : activité inhabituelle détectée sur votre compte {software}",
                "Action immédiate requise : confirmez les informations de votre compte {software}",
                "Avertissement de suspension de compte {software} - Vérifiez maintenant",
            ],
            "body": "Bonjour {first_name},\n\n{urgency_opening}\n\nMerci de vérifier votre identité en cliquant sur le lien ci-dessous :\n\n{phishing_link}\n\nSi vous ne complétez pas cette vérification dans un délai de {deadline}, votre accès à {software} sera temporairement suspendu.\n\n{signature}",
        },
        {
            "id": "malicious_attachment",
            "name": "Pièce jointe malveillante",
            "subject_lines": [
                "Important : {document_name} - Examen requis",
                "Mise à jour {department} : merci de consulter le document ci-joint",
                "Confidentiel : {document_name} - À votre seule attention",
                "Action requise : consultez et signez {document_name}",
            ],
            "body": "Bonjour {first_name},\n\n{urgency_opening}\n\nVeuillez trouver ci-joint le {document_type} nécessitant votre examen immédiat. Ce document a été approuvé par la direction du service {department} et est distribué à l'ensemble du personnel concerné.\n\n\U0001f4ce {attachment_note}\n\nMerci de le consulter, le signer et le retourner avant le {deadline}. Si vous rencontrez des difficultés pour ouvrir le fichier, veuillez activer les macros lorsque cela vous est demandé — ceci est requis par notre politique de sécurité documentaire.\n\n{signature}",
        },
        {
            "id": "bec_wire",
            "name": "Compromission de messagerie d'entreprise (fraude au virement)",
            "subject_lines": [
                "Confidentiel - Paiement urgent requis",
                "Re : Paiement fournisseur - Coordonnées bancaires mises à jour",
                "Petit service - À traiter discrètement",
                "{executive_name} - Demande de virement urgent",
            ],
            "body": "Bonjour {first_name},\n\nJ'ai besoin que vous traitiez quelque chose de manière urgente et discrète. Nous sommes en train de finaliser un accord confidentiel et j'ai besoin qu'un virement soit effectué avant la fin de journée.\n\nMerci d'effectuer le virement suivant :\n\n    Montant : {amount} €\n    Banque : {bank_name}\n    Compte : {account_placeholder}\n    Référence : {reference}\n\nCeci doit être finalisé avant le {deadline}. N'en parlez à personne tant que l'accord n'est pas finalisé — nous ne pouvons pas nous permettre une fuite d'information.\n\nJ'ai déjà obtenu la validation du service juridique. Confirmez une fois que c'est fait.\n\n{executive_signature}",
        },
        {
            "id": "callback_phishing",
            "name": "Phishing par rappel téléphonique (préparation au vishing)",
            "subject_lines": [
                "Renouvellement d'abonnement - Débit de {amount} € effectué",
                "Confirmation de commande n°{invoice_number}",
                "Votre compte a été débité de {amount} €",
                "Reçu de votre achat récent - Licence entreprise {software}",
            ],
            "body": "Cher/Chère {first_name},\n\nCe courriel confirme votre achat récent :\n\n    Identifiant de transaction : {transaction_id}\n    Date : {date}\n    Description : Licence entreprise {software} - Renouvellement annuel\n    Montant : {amount} €\n\nSi vous avez autorisé cette transaction, aucune action n'est requise.\n\nSi vous N'AVEZ PAS autorisé ce débit, contactez notre équipe d'assistance immédiatement pour demander un remboursement intégral :\n\n    Téléphone : {callback_number}\n    Disponible 24h/24 7j/7 - Mentionnez votre identifiant de transaction lors de l'appel\n\nVeuillez noter : les demandes de remboursement doivent être soumises dans les 48 heures suivant le débit.\n\n{generic_signature}",
        },
    ],

    # ── Smishing templates ────────────────────────────────────
    "smishing_templates": [
        {
            "id": "account_verify",
            "name": "Vérification de compte",
            "messages": [
                "[{company}] Votre compte a été verrouillé en raison d'une activité suspecte. Vérifiez maintenant pour rétablir l'accès : {smishing_link}",
                "[{company}] ALERTE : connexion inhabituelle détectée sur votre compte {software}. Confirmez votre identité : {smishing_link}",
                "[{company}] Vos identifiants expirent aujourd'hui. Mettez-les à jour immédiatement pour éviter toute interruption : {smishing_link}",
            ],
        },
        {
            "id": "package_delivery",
            "name": "Livraison de colis",
            "messages": [
                "[{carrier}] Votre colis n'a pas pu être livré. Reprogrammez la livraison : {smishing_link}",
                "[{carrier}] Tentative de livraison - confirmation d'adresse nécessaire. Mettez à jour ici : {smishing_link}",
                "[{carrier}] Colis n°{tracking_id} retenu en entrepôt. Payez {small_fee} € de frais de douane pour le libérer : {smishing_link}",
            ],
        },
        {
            "id": "mfa_code",
            "name": "Code MFA / vérification",
            "messages": [
                "Votre code de vérification {software} est {mfa_code}. Si vous n'avez pas fait cette demande, sécurisez votre compte : {smishing_link}",
                "[{company}] Code de sécurité : {mfa_code}. Si ce n'était pas vous, signalez un accès non autorisé : {smishing_link}",
                "Tentative de connexion {software} détectée. Votre code à usage unique est {mfa_code}. Ce n'est pas vous ? Agissez maintenant : {smishing_link}",
            ],
        },
        {
            "id": "payment_alert",
            "name": "Alerte de paiement / bancaire",
            "messages": [
                "[{bank_name}] Un paiement de {amount} € a été débité de votre compte. Si non autorisé, contestez : {smishing_link}",
                "[{bank_name}] ALERTE FRAUDE : transaction en attente de {amount} €. Approuvez ou refusez : {smishing_link}",
                "[{company}] Votre virement de {amount} € a échoué. Mettez à jour vos coordonnées bancaires : {smishing_link}",
            ],
        },
    ],

    # ── Quishing templates ────────────────────────────────────
    "quishing_templates": [
        {
            "id": "wifi_portal",
            "name": "Portail Wi-Fi invité",
            "pretext_text": "ACCÈS WI-FI INVITÉ\n\nScannez le QR code ci-dessous pour vous connecter au réseau invité de {company}.\nUne adresse e-mail professionnelle valide est requise pour l'authentification.\n\nRéseau : {company}-Invité\nAssistance : {support_email}",
            "delivery_methods": ["Affiche plastifiée dans le hall", "Chevalet sur la table de conférence", "Autocollant près de l'accueil", "Affichage numérique en salle d'attente"],
            "placement_suggestions": ["Hall et zones d'accueil", "Salles de réunion", "Salles d'attente visiteurs", "Espaces de coworking", "Cafétéria et salles de pause"],
            "objectives": [
                "Collecter les identifiants professionnels via un faux portail captif",
                "Capturer les jetons MFA via un proxy de phishing en temps réel",
                "Collecter les informations des appareils se connectant",
                "Établir une position d'interception sur le trafic de la victime",
            ],
        },
        {
            "id": "parking_payment",
            "name": "Borne de paiement parking",
            "pretext_text": "PAIEMENT PARKING\n\nScannez pour payer votre stationnement — sans contact et rapide.\nAcceptés : Visa, Mastercard, Apple Pay\n\nZone : {parking_zone}\nTarif : {parking_rate} €/h\nParking : {company} Bâtiment {department}",
            "delivery_methods": ["Autocollant placé par-dessus le QR légitime sur l'horodateur", "Flyer sur les pare-brise dans le parking", "Panneau affiché près de l'entrée du parking", "Carte imprimée laissée sur la borne de paiement"],
            "placement_suggestions": ["Parking de l'entreprise", "Parking visiteurs", "Horodateurs à proximité du bâtiment cible", "Parking couvert des employés"],
            "objectives": [
                "Collecter les données de carte bancaire via une fausse page de paiement",
                "Collecter des informations personnelles (nom, e-mail, téléphone)",
                "Associer les informations de paiement aux identités des employés pour un suivi ciblé",
                "Tester la sensibilisation à la sécurité physique des employés dans les zones de stationnement",
            ],
        },
        {
            "id": "document_access",
            "name": "Accès à un document partagé",
            "pretext_text": "CONFIDENTIEL — RÉSERVÉ AU SERVICE {department}\n\nScannez pour accéder à : {document_name}\nPartagé par : {sender_name}, {sender_title}\n\nCe document nécessite une authentification {software}.\nLien expirant le : {deadline}",
            "delivery_methods": ["Note imprimée laissée sur les bureaux ou dans les casiers", "Intégrée dans un e-mail de phishing sous forme d'image", "Affichée sur le tableau d'information interne", "Incluse dans l'ordre du jour imprimé d'une réunion"],
            "placement_suggestions": ["Bacs à papier des imprimantes du service", "Casiers et boîtes aux lettres partagés", "Tables de salle de réunion avant les réunions", "Affichée sur les tableaux d'information d'équipe", "Laissée en salle de pause"],
            "objectives": [
                "Collecter les identifiants SSO/d'entreprise via une fausse page de connexion",
                "Distribuer un malware via un faux téléchargement de document",
                "Capturer les jetons de session via un proxy de phishing",
                "Tester la réaction des employés face à des artefacts d'ingénierie sociale physique",
            ],
        },
        {
            "id": "employee_verify",
            "name": "Vérification de badge employé",
            "pretext_text": "AVIS : VÉRIFICATION DE BADGE OBLIGATOIRE\n\nTous les employés du service {department} doivent vérifier que leur badge est actif.\nScannez le QR code ci-dessous et connectez-vous avec vos identifiants {software}.\n\nDate limite : {deadline}\nLe non-respect entraînera une suspension temporaire de l'accès.\n\nSécurité informatique — {company}",
            "delivery_methods": ["Affiché près des lecteurs de badges et des entrées du bâtiment", "Flyer imprimé dans l'ascenseur ou la cage d'escalier", "Avis affiché en salle de pause", "Distribué par un ingénieur social se faisant passer pour un agent de sécurité"],
            "placement_suggestions": ["Entrée du bâtiment près du lecteur de badge", "Halls d'ascenseur à chaque étage", "Salles de pause et cuisines", "Tableau d'affichage RH", "Près des portes à accès restreint"],
            "objectives": [
                "Collecter les identifiants des employés en exploitant l'urgence et l'autorité",
                "Cartographier les emplacements des lecteurs de badges et les habitudes d'accès des employés",
                "Tester la conformité face à des avis de sécurité non vérifiés",
                "Collecter les noms des employés et les informations de service à partir des soumissions de formulaire",
            ],
        },
    ],

    # ── Vishing scripts ───────────────────────────────────────
    "vishing_scripts": [
        {
            "id": "it_support_call",
            "name": "Appel du support informatique",
            "opening": "[APPELANT] : Bonjour, ici {caller_name} du support informatique de {company}.\nJe vous contacte car nous avons détecté {issue} sur votre poste de travail.\nSuis-je bien en ligne avec {target_name} du service {department} ?",
            "escalation": "[APPELANT] : Je comprends tout à fait votre préoccupation - nous avons reçu beaucoup d'appels à ce sujet aujourd'hui.\nLaissez-moi consulter votre ticket... Oui, je vois que le ticket n°{ticket_number} a été créé à {time} aujourd'hui.\n{manager_name} de votre service a approuvé cette fenêtre de maintenance.\nJ'ai juste besoin de vérifier quelques éléments de votre côté pour résoudre cela rapidement.\nPréférez-vous que je vous rappelle sur votre poste fixe, ou peut-on s'en occuper maintenant ?",
            "objective": "OBJECTIF : Amener la cible à :\n  - Confirmer son nom d'utilisateur et son numéro d'employé\n  - Naviguer vers une URL pour une « session d'assistance à distance »\n  - Lire à voix haute un code de vérification (jeton MFA intercepté)\n  - Désactiver temporairement la protection du poste pour la « mise à jour »\n  - Exécuter un outil de diagnostic (charge utile) envoyé par e-mail",
            "red_flags_to_avoid": "MAINTENIR LA CRÉDIBILITÉ :\n  \u2717 Ne demandez pas directement les mots de passe - demandez de « réinitialiser via notre portail »\n  \u2717 Ne précipitez pas - le vrai support informatique est patient et méthodique\n  \u2717 Ne soyez pas sur la défensive si on vous questionne - proposez de laisser vérifier via un rappel\n  \u2717 N'utilisez pas de jargon technique que la cible ne comprendrait pas\n  \u2713 Utilisez le vrai nom du service et du responsable de la cible (issu de l'OSINT)\n  \u2713 Faites référence aux vrais logiciels qu'ils utilisent\n  \u2713 Ayez un identifiant d'appelant usurpé correspondant au service informatique de l'entreprise\n  \u2713 Proposez un numéro de rappel qui redirige vers votre infrastructure",
        },
        {
            "id": "vendor_support_call",
            "name": "Appel du support éditeur",
            "opening": "[APPELANT] : Bon{time_of_day}, ici {caller_name} du support {vendor_name}.\nJe vous appelle au sujet d'un avis de sécurité critique affectant votre déploiement {software}.\nPuis-je parler à la personne qui gère votre environnement {software} ?",
            "escalation": "[APPELANT] : Je comprends que vous devez vérifier. Absolument — la sécurité est justement la raison de mon appel.\nNous avons identifié une vulnérabilité — CVE-{cve_year}-{cve_id} — qui affecte votre version.\nJ'ai été chargé d'aider les clients prioritaires à appliquer le correctif avant la divulgation publique du {disclosure_date}.\nJe peux vous envoyer l'avis officiel par e-mail tout de suite si vous souhaitez vérifier.\nEn attendant, pouvez-vous me confirmer quelle version vous utilisez actuellement afin que je vérifie si vous êtes concerné ?",
            "objective": "OBJECTIF : Amener la cible à :\n  - Confirmer la version du logiciel et les détails du déploiement\n  - Accorder un accès à distance pour une « mise à jour d'urgence »\n  - Exécuter un « outil de vérification » envoyé par e-mail (charge utile)\n  - Fournir les identifiants administrateur pour le « déploiement du correctif »\n  - Désactiver les contrôles de sécurité qui bloqueraient la « mise à jour »",
            "red_flags_to_avoid": "MAINTENIR LA CRÉDIBILITÉ :\n  \u2717 N'utilisez pas de faux numéros CVE - recherchez de vrais CVE récents pour le logiciel\n  \u2717 Ne faites pas pression pour un accès administrateur immédiat - montez en puissance progressivement\n  \u2717 Ne prétendez pas connaître leur installation si vous n'avez pas fait d'OSINT\n  \u2713 Faites référence à leur version réelle du logiciel (offres d'emploi, Shodan, Wappalyzer)\n  \u2713 Proposez d'envoyer un e-mail de vérification (depuis votre domaine usurpé)\n  \u2713 Soyez prêt à expliquer la vulnérabilité techniquement\n  \u2713 Connaissez les vrais processus de support de l'éditeur pour les imiter",
        },
        {
            "id": "executive_impersonation_call",
            "name": "Appel d'usurpation d'identité de dirigeant",
            "opening": "[APPELANT] : {target_name} ? C'est {executive_name}.\nJe suis entre deux réunions là mais j'ai besoin que vous gériez quelque chose rapidement.\nVous avez une minute ?",
            "escalation": "[APPELANT] : Écoutez, je ne peux pas entrer dans tous les détails maintenant parce que\nc'est confidentiel. Nous sommes en train de finaliser un accord et j'ai besoin que {action} soit traité\navant {deadline}. J'en ai déjà parlé avec {department_head}.\nJe vais vous envoyer les détails par e-mail juste après cet appel.\nVous pouvez vous en occuper dès réception ? Je compte sur vous.",
            "objective": "OBJECTIF : Amener la cible à :\n  - Effectuer un virement ou un paiement\n  - Partager des documents financiers sensibles\n  - Contourner les circuits d'approbation normaux en raison de l'autorité perçue\n  - Transmettre des identifiants ou accorder un accès au système\n  - Ouvrir une pièce jointe envoyée dans l'e-mail de suivi (livraison de la charge utile)",
            "red_flags_to_avoid": "MAINTENIR LA CRÉDIBILITÉ :\n  \u2717 Ne tentez pas sans avoir étudié les habitudes d'expression du dirigeant (YouTube, podcasts, assemblées générales)\n  \u2717 Ne demandez pas des choses hors du périmètre réel d'autorité de la cible\n  \u2717 Ne soyez pas agressif - les vrais dirigeants délèguent, ils ne menacent pas leurs subordonnés\n  \u2717 N'appelez pas depuis un numéro inconnu - usurpez le vrai numéro du dirigeant ou de son bureau\n  \u2713 Renseignez-vous sur l'agenda du dirigeant et faites référence à de vrais événements\n  \u2713 Faites référence à de vrais projets en cours (LinkedIn, communiqués de presse, publications AMF)\n  \u2713 Restez bref - les dirigeants ne font pas de longues conversations téléphoniques\n  \u2713 Créez un suivi par e-mail pour la livraison de la charge utile après avoir établi la confiance par téléphone",
        },
    ],

    # ── Physical pretexts ─────────────────────────────────────
    "physical_pretexts": [
        {
            "id": "hvac_technician",
            "name": "Technicien CVC",
            "appearance": "Polo ou uniforme de l'entreprise, ceinture à outils, bloc-notes avec bons de travail, lunettes de sécurité, chaussures de sécurité",
            "props": [
                "Bon de travail imprimé avec l'adresse de l'entreprise cible et le logo de la gestion du bâtiment",
                "Multimètre et outils CVC de base",
                "Lampe torche",
                "Badge générique d'entreprise CVC avec photo",
                "Gilet haute visibilité",
            ],
            "script": "Je suis ici pour l'inspection CVC programmée à l'étage {floor}.\nLa gestion du bâtiment devrait avoir envoyé un avis la semaine dernière - je peux vous montrer le bon de travail.\nJ'ai besoin d'accéder à la salle serveur pour vérifier les unités de refroidissement.\nNous avons reçu des alertes de température provenant de ce bâtiment et personne ne veut\nque des équipements surchauffent pendant le week-end.",
            "target_areas": ["Salles serveur", "Locaux réseau", "Locaux techniques", "Accès au toit", "Infrastructure en sous-sol"],
            "objectives": [
                "Installer un dispositif réseau pirate (LAN Turtle, Raspberry Pi, WiFi Pineapple)",
                "Photographier les étiquettes des équipements réseau et les configurations IP",
                "Accéder aux postes de travail non verrouillés en salle serveur",
                "Cartographier les contrôles de sécurité physique (caméras, lecteurs de badges, serrures)",
                "S'introduire par talonnage à travers les portes sécurisées en portant du matériel",
            ],
        },
        {
            "id": "fire_inspector",
            "name": "Inspecteur sécurité incendie",
            "appearance": "Tenue professionnelle avec gilet haute visibilité, bloc-notes, appareil photo, badge plastifié d'apparence officielle",
            "props": [
                "Liste de contrôle d'inspection incendie (imprimée, aspect officiel)",
                "Appareil photo pour la « documentation de l'emplacement des extincteurs »",
                "Badge avec nom générique d'entreprise de sécurité incendie et photo",
                "Mètre ruban",
                "Lampe torche",
            ],
            "script": "Bonjour, je suis {name} de {fire_safety_company}. Nous effectuons l'inspection\nannuelle du système d'extinction incendie pour ce bâtiment. J'aurai besoin d'accéder\nà tous les étages y compris les zones restreintes pour vérifier l'emplacement des extincteurs\net inspecter le système de sprinklers. C'est une obligation réglementaire et\nla gestion du bâtiment l'a inscrit au planning. À qui dois-je me présenter ?",
            "target_areas": ["Tous les étages y compris les zones restreintes", "Salles serveur (systèmes d'extinction incendie)", "Cages d'escalier et issues de secours", "Locaux électriques", "Étages de la direction"],
            "objectives": [
                "Obtenir un accès illimité au bâtiment avec un prétexte d'autorité légitime",
                "Photographier les plans des bureaux, les positions des caméras de sécurité et les emplacements des lecteurs de badges",
                "Tester la réaction de la sécurité physique face à une personne inconnue dans des zones restreintes",
                "Accéder aux salles serveur sous prétexte d'extinction incendie",
                "Identifier les bureaux non verrouillés et les postes de travail sans surveillance",
            ],
        },
        {
            "id": "delivery_driver",
            "name": "Livreur / Coursier",
            "appearance": "Tenue décontractée, transportant des colis de marque (Amazon, Chronopost, Colissimo), éventuellement avec un diable pour les grosses livraisons",
            "props": [
                "Colis avec marquage de transporteur (Amazon, Chronopost ou similaire)",
                "Bloc-notes avec bordereau de livraison imprimé portant le nom de la cible",
                "Diable pour les livraisons volumineuses",
                "Clés USB piégées dissimulées dans les colis",
                "Étiquette d'expédition imprimée avec l'adresse correcte de l'entreprise",
            ],
            "script": "Livraison pour {target_name} au service {department}. On m'a dit de livrer\ndirectement à son bureau - c'est marqué fragile et confidentiel donc je ne peux pas\njuste le laisser à l'accueil. J'ai besoin de sa signature en personne.\nQuelqu'un peut m'accompagner ? J'ai d'autres livraisons à faire donc je suis\nun peu pressé.",
            "target_areas": ["Accueil et hall d'entrée", "Salle du courrier", "Bureau ou poste de travail de la cible", "Espaces communs et salles de pause"],
            "objectives": [
                "Contourner la sécurité du hall en portant des colis d'apparence légitime",
                "Accéder aux zones de bureaux internes au-delà de l'accueil",
                "Déposer des clés USB dans les espaces communs ou sur les bureaux",
                "Observer les systèmes de badges, les codes de portes et les procédures de sécurité",
                "Livrer un colis contenant un dispositif pirate à une personne spécifique",
            ],
        },
        {
            "id": "telecom_technician",
            "name": "Technicien télécom / Internet",
            "appearance": "Polo ou veste aux couleurs du FAI, ceinture à outils, testeur de câble, sacoche pour ordinateur portable, casque de chantier si accès aux locaux techniques",
            "props": [
                "Uniforme ou polo aux couleurs du FAI",
                "Testeur de câble et outils de sertissage Ethernet",
                "Ordinateur portable avec logiciel de diagnostic réseau",
                "Bon de travail imprimé faisant référence à des problèmes de connectivité signalés",
                "Badge avec logo du FAI",
            ],
            "script": "Bonjour, je suis de chez {isp_name}. Nous avons reçu un ticket concernant des\nproblèmes de connectivité intermittents sur cet étage. J'ai besoin de vérifier le\nlocal réseau et de tracer le câblage jusqu'au point de démarcation. Cela ne devrait\npas prendre plus de 30 minutes. Quelqu'un peut me montrer où se trouve le local\nréseau ? J'ai aussi besoin de brancher mon outil de diagnostic pour effectuer quelques tests.",
            "target_areas": ["Locaux réseau et panneaux de brassage", "Salles serveur", "Point de démarcation / local télécom", "Accès au câblage sous les bureaux"],
            "objectives": [
                "Installer un dispositif d'écoute réseau ou un équipement pirate dans le local réseau",
                "Connecter un dispositif à un port réseau actif pour un accès à distance",
                "Photographier la topologie réseau et les étiquettes de câbles",
                "Cartographier l'infrastructure réseau interne et les configurations VLAN",
                "Identifier le trafic réseau non chiffré ou les protocoles non sécurisés",
            ],
        },
    ],

    # ── Psychological principles ──────────────────────────────
    "psych_principles": {
        "authority": {
            "name": "Autorité",
            "description": "Les gens obéissent aux figures d'autorité perçues",
            "application": "Usurper l'identité de dirigeants, d'administrateurs informatiques, d'auditeurs ou de forces de l'ordre",
            "example": "Le RSSI m'a demandé de vérifier tous les comptes de votre service aujourd'hui.",
        },
        "urgency": {
            "name": "Urgence / Rareté",
            "description": "La pression temporelle réduit l'esprit critique",
            "application": "Créer des échéances artificielles, faire référence à des incidents en cours ou à des accès expirant",
            "example": "Votre compte sera verrouillé dans 30 minutes si vous ne procédez pas à la vérification.",
        },
        "social_proof": {
            "name": "Preuve sociale",
            "description": "Les gens suivent ce que font les autres",
            "application": "Faire référence aux collègues qui ont déjà obtempéré",
            "example": "Tout le monde dans votre service a déjà complété cette vérification - vous êtes le dernier.",
        },
        "reciprocity": {
            "name": "Réciprocité",
            "description": "Les gens se sentent obligés de rendre les faveurs",
            "application": "Aider la cible avec quelque chose d'abord, puis formuler la vraie demande",
            "example": "Je viens de réparer votre imprimante. Au fait, pourriez-vous me badger pour accéder à la salle serveur ?",
        },
        "liking": {
            "name": "Sympathie / Rapport",
            "description": "Les gens obéissent davantage à ceux qu'ils apprécient",
            "application": "Établir un rapport par la conversation informelle et les points communs avant de formuler des demandes",
            "example": "Ah vous êtes aussi passionné de vélo ? Sinon, un petit service - vous pouvez vérifier quelque chose pour moi ?",
        },
        "commitment": {
            "name": "Engagement / Cohérence",
            "description": "Une fois que quelqu'un accepte quelque chose de mineur, il acceptera des demandes plus importantes",
            "application": "Commencer par des questions anodines et monter progressivement vers des demandes sensibles",
            "example": "Pouvez-vous me confirmer votre service ? Parfait. Et votre poste ? Très bien. Maintenant, pourriez-vous vérifier votre numéro d'employé pour nos dossiers ?",
        },
    },

    # ── Fake documents ────────────────────────────────────────
    "fake_documents": [
        "Revue_Financiere_T4_2025.xlsx",
        "Mise_a_Jour_Politique_Mots_de_Passe.docx",
        "Avis_Renouvellement_Contrat_Fournisseur.pdf",
        "Conclusions_Audit_Securite_Interne.pptx",
        "Liste_Clients_Confidentielle.xlsx",
        "Ordre_du_Jour_Reunion_Direction.docx",
        "Ticket_Support_Informatique.pdf",
        "Audit_Conformite_Paie_RH_2025.xlsx",
        "Instructions_Deploiement_Correctif_Critique.docx",
        "Rapport_Simulation_Phishing.pdf",
        "Mise_a_Jour_Plan_Reponse_Incidents.docx",
        "Checklist_Integration_Nouvel_Employe.xlsx",
        "Evaluation_Securite_Fournisseur.pdf",
        "Inscription_Formation_Securite_Annuelle.docx",
        "Grille_Primes_2025.xlsx",
        "Organigramme_2025.pptx",
        "Notifications_Licenciement_T1_2026.docx",
        "Evaluation_Performance_Individuelle_2025.xlsx",
    ],

    # ── Generator hardcoded strings ───────────────────────────
    "generator": {
        "signature_closing": "Cordialement,",
        "billing_department": "Service facturation, {company}",
        "attachment_prefix": "Pièce jointe",
        "deadlines": ["24 heures", "fin de journée", "16h00 aujourd'hui", "vendredi"],
        "deadlines_vishing": ["fin de journée", "demain", "avant midi"],
        "deadlines_quishing": ["24 heures", "fin de journée", "vendredi à 17h00"],
        "document_types": ["document", "tableur", "rapport", "facture"],
        "vishing_issues": [
            "une activité de connexion inhabituelle",
            "un échec d'analyse de sécurité",
            "des vulnérabilités logicielles non corrigées",
            "un trafic réseau anormal",
        ],
        "vishing_actions": ["virement bancaire", "transfert de données", "réinitialisation de mot de passe"],
        "time_of_day": ["jour", "jour", "soir"],
        "preparation_notes_vishing": [
            "Effectuer de l'OSINT sur le LinkedIn de la cible pour confirmer son poste",
            "Vérifier que {software} est réellement utilisé (offres d'emploi, Shodan)",
            "Usurper l'identifiant d'appelant pour correspondre aux numéros connus de {company}",
            "Préparer un faux numéro de ticket au cas où ils voudraient vérifier",
        ],
        "preparation_notes_physical": [
            "Se procurer l'uniforme et les accessoires appropriés pour l'identité de couverture",
            "Imprimer des bons de travail avec l'adresse de {company} et le logo de la gestion du bâtiment",
            "Étudier le plan du bâtiment via Google Maps et les registres publics",
            "Identifier les points de contrôle de sécurité, les lecteurs de badges et les positions des caméras",
            "Connaître le nom du responsable de la gestion du bâtiment ou des installations en cas de questionnement",
        ],
        "recon_tasks": [
            "Rechercher les employés et la structure organisationnelle de {company}",
            "Identifier le personnel clé dans les services {departments}",
            "Cartographier la topologie réseau interne et les systèmes critiques",
            "Identifier les services exposés publiquement et les vecteurs d'attaque potentiels",
        ],
        "opsec_notes": [
            "Utiliser un VPN et une infrastructure jetable pour toutes les communications",
            "Enregistrer les domaines ressemblants au moins 30 jours à l'avance",
            "Préchauffer le domaine e-mail avec du trafic légitime avant le phishing",
            "Utiliser des appareils distincts pour chaque phase de l'engagement",
            "Tout documenter pour le rapport final",
        ],
        "first_names": [
            "Jean", "Marie", "Pierre", "Sophie", "Thomas", "Nathalie",
            "Nicolas", "Isabelle", "Laurent", "Céline", "Philippe", "Valérie",
            "François", "Caroline", "Julien", "Stéphanie", "Antoine", "Aurélie",
        ],
        "last_names": [
            "Martin", "Bernard", "Dubois", "Moreau", "Laurent",
            "Simon", "Michel", "Lefèvre", "Leroy", "Roux",
            "David", "Bertrand", "Morel", "Fournier", "Girard",
        ],
        "months": [
            "janvier", "février", "mars", "avril", "mai", "juin",
            "juillet", "août", "septembre", "octobre", "novembre", "décembre",
        ],
    },
}
