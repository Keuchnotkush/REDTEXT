"""Cadenas de texto en español para REDTEXT."""

STRINGS = {
    "meta": {
        "language_name": "Español",
        "language_code": "es",
    },

    # ── Industries ─────────────────────────────────────────────
    "industries": {
        "tech": {
            "name": "Tecnología",
            "departments": ["Ingeniería", "DevOps", "Informática", "Seguridad"],
            "jargon": ["planificación de sprint", "pipeline CI/CD", "integración SSO", "respuesta a incidentes"],
            "pain_points": ["caídas en producción", "rotación de credenciales", "fatiga por guardias"],
        },
        "finance": {
            "name": "Servicios Financieros",
            "departments": ["Contabilidad", "Gestión de Riesgos", "Cumplimiento Normativo", "Informática", "Sala de Operaciones", "Auditoría Interna"],
            "jargon": ["trimestre fiscal", "cumplimiento normativo", "pista de auditoría", "evaluación de riesgos", "revisión KYC", "cumplimiento AML", "auditoría SOX"],
            "pain_points": ["plazos regulatorios", "prevención de fraude", "filtraciones de datos"],
        },
        "healthcare": {
            "name": "Sanidad",
            "departments": ["Historiales Clínicos", "Facturación", "Informática", "Cumplimiento Normativo"],
            "jargon": ["cumplimiento HIPAA", "portal del paciente", "sistema HCE", "flujo de trabajo clínico"],
            "pain_points": ["seguridad de datos de pacientes", "tiempo de inactividad del sistema", "auditorías regulatorias"],
        },
        "government": {
            "name": "Administración Pública",
            "departments": ["Seguridad", "Informática", "Cumplimiento Normativo", "Operaciones"],
            "jargon": ["información clasificada", "habilitación de seguridad", "cumplimiento FISMA", "estándares NIST", "remediación POAM", "autorización para operar"],
            "pain_points": ["clasificación de datos", "problemas de control de acceso", "auditorías de cumplimiento"],
        },
        "education": {
            "name": "Educación",
            "departments": ["Informática", "Admisiones", "Becas y Ayudas", "Servicios al Estudiante"],
            "jargon": ["gestión de cursos", "sistema de información estudiantil", "entorno virtual de aprendizaje", "ciclo de admisiones"],
            "pain_points": ["ataques de phishing a estudiantes", "robo de credenciales", "caídas del sistema durante las matrículas"],
        },
        "manufacturing": {
            "name": "Industria Manufacturera",
            "departments": ["Operaciones", "Informática", "Cadena de Suministro", "Control de Calidad"],
            "jargon": ["línea de producción", "interrupción de la cadena de suministro", "aseguramiento de calidad", "rotación de inventario", "sistema SCADA", "firmware PLC"],
            "pain_points": ["paradas de producción", "ataques a la cadena de suministro", "robo de propiedad intelectual"],
        },
        "retail": {
            "name": "Comercio Minorista",
            "departments": ["Ventas", "Informática", "Atención al Cliente", "Logística"],
            "jargon": ["punto de venta", "gestión de relaciones con clientes", "logística de la cadena de suministro", "rotación de inventario", "cumplimiento PCI DSS"],
            "pain_points": ["filtraciones de tarjetas de pago", "robo de credenciales de empleados", "interrupciones en la cadena de suministro"],
        },
    },

    # ── Personas ───────────────────────────────────────────────
    "personas": {
        "it_support": {
            "name": "Técnico de Soporte Informático",
            "titles": ["Especialista de Soporte Informático", "Analista de Mesa de Ayuda", "Administrador de Sistemas", "Ingeniero de Soporte de Escritorio"],
            "pretexts": [
                "su contraseña caduca en 2 horas - restablézcala ahora a través de este portal para evitar el bloqueo de su cuenta",
                "estamos desplegando un parche de seguridad crítico de {software} - necesitamos que ejecute el instalador adjunto o nos conceda acceso remoto",
                "su cuenta ha sido marcada por actividad de inicio de sesión sospechosa - verifique su identidad para evitar la suspensión",
                "inscripción programada de MFA para su departamento - complete el registro antes de finalizar el día o su acceso será restringido",
                "se requiere actualización de la configuración VPN - descargue el nuevo perfil desde este enlace antes de que se revoque el acceso remoto",
                "su estación de trabajo no superó nuestro último análisis de seguridad - necesitamos acceso remoto para corregirlo antes del próximo ciclo de auditoría",
            ],
        },
        "vendor": {
            "name": "Proveedor Externo",
            "titles": ["Gestor Técnico de Cuentas", "Ingeniero de Éxito del Cliente", "Especialista en Integración"],
            "pretexts": [
                "su licencia de {software} caduca en 48 horas - confirme la renovación de inmediato",
                "se ha descubierto una vulnerabilidad crítica en {software} - necesitamos hacer una copia de seguridad y restablecer su espacio de trabajo",
                "su integración de {software} está generando conflictos en el sistema - necesitamos que transfiera su trabajo para poder resolverlo",
                "parche de seguridad urgente para {software} - requiere su autorización para desplegarlo",
                "su entorno de {software} no superó nuestro análisis de cumplimiento - necesitamos acceso remoto para corregirlo",
            ],
        },
        "executive": {
            "name": "Suplantación de Ejecutivo / Alta Dirección",
            "titles": ["CEO", "CFO", "CTO", "COO", "Vicepresidente de Operaciones"],
            "pretexts": [
                "envíame el informe trimestral de seguridad antes de mi reunión - lo necesito en menos de una hora",
                "gestiona las instrucciones de transferencia adjuntas con discreción - no podemos permitirnos una filtración de información",
                "ya he hablado con {name} sobre esto - necesito que lo tramites de inmediato",
                "diligencia debida de adquisición confidencial - necesito los datos financieros antes del cierre del día",
                "autorización de pago a proveedor - transferencia antes de las 15:00 de hoy, detalles adjuntos",
            ],
        },
        "auditor": {
            "name": "Auditor Externo",
            "titles": ["Director de Auditoría", "Auditor de Cumplimiento", "Especialista en Evaluación de Riesgos", "Evaluador de Seguridad"],
            "pretexts": [
                "estamos realizando una auditoría de cumplimiento RGPD - necesitamos los registros de datos de usuarios almacenados y muestras de registros de datos personales antes de medianoche o la empresa se enfrentará a procedimientos legales por incumplimiento",
                "enviados por ATOS para revisar los registros de acceso y verificar la actividad de cuentas privilegiadas - si no los facilita antes de mañana por la mañana, se registrará como excepción de auditoría y se escalará al consejo de administración",
                "estamos realizando una auditoría de cumplimiento de nóminas - necesitamos todas las hojas de cálculo relevantes de este trimestre antes de mañana por la tarde o se activará una inspección presencial por parte de la autoridad tributaria",
                "auditoría de seguridad anual - necesitamos las configuraciones actuales del cortafuegos y las listas de acceso de administradores en un plazo de 24 horas",
                "seguimiento de la evaluación de riesgos de terceros - la documentación de cumplimiento de su proveedor está vencida y bloquea la renovación de la certificación",
            ],
        },
        "new_employee": {
            "name": "Empleado Nuevo",
            "titles": ["Nuevo Incorporado", "Transferencia Reciente", "Contratista (Primer Día)", "Becario"],
            "pretexts": [
                "soy un nuevo empleado de la sucursal de Redes - necesito que ejecute la prueba de velocidad adjunta para evaluar el rendimiento en las instalaciones",
                "mi tarjeta no me deja entrar en la sala de servidores - mi responsable {name} me pidió que cambiara los cables RJ45 fuera del horario habitual",
                "mi cuenta está en proceso de activación - ¿puede reenviarme el esquema de la infraestructura de red para que pueda empezar a trabajar fuera de horario?",
                "mi responsable {name} me dijo que le pidiera acceso temporal - informática aún no ha configurado mi cuenta",
                "es mi primer día y no puedo acceder a {software} - necesito credenciales temporales para la formación de incorporación de las 14:00",
            ],
        },
        "physical": {
            "name": "Intruso Físico",
            "titles": ["Técnico de Climatización", "Repartidor", "Técnico de Mantenimiento", "Técnico de Telecomunicaciones", "Inspector de Seguridad contra Incendios"],
            "pretexts": [
                "vengo a grabar imágenes de la sala de reuniones para preparar las reformas del cuarto trimestre",
                "traigo una impresora inteligente para Recursos Humanos - el responsable solicitó la entrega directa en la oficina",
                "mantenimiento de las fuentes de alimentación principales - se han notificado cables defectuosos por parte del administrador del edificio que solicitó mi presencia",
                "instalación programada de cableado de red según la orden de trabajo #{wo_number} - la dirección del edificio autorizó el acceso",
                "certificación anual del sistema de extinción de incendios - necesito acceso a todas las plantas, incluida la sala de servidores",
            ],
        },
    },

    # ── Urgency triggers ──────────────────────────────────────
    "urgency_triggers": {
        "low": [
            "Cuando tenga un momento",
            "Por favor, revíselo cuando le venga bien",
            "No dude en echarle un vistazo cuando tenga tiempo",
            "Sin prisa, pero revíselo cuando le sea conveniente",
        ],
        "medium": [
            "Antes del final del día de hoy",
            "Por favor, complételo antes de mañana",
            "Esto debe resolverse antes del fin de semana",
            "Por favor, priorice esta tarea",
        ],
        "high": [
            "Esto debe hacerse en los próximos 30 minutos",
            "Esto requiere atención inmediata",
            "Por favor, resuélvalo en el plazo de una hora",
            "Tarea importante - actúe ahora, por favor",
        ],
        "critical": [
            "Se está produciendo una brecha de seguridad y su cuenta aún no se ha visto comprometida",
            "Según resolución de emergencia del consejo - todos los responsables deben volver a verificar sus credenciales antes de medianoche",
            "Para cumplir con la investigación de la CNMV, revise y envíe los informes de este trimestre de inmediato",
            "Revise y envíe los contratos firmados durante la primera semana del segundo trimestre - se ha detectado un fallo y los clientes amenazan con acciones legales",
        ],
    },

    # ── Seasonal hooks ────────────────────────────────────────
    "seasonal_hooks": {
        "q1": [
            "Inscripción en la formación anual de seguridad",
            "Entrega de documentación fiscal - verificación de certificados de retenciones",
            "Aplicación de la política anual de restablecimiento de contraseñas",
            "Se acerca la fecha límite de los informes financieros del primer trimestre",
        ],
        "q2": [
            "Revisión de cumplimiento de mitad de año",
            "Incorporación de becarios de verano - solicitudes de acceso informático",
            "Avisos de renovación trimestral de licencias de software",
            "Seguimiento de la política de restablecimiento de contraseñas para cuentas creadas en el primer trimestre",
        ],
        "q3": [
            "Preparación previa a la auditoría",
            "Simulacro de recuperación ante desastres",
            "Negociaciones de renovación de contratos con proveedores a punto de vencer",
            "Ciclo de evaluación del desempeño del tercer trimestre - aprobaciones de responsables",
        ],
        "q4": [
            "Calendario festivo - urgente antes del cierre de oficinas",
            "Fecha límite de cumplimiento de fin de año - entregas finales",
            "Informes financieros de cierre de ejercicio",
            "Formación de concienciación en seguridad navideña",
        ],
    },

    # ── Phishing templates ────────────────────────────────────
    "phishing_templates": [
        {
            "id": "credential_harvest",
            "name": "Recolección de Credenciales",
            "subject_lines": [
                "Acción Requerida: Verifique Su Cuenta de {software}",
                "Alerta de Seguridad: Actividad Inusual Detectada en Su Cuenta de {software}",
                "Acción Inmediata Requerida: Confirme los Datos de Su Cuenta de {software}",
                "Aviso de Suspensión de Cuenta de {software} - Verifique Ahora",
            ],
            "body": "Hola {first_name},\n\n{urgency_opening}\n\nPor favor, verifique su identidad haciendo clic en el siguiente enlace:\n\n{phishing_link}\n\nSi no completa esta verificación en un plazo de {deadline}, su acceso a {software} será suspendido temporalmente.\n\n{signature}",
        },
        {
            "id": "malicious_attachment",
            "name": "Adjunto Malicioso",
            "subject_lines": [
                "Importante: {document_name} - Revisión Requerida",
                "Actualización de {department}: Revise el Documento Adjunto",
                "Confidencial: {document_name} - Solo Para Sus Ojos",
                "Acción Requerida: Revise y Firme {document_name}",
            ],
            "body": "Hola {first_name},\n\n{urgency_opening}\n\nAdjunto encontrará el {document_type} que requiere su revisión inmediata. Este documento ha sido aprobado por la dirección de {department} y se está distribuyendo a todo el personal correspondiente.\n\n\U0001f4ce {attachment_note}\n\nPor favor, revíselo, fírmelo y devuélvalo antes de {deadline}. Si tiene problemas para abrir el archivo, habilite las macros cuando se le solicite — esto es necesario según nuestra política de seguridad documental.\n\n{signature}",
        },
        {
            "id": "bec_wire",
            "name": "Compromiso de Correo Empresarial (Fraude por Transferencia)",
            "subject_lines": [
                "Confidencial - Pago Urgente Requerido",
                "Re: Pago a Proveedor - Datos Bancarios Actualizados",
                "Un Favor Rápido - Necesito Que Gestiones Esto Con Discreción",
                "{executive_name} - Solicitud Urgente de Transferencia Bancaria",
            ],
            "body": "Hola {first_name},\n\nNecesito que gestiones algo de forma urgente y discreta. Estamos cerrando un acuerdo confidencial y necesito que se tramite una transferencia bancaria antes del cierre del día.\n\nPor favor, envía lo siguiente:\n\n    Importe: ${amount}\n    Banco: {bank_name}\n    Cuenta: {account_placeholder}\n    Referencia: {reference}\n\nEsto debe completarse antes de {deadline}. No comentes esto con nadie hasta que se cierre el acuerdo — no podemos permitirnos una filtración de información.\n\nYa lo he autorizado con el departamento jurídico. Confírmame cuando esté hecho.\n\n{executive_signature}",
        },
        {
            "id": "callback_phishing",
            "name": "Phishing de Devolución de Llamada (Preparación de Vishing)",
            "subject_lines": [
                "Renovación de Suscripción - Cargo de ${amount} Procesado",
                "Confirmación de Pedido #{invoice_number}",
                "Se Ha Cargado ${amount} en Su Cuenta",
                "Recibo de Compra Reciente - Licencia Empresarial de {software}",
            ],
            "body": "Estimado/a {first_name},\n\nEste correo electrónico confirma su compra reciente:\n\n    ID de Transacción: {transaction_id}\n    Fecha: {date}\n    Descripción: Licencia Empresarial de {software} - Renovación Anual\n    Importe: ${amount}\n\nSi usted autorizó esta transacción, no es necesaria ninguna acción.\n\nSi NO autorizó este cargo, contacte con nuestro equipo de soporte inmediatamente para solicitar un reembolso completo:\n\n    Teléfono: {callback_number}\n    Disponible 24/7 - Indique su ID de Transacción al llamar\n\nTenga en cuenta que las solicitudes de reembolso deben presentarse en un plazo de 48 horas desde el cargo.\n\n{generic_signature}",
        },
        {
            "id": "supply_chain",
            "name": "Compromiso de Proveedor de Cadena de Suministro",
            "subject_lines": [
                "Urgente: parche de seguridad de {software} disponible - Instale antes de {deadline}",
                "[{software}] Actualización crítica requerida - Acción necesaria",
                "Obligatorio: actualización de seguridad del proveedor {software} - Ref.: {reference}",
                "Actualización de integración de {software} - Requiere su autorización",
            ],
            "body": "Hola {first_name},\n\nNos ponemos en contacto para notificarle una actualización de seguridad crítica de {software} que requiere acción inmediata por parte de todos los usuarios autorizados.\n\nComo parte de nuestra colaboración continua con {company}, hemos identificado una vulnerabilidad en el despliegue actual que debe corregirse antes de {deadline}.\n\nPor favor, descargue e instale la actualización utilizando el enlace seguro a continuación:\n\n{phishing_link}\n\nEsta actualización ha sido revisada y aprobada por su departamento de informática. Si experimenta algún problema durante la instalación, contacte con su representante de cuenta de {software}.\n\n{signature}",
        },
        {
            "id": "credential_breach",
            "name": "Notificación de Filtración de Credenciales",
            "subject_lines": [
                "ALERTA DE SEGURIDAD: sus credenciales de {company} encontradas en una filtración de datos",
                "Acción Requerida: restablecimiento de contraseña por filtración de datos de terceros",
                "Urgente: su cuenta de {software} podría estar comprometida",
                "[Equipo de Seguridad] Restablecimiento obligatorio de contraseña - Filtración detectada",
            ],
            "body": "Estimado/a {first_name},\n\nNuestro sistema de monitorización de seguridad ha detectado que las credenciales asociadas a su cuenta de {company} fueron encontradas en una filtración de datos de terceros. NO se trata de una brecha en los sistemas de {company}, pero sus credenciales pueden haber quedado expuestas a través de un servicio externo comprometido.\n\nPara proteger su cuenta, debe restablecer su contraseña de inmediato:\n\n{phishing_link}\n\nSi no restablece su contraseña antes de {deadline}, su cuenta será bloqueada temporalmente como medida de precaución.\n\nComo referencia, los datos comprometidos fueron identificados el {date} e incluyen direcciones de correo electrónico y contraseñas cifradas. Le recomendamos encarecidamente que active la autenticación multifactor tras restablecer su contraseña.\n\n{signature}",
        },
    ],

    # ── Smishing templates ────────────────────────────────────
    "smishing_templates": [
        {
            "id": "account_verify",
            "name": "Verificación de Cuenta",
            "messages": [
                "[{company}] Su cuenta ha sido bloqueada por actividad sospechosa. Verifique ahora para restaurar el acceso: {smishing_link}",
                "[{company}] ALERTA: Inicio de sesión inusual detectado en su cuenta de {software}. Confirme su identidad: {smishing_link}",
                "[{company}] Sus credenciales de acceso caducan hoy. Actualícelas de inmediato para evitar interrupciones: {smishing_link}",
            ],
        },
        {
            "id": "package_delivery",
            "name": "Entrega de Paquete",
            "messages": [
                "[{carrier}] No se ha podido entregar su paquete. Reprograme la entrega: {smishing_link}",
                "[{carrier}] Intento de entrega fallido - se necesita confirmación de dirección. Actualícela aquí: {smishing_link}",
                "[{carrier}] El paquete #{tracking_id} está retenido en el almacén. Pague ${small_fee} de gastos de aduanas para liberarlo: {smishing_link}",
            ],
        },
        {
            "id": "mfa_code",
            "name": "MFA / Código de Verificación",
            "messages": [
                "Su código de verificación de {software} es {mfa_code}. Si no lo solicitó, proteja su cuenta: {smishing_link}",
                "[{company}] Código de seguridad: {mfa_code}. Si no fue usted, informe de un acceso no autorizado: {smishing_link}",
                "Intento de inicio de sesión en {software} detectado. Su código de un solo uso es {mfa_code}. ¿No fue usted? Actúe ahora: {smishing_link}",
            ],
        },
        {
            "id": "payment_alert",
            "name": "Alerta de Pago / Bancaria",
            "messages": [
                "[{bank_name}] Se ha realizado un cargo de ${amount} en su cuenta. Si no lo autorizó, reclame aquí: {smishing_link}",
                "[{bank_name}] ALERTA DE FRAUDE: Transacción pendiente de ${amount}. Apruebe o rechace: {smishing_link}",
                "[{company}] Su ingreso por domiciliación de ${amount} ha fallado. Actualice sus datos bancarios: {smishing_link}",
            ],
        },
    ],

    # ── Quishing templates ────────────────────────────────────
    "quishing_templates": [
        {
            "id": "wifi_portal",
            "name": "Portal Wi-Fi para Invitados",
            "pretext_text": "ACCESO WI-FI PARA INVITADOS\n\nEscanee el código QR a continuación para conectarse a la red de invitados de {company}.\nSe requiere un correo electrónico corporativo válido para la autenticación.\n\nRed: {company}-Invitados\nSoporte: {support_email}",
            "delivery_methods": ["Cartel plastificado en el vestíbulo", "Caballete sobre la mesa de reuniones", "Pegatina cerca del mostrador de recepción", "Cartelería digital en la sala de espera"],
            "placement_suggestions": ["Vestíbulo y zonas de recepción", "Salas de reuniones", "Salas de espera de visitantes", "Espacios de coworking", "Cafetería y salas de descanso"],
            "objectives": [
                "Recolectar credenciales de correo corporativo mediante un portal cautivo falso",
                "Capturar tokens MFA a través de un proxy de phishing en tiempo real",
                "Recopilar información de dispositivos de los clientes que se conectan",
                "Establecer una posición de intermediario en el tráfico de la víctima",
            ],
        },
        {
            "id": "parking_payment",
            "name": "Quiosco de Pago de Aparcamiento",
            "pretext_text": "PAGO DE APARCAMIENTO\n\nEscanee para pagar el aparcamiento — sin contacto y rápido.\nAceptamos: Visa, Mastercard, Apple Pay\n\nZona: {parking_zone}\nTarifa: ${parking_rate}/hora\nAparcamiento: Edificio {company} {department}",
            "delivery_methods": ["Pegatina colocada sobre el QR legítimo del parquímetro", "Folleto en los parabrisas del garaje", "Cartel junto a la entrada del aparcamiento", "Tarjeta impresa dejada en el quiosco de pago"],
            "placement_suggestions": ["Garaje de la empresa", "Aparcamiento de visitantes", "Parquímetros de la calle cerca del edificio objetivo", "Estructura de aparcamiento de empleados"],
            "objectives": [
                "Recolectar datos de tarjetas de pago mediante una página de pago falsa",
                "Recopilar información personal (nombre, correo electrónico, teléfono)",
                "Vincular información de pago con identidades de empleados para seguimiento dirigido",
                "Evaluar la concienciación en seguridad física de los empleados en zonas de aparcamiento",
            ],
        },
        {
            "id": "document_access",
            "name": "Acceso a Documento Compartido",
            "pretext_text": "CONFIDENCIAL — SOLO {department}\n\nEscanee para acceder a: {document_name}\nCompartido por: {sender_name}, {sender_title}\n\nEste documento requiere autenticación de {software}.\nEl enlace caduca: {deadline}",
            "delivery_methods": ["Memorando impreso dejado en escritorios o buzones", "Incrustado en un correo de phishing como imagen", "Publicado en el tablón de anuncios interno", "Incluido en una agenda de reunión impresa"],
            "placement_suggestions": ["Bandejas de las impresoras del departamento", "Buzones y casilleros compartidos", "Mesas de reuniones antes de las reuniones", "Tablones de anuncios del equipo", "Dejado en la sala de descanso"],
            "objectives": [
                "Recolectar credenciales SSO/corporativas mediante una página de inicio de sesión falsa",
                "Distribuir malware a través de una descarga de documento falsa",
                "Capturar tokens de sesión a través de un proxy de phishing",
                "Evaluar la respuesta de los empleados ante artefactos de ingeniería social física",
            ],
        },
        {
            "id": "employee_verify",
            "name": "Verificación de Tarjeta de Empleado",
            "pretext_text": "AVISO: VERIFICACIÓN OBLIGATORIA DE TARJETA\n\nTodos los empleados de {department} deben verificar que su tarjeta está activa.\nEscanee el código QR a continuación e inicie sesión con sus credenciales de {software}.\n\nFecha límite: {deadline}\nEl incumplimiento resultará en la suspensión temporal del acceso.\n\nSeguridad Informática — {company}",
            "delivery_methods": ["Colocado cerca de los lectores de tarjetas y entradas del edificio", "Folleto impreso en el ascensor o la escalera", "Aviso publicado en la sala de descanso", "Entregado en mano por un ingeniero social haciéndose pasar por seguridad"],
            "placement_suggestions": ["Entrada del edificio junto al lector de tarjetas", "Vestíbulos de ascensores en cada planta", "Salas de descanso y cocinas", "Tablón de anuncios de Recursos Humanos", "Cerca de puertas de acceso restringido"],
            "objectives": [
                "Recolectar credenciales de empleados mediante urgencia y autoridad",
                "Mapear las ubicaciones de los lectores de tarjetas y los patrones de acceso de los empleados",
                "Evaluar el cumplimiento ante avisos de seguridad no verificados",
                "Recopilar nombres de empleados e información de departamentos a partir de los envíos de formularios",
            ],
        },
    ],

    # ── Vishing scripts ───────────────────────────────────────
    "vishing_scripts": [
        {
            "id": "it_support_call",
            "name": "Llamada de Soporte Informático",
            "opening": "[LLAMANTE]: Hola, soy {caller_name} del departamento de Soporte Informático de {company}.\nLe llamo porque hemos detectado {issue} en su estación de trabajo.\n¿Es usted {target_name} del departamento de {department}?",
            "escalation": "[LLAMANTE]: Entiendo perfectamente su preocupación - hoy hemos recibido muchas llamadas por esto.\nPermítame buscar su incidencia... Sí, puedo ver que la incidencia #{ticket_number} fue creada a las {time} de hoy.\n{manager_name} de su departamento aprobó esta ventana de mantenimiento.\nSolo necesito verificar algunas cosas de su parte para resolver esto rápidamente.\n¿Prefiere que le devuelva la llamada a su teléfono fijo, o podemos gestionarlo ahora?",
            "objective": "OBJETIVO: Conseguir que el objetivo:\n  - Confirme su nombre de usuario e identificador de empleado\n  - Navegue a una URL para una \"sesión de soporte remoto\"\n  - Lea en voz alta un código de verificación (token MFA interceptado)\n  - Desactive temporalmente la protección del puesto para \"aplicar parches\"\n  - Ejecute una herramienta de diagnóstico (carga maliciosa) enviada por correo electrónico",
            "red_flags_to_avoid": "MANTENER LA CREDIBILIDAD:\n  \u2717 No pida contraseñas directamente - pídale que \"la restablezca a través de nuestro portal\"\n  \u2717 No tenga prisa - el soporte informático real es paciente y metódico\n  \u2717 No se ponga a la defensiva si le cuestionan - ofrezca verificación mediante devolución de llamada\n  \u2717 No use jerga técnica que el objetivo no entendería\n  \u2713 Use el departamento y los nombres de responsables reales del objetivo (obtenidos por OSINT)\n  \u2713 Haga referencia al software que realmente utilizan\n  \u2713 Tenga un identificador de llamadas falsificado que coincida con el departamento de informática de la empresa\n  \u2713 Ofrezca un número de devolución de llamada que redirija a su infraestructura",
        },
        {
            "id": "vendor_support_call",
            "name": "Llamada de Soporte del Proveedor",
            "opening": "[LLAMANTE]: Buenos/as {time_of_day}, soy {caller_name} del soporte de {vendor_name}.\nLe llamo respecto a un aviso de seguridad crítico que afecta a su despliegue de {software}.\n¿Podría hablar con la persona responsable de su entorno de {software}?",
            "escalation": "[LLAMANTE]: Entiendo que necesita verificarlo. Por supuesto - precisamente por seguridad le estoy llamando.\nHemos identificado una vulnerabilidad - CVE-{cve_year}-{cve_id} - que afecta a su versión.\nMe han asignado para ayudar a los clientes prioritarios a aplicar el parche antes de la divulgación pública el {disclosure_date}.\nPuedo enviarle el correo con el aviso oficial ahora mismo si desea verificarlo.\nMientras tanto, ¿puede confirmarme qué versión están ejecutando actualmente para comprobar si están afectados?",
            "objective": "OBJETIVO: Conseguir que el objetivo:\n  - Confirme la versión del software y los detalles de despliegue\n  - Conceda acceso remoto para \"aplicar un parche de emergencia\"\n  - Ejecute una \"herramienta de verificación\" enviada por correo (carga maliciosa)\n  - Proporcione credenciales de administrador para el \"despliegue del parche\"\n  - Desactive controles de seguridad que bloquearían la \"actualización\"",
            "red_flags_to_avoid": "MANTENER LA CREDIBILIDAD:\n  \u2717 No use números CVE falsos - investigue los reales recientes para ese software\n  \u2717 No presione para obtener acceso de administrador inmediato - escale gradualmente\n  \u2717 No pretenda conocer su configuración si no ha hecho OSINT\n  \u2713 Haga referencia a la versión real de su software (obtenida de ofertas de empleo, Shodan, Wappalyzer)\n  \u2713 Ofrezca enviar un correo de verificación (desde su dominio falsificado)\n  \u2713 Esté preparado para explicar la vulnerabilidad técnicamente\n  \u2713 Conozca los procesos reales de soporte del proveedor para poder imitarlos",
        },
        {
            "id": "executive_impersonation_call",
            "name": "Llamada de Suplantación de Ejecutivo",
            "opening": "[LLAMANTE]: ¿{target_name}? Soy {executive_name}.\nEstoy entre reuniones ahora mismo pero necesito que me gestiones algo rápidamente.\n¿Puedes hablar un momento?",
            "escalation": "[LLAMANTE]: Mira, no puedo entrar en todos los detalles ahora porque\nes confidencial. Estamos cerrando un acuerdo y necesito que se tramite {action}\nantes de {deadline}. Ya he hablado con {department_head} al respecto.\nTe voy a enviar los detalles por correo justo después de esta llamada.\n¿Puedes encargarte de esto en cuanto lo recibas? Cuento contigo.",
            "objective": "OBJETIVO: Conseguir que el objetivo:\n  - Tramite una transferencia bancaria o pago\n  - Comparta documentos financieros confidenciales\n  - Omita los flujos de aprobación normales basándose en la autoridad percibida\n  - Reenvíe credenciales o conceda acceso al sistema\n  - Abra un adjunto enviado en el correo de seguimiento (entrega de carga maliciosa)",
            "red_flags_to_avoid": "MANTENER LA CREDIBILIDAD:\n  \u2717 No lo intente sin estudiar los patrones de habla del ejecutivo (YouTube, podcasts, presentaciones de resultados)\n  \u2717 No solicite cosas fuera de la autoridad real del objetivo\n  \u2717 No sea agresivo - los ejecutivos reales delegan, no amenazan a sus subordinados\n  \u2717 No llame desde un número desconocido - falsifique el número real del ejecutivo o de su despacho\n  \u2713 Investigue la agenda del ejecutivo y haga referencia a eventos reales\n  \u2713 Haga referencia a proyectos reales en curso (de LinkedIn, notas de prensa, informes de la CNMV)\n  \u2713 Sea breve - los ejecutivos no tienen conversaciones telefónicas largas\n  \u2713 Cree un seguimiento por correo para la entrega de la carga maliciosa después de establecer confianza por teléfono",
        },
        {
            "id": "password_reset_escalation",
            "name": "Restablecimiento de Contraseña / Escalada de Privilegios",
            "opening": "[LLAMANTE]: Hola, soy {caller_name} del departamento de Gestión de Identidades y Accesos de {company}.\nLe llamo porque su cuenta ha sido marcada para una revisión obligatoria de privilegios.\n¿Es usted {target_name} del departamento de {department}?",
            "escalation": "[LLAMANTE]: Muy bien. La situación es la siguiente — durante nuestra revisión trimestral de accesos,\nhemos detectado que su cuenta dispone de privilegios elevados que necesitan ser recertificados.\nTengo su incidencia aquí mismo — n.º {ticket_number}, abierta por {manager_name}.\nPara completar la recertificación, necesito que verifique su nivel de acceso actual\ny después realizaremos juntos el proceso de restablecimiento.\n¿Puede confirmarme su rol actual y los grupos de administración a los que pertenece?",
            "objective": "OBJETIVO: Conseguir que el objetivo:\n  - Revele su nivel de acceso y pertenencia a grupos de administración\n  - Navegue a un portal IAM falso para la « recertificación »\n  - Introduzca sus credenciales actuales para « verificación previa al restablecimiento »\n  - Apruebe una solicitud MFA falsa (ataque por notificación push)\n  - Revele las credenciales de las cuentas de servicio que gestiona",
            "red_flags_to_avoid": "MANTENER LA CREDIBILIDAD:\n  \u2717 No afirme que la cuenta está comprometida - diga que es una revisión rutinaria\n  \u2717 No pida contraseñas directamente - utilice el « portal de recertificación »\n  \u2717 No apresure el proceso - los equipos IAM son metódicos\n  \u2717 No llame sin conocer las herramientas de administración reales del objetivo\n  \u2713 Conozca los nombres reales de los grupos de administración (obtenidos por OSINT, LinkedIn, ofertas de empleo)\n  \u2713 Haga referencia a las herramientas IAM reales que utiliza la empresa (Azure AD, Okta, CyberArk)\n  \u2713 Tenga un identificador de llamadas falsificado que coincida con la extensión del equipo IAM/Identidad\n  \u2713 Esté preparado para explicar el proceso de recertificación en detalle",
        },
        {
            "id": "service_account_audit",
            "name": "Auditoría de Seguridad de Cuentas de Servicio",
            "opening": "[LLAMANTE]: Buenos/as {time_of_day}, soy {caller_name} del Centro de Operaciones de Seguridad de {company}.\nMe pongo en contacto respecto a la auditoría de cuentas de servicio exigida por cumplimiento normativo.\nNecesito hablar con la persona que gestiona las cuentas de servicio de {software} en el departamento de {department}.",
            "escalation": "[LLAMANTE]: Muy bien, como parte de nuestros requisitos de cumplimiento SOC2/ISO 27001,\nestamos auditando todas las cuentas de servicio de la organización.\n{manager_name} del departamento de {department} fue notificado de esta auditoría hace dos semanas.\nNecesito verificar las cuentas de servicio vinculadas a su despliegue de {software} —\nconcretamente los nombres de cuenta, el calendario de rotación y quién tiene acceso.\n¿Puede buscar esa información? También necesitaré que verifique la validez\nde las credenciales actuales probándolas a través de nuestro portal de auditoría.",
            "objective": "OBJETIVO: Conseguir que el objetivo:\n  - Revele los nombres y configuraciones de las cuentas de servicio\n  - Revele el calendario de rotación de contraseñas y la fecha del último cambio\n  - Pruebe las credenciales a través de un « portal de auditoría » controlado por el atacante\n  - Comparta claves API o tokens utilizados por las cuentas de servicio\n  - Conceda acceso temporal a la consola de gestión de cuentas de servicio",
            "red_flags_to_avoid": "MANTENER LA CREDIBILIDAD:\n  \u2717 No afirme ser de una firma de auditoría externa sin preparación previa\n  \u2717 No solicite todas las cuentas de servicio a la vez - empiece por un solo sistema\n  \u2717 No utilice jerga de cumplimiento normativo que no pueda explicar si le cuestionan\n  \u2717 No omita la referencia a un responsable que aprobó la auditoría\n  \u2713 Investigue los marcos de cumplimiento que la empresa realmente sigue\n  \u2713 Conozca las convenciones de nomenclatura de cuentas de servicio (mensajes de error, ofertas de empleo)\n  \u2713 Haga referencia a plazos reales de auditoría (SOC2 Tipo II es anual)\n  \u2713 Ofrezca enviar la solicitud de auditoría por correo con aspecto oficial como verificación",
        },
    ],

    # ── Physical pretexts ─────────────────────────────────────
    "physical_pretexts": [
        {
            "id": "hvac_technician",
            "name": "Técnico de Climatización",
            "appearance": "Polo o camisa de uniforme con logotipo, cinturón de herramientas, portapapeles con órdenes de trabajo, gafas de seguridad, botas de seguridad con puntera reforzada",
            "props": [
                "Orden de trabajo impresa con la dirección de la empresa objetivo y logotipo de la administración del edificio",
                "Multímetro y herramientas básicas de climatización",
                "Linterna",
                "Identificación genérica de empresa de climatización con foto",
                "Chaleco reflectante",
            ],
            "script": "Vengo para la inspección programada de climatización en la planta {floor}.\nLa administración del edificio debería haber enviado un aviso la semana pasada - puedo mostrarle la orden de trabajo.\nNecesito acceso a la sala de servidores para revisar las unidades de refrigeración.\nHemos estado recibiendo alertas de temperatura de este edificio y lo último\nque queremos es que los equipos se sobrecalienten durante el fin de semana.",
            "target_areas": ["Salas de servidores", "Armarios de red", "Salas de máquinas", "Acceso a la azotea", "Infraestructura del sótano"],
            "objectives": [
                "Instalar un dispositivo de red no autorizado (LAN Turtle, Raspberry Pi, WiFi Pineapple)",
                "Fotografiar etiquetas de equipos de red y configuraciones IP",
                "Acceder a estaciones de trabajo desbloqueadas en la sala de servidores",
                "Mapear controles de seguridad física (cámaras, lectores de tarjetas, cerraduras)",
                "Colarse por puertas protegidas mientras se transporta equipamiento",
            ],
        },
        {
            "id": "fire_inspector",
            "name": "Inspector de Seguridad contra Incendios",
            "appearance": "Ropa informal de negocios con chaleco reflectante, portapapeles, cámara, identificación plastificada de aspecto oficial",
            "props": [
                "Lista de verificación de inspección contra incendios (impresa, de aspecto oficial)",
                "Cámara para 'documentación de la ubicación de los extintores'",
                "Identificación con nombre genérico de empresa de seguridad contra incendios y foto",
                "Cinta métrica",
                "Linterna",
            ],
            "script": "Hola, soy {name} de {fire_safety_company}. Estamos realizando la inspección\nanual del sistema de extinción de incendios de este edificio. Necesitaré acceso a\ntodas las plantas, incluidas las zonas restringidas, para verificar la ubicación de los\nextintores e inspeccionar el sistema de rociadores. Esto es obligatorio según\nla normativa contra incendios y la administración del edificio lo tiene programado.\n¿Con quién debo registrarme?",
            "target_areas": ["Todas las plantas, incluidas las zonas restringidas", "Salas de servidores (sistemas de extinción de incendios)", "Escaleras y salidas de emergencia", "Salas eléctricas", "Plantas de dirección"],
            "objectives": [
                "Obtener acceso sin restricciones al edificio con una autoridad de apariencia legítima",
                "Fotografiar distribuciones de oficinas, posiciones de cámaras de seguridad y ubicación de lectores de tarjetas",
                "Evaluar la respuesta de seguridad física ante una persona desconocida en zonas restringidas",
                "Acceder a salas de servidores bajo pretexto de extinción de incendios",
                "Identificar oficinas sin cerrar y estaciones de trabajo desatendidas",
            ],
        },
        {
            "id": "delivery_driver",
            "name": "Repartidor / Mensajero",
            "appearance": "Ropa informal, transportando cajas con marcas conocidas (Amazon, SEUR, MRW), posiblemente con una carretilla para entregas voluminosas",
            "props": [
                "Cajas de envío con marcas conocidas (Amazon, SEUR o similares)",
                "Portapapeles con albarán de entrega impreso con el nombre del objetivo",
                "Carretilla para paquetes grandes",
                "Dispositivos USB ocultos dentro de los paquetes",
                "Etiqueta de envío impresa con la dirección correcta de la empresa",
            ],
            "script": "Entrega para {target_name} en {department}. Me indicaron que la entregara\ndirectamente en su puesto - está marcado como frágil y confidencial así que no puedo\ndejarlo en recepción. Necesito su firma personal.\n¿Puede alguien acompañarme hasta allí? Tengo más entregas que hacer y voy\nun poco justo de tiempo.",
            "target_areas": ["Recepción y vestíbulo", "Sala de correo", "Oficina o puesto del objetivo", "Zonas comunes y salas de descanso"],
            "objectives": [
                "Eludir la seguridad del vestíbulo transportando paquetes de apariencia legítima",
                "Acceder a zonas de oficina internas más allá de recepción",
                "Dejar dispositivos USB en zonas comunes o escritorios",
                "Observar sistemas de tarjetas, códigos de puertas y procedimientos de seguridad",
                "Entregar un paquete con un dispositivo no autorizado a una persona específica",
            ],
        },
        {
            "id": "telecom_technician",
            "name": "Técnico de Telecomunicaciones / Internet",
            "appearance": "Polo o chaqueta con logotipo de operador, cinturón de herramientas, comprobador de cables, bolsa de portátil, casco si se accede a zonas de servicios",
            "props": [
                "Uniforme o polo con logotipo del operador de telecomunicaciones",
                "Comprobador de cables y herramientas de crimpado de Ethernet",
                "Portátil con software de diagnóstico de red",
                "Orden de trabajo impresa haciendo referencia a problemas de conectividad reportados",
                "Identificación con logotipo de la operadora",
            ],
            "script": "Hola, soy de {isp_name}. Hemos recibido una incidencia sobre problemas\nintermitentes de conectividad en esta planta. Necesito revisar el armario de red\ny trazar el cableado hasta el punto de demarcación. No debería llevar\nmás de 30 minutos. ¿Puede alguien indicarme dónde está el armario de red?\nTambién necesito conectar mi herramienta de diagnóstico para ejecutar algunas pruebas.",
            "target_areas": ["Armarios de red y paneles de cableado", "Salas de servidores", "Punto de demarcación / sala de telecomunicaciones", "Acceso al cableado bajo los escritorios"],
            "objectives": [
                "Instalar una derivación de red o dispositivo no autorizado en el armario de red",
                "Conectar un dispositivo a un puerto de red activo para acceso remoto",
                "Fotografiar la topología de red y etiquetas de cables",
                "Mapear la infraestructura de red interna y configuraciones de VLAN",
                "Identificar tráfico de red sin cifrar o protocolos inseguros",
            ],
        },
        {
            "id": "copier_technician",
            "name": "Técnico de Fotocopiadora / Impresora",
            "appearance": "Ropa informal de negocios con polo del proveedor, maletín de herramientas con ruedas, bolsa de portátil, identificación con logo del fabricante de impresoras",
            "props": [
                "Polo con marca del proveedor (Canon, Ricoh, Xerox o HP)",
                "Maletín de herramientas con ruedas con herramientas básicas y cartuchos de tóner",
                "Portátil para 'diagnósticos y actualizaciones de firmware'",
                "Parte de servicio impreso con referencia al modelo de impresora y planta específicos",
                "Identificación con logo y foto de la empresa proveedora",
            ],
            "script": "Hola, soy {name} de {printer_vendor}. Hemos recibido una alerta automática\nindicando que la {printer_model} de la planta {floor} necesita mantenimiento y una\nactualización de firmware. Necesitaré acceder directamente a la impresora y conectar\nmi portátil para la actualización del firmware. También tengo que comprobar la\nconectividad de red en el lado del servidor de impresión. Esto debería llevar\nunas 45 minutos. Es posible que necesite visitar impresoras en otras plantas\ntambién — nuestro sistema ha marcado varias más para la misma actualización.",
            "target_areas": ["Plantas de oficinas con impresoras en red", "Salas de impresión y centros de reprografía", "Armarios de red donde se conectan los servidores de impresión", "Plantas de dirección (objetivos de alto valor)", "Múltiples plantas para 'mantenimiento por lotes'"],
            "objectives": [
                "Instalar un implante de red a través de la conexión Ethernet de la impresora",
                "Acceder a múltiples plantas bajo la cobertura de 'mantenimiento por lotes'",
                "Recolectar credenciales del servidor de impresión o de trabajos de impresión en caché",
                "Instalar un dispositivo no autorizado en puertos de red cercanos a las impresoras",
                "Mapear la distribución de oficinas e identificar estaciones de trabajo de alto valor durante el recorrido por las plantas",
            ],
        },
        {
            "id": "it_asset_inventory",
            "name": "Especialista en Inventario de Activos Informáticos",
            "appearance": "Ropa informal de negocios, portapapeles con hoja de seguimiento de activos, escáner de códigos de barras, portátil, tarjeta del departamento de informática en cordón",
            "props": [
                "Portapapeles con hoja de inventario de activos impresa mostrando registros existentes",
                "Escáner de códigos de barras USB para 'escanear etiquetas de activos'",
                "Portátil con 'software de gestión de activos' abierto",
                "Cámara para 'fotografiar etiquetas de activos y números de serie'",
                "Identificación del departamento de informática (genérica o falsificada)",
            ],
            "script": "Hola, soy {name} de Gestión de Activos Informáticos. Estamos realizando el inventario\nanual de hardware para {company} — cada estación de trabajo, monitor y dispositivo de red\ndebe ser verificado. Necesito escanear físicamente la etiqueta de activo de cada máquina\ny verificar que el número de serie coincide con nuestros registros. Hoy iré puesto por puesto\nen la planta {floor}. La administración del edificio y su jefe de departamento fueron\nnotificados la semana pasada. Intentaré ser rápido y no molestar a nadie.",
            "target_areas": ["Cada puesto y estación de trabajo de la planta objetivo", "Salas de servidores y armarios de red", "Salas de reuniones con equipos audiovisuales", "Almacenes con hardware de repuesto", "Despachos de dirección"],
            "objectives": [
                "Obtener acceso prolongado y sistemático a cada estación de trabajo del edificio",
                "Fotografiar pantallas, notas adhesivas y pizarras para recolectar credenciales",
                "Conectar dispositivos USB (keyloggers, implantes) mientras se 'escanean etiquetas de activos'",
                "Mapear toda la topología de red documentando los dispositivos conectados",
                "Identificar estaciones de trabajo desatendidas y desbloqueadas para su explotación",
            ],
        },
    ],

    # ── Psychological principles ──────────────────────────────
    "psych_principles": {
        "authority": {
            "name": "Autoridad",
            "description": "Las personas obedecen a las figuras que perciben como autoridad",
            "application": "Suplantar a ejecutivos, administradores de informática, auditores o fuerzas del orden",
            "example": "El CISO me ha pedido que verifique todas las cuentas de su departamento hoy.",
        },
        "urgency": {
            "name": "Urgencia / Escasez",
            "description": "La presión temporal reduce el pensamiento crítico",
            "application": "Crear plazos artificiales, hacer referencia a incidentes activos o accesos a punto de caducar",
            "example": "Su cuenta se bloqueará en 30 minutos si no la verifica.",
        },
        "social_proof": {
            "name": "Prueba Social",
            "description": "Las personas siguen lo que hacen los demás",
            "application": "Hacer referencia a compañeros que ya han cumplido",
            "example": "Todos en su departamento ya lo han completado - usted es el último.",
        },
        "reciprocity": {
            "name": "Reciprocidad",
            "description": "Las personas sienten la obligación de devolver favores",
            "application": "Ayudar al objetivo con algo primero y luego hacer la solicitud real",
            "example": "Acabo de arreglarle el problema de la impresora. Por cierto, ¿puede abrirme la puerta de la sala de servidores con su tarjeta?",
        },
        "liking": {
            "name": "Simpatía / Empatía",
            "description": "Las personas acceden más fácilmente a las peticiones de quienes les caen bien",
            "application": "Generar confianza mediante conversación informal y puntos en común antes de hacer solicitudes",
            "example": "¿A ti también te gusta el ciclismo? Bueno, un favor rápido - ¿puedes comprobar algo por mí?",
        },
        "commitment": {
            "name": "Compromiso / Coherencia",
            "description": "Una vez que alguien acepta algo pequeño, aceptará peticiones mayores",
            "application": "Comenzar con preguntas inocentes y escalar gradualmente hacia solicitudes sensibles",
            "example": "¿Puede confirmarme su departamento? Perfecto. ¿Y su puesto? Muy bien. Ahora, ¿puede verificar su identificador de empleado para nuestros registros?",
        },
    },

    # ── Fake documents ────────────────────────────────────────
    "fake_documents": [
        "Revision_Financiera_Q4_2025.xlsx",
        "Actualizacion_Politica_Contrasenas_Empleados.docx",
        "Aviso_Renovacion_Contrato_Proveedor.pdf",
        "Hallazgos_Auditoria_Seguridad_Interna.pptx",
        "Lista_Confidencial_Clientes.xlsx",
        "Agenda_Reunion_Consejo_Directivo.docx",
        "Incidencia_Soporte_Informatico.pdf",
        "Auditoria_Cumplimiento_Nominas_RRHH_2025.xlsx",
        "Instrucciones_Despliegue_Parche_Critico.docx",
        "Informe_Simulacion_Phishing.pdf",
        "Actualizacion_Plan_Respuesta_Incidentes.docx",
        "Lista_Verificacion_Incorporacion_Empleados.xlsx",
        "Evaluacion_Seguridad_Proveedores.pdf",
        "Inscripcion_Formacion_Seguridad_Anual.docx",
        "Estructura_Bonificaciones_2025.xlsx",
        "Organigrama_2025.pptx",
        "Notificaciones_Despido_Q1_2026.docx",
        "Evaluacion_Desempeno_Personal_2025.xlsx",
    ],

    # ── Generator hardcoded strings ───────────────────────────
    "generator": {
        "signature_closing": "Atentamente,",
        "billing_department": "Departamento de Facturación, {company}",
        "attachment_prefix": "Adjunto",
        "deadlines": ["24 horas", "antes del cierre del día", "16:00 de hoy", "viernes"],
        "deadlines_vishing": ["antes de finalizar el día", "mañana", "antes del mediodía"],
        "deadlines_quishing": ["24 horas", "antes del cierre del día", "viernes a las 17:00"],
        "document_types": ["documento", "hoja de cálculo", "informe", "factura"],
        "vishing_issues": [
            "actividad de inicio de sesión inusual",
            "un análisis de seguridad fallido",
            "vulnerabilidades de software sin parchear",
            "tráfico de red anómalo",
        ],
        "vishing_actions": ["transferencia bancaria", "transferencia de datos", "restablecimiento de contraseña"],
        "time_of_day": ["días", "tardes", "noches"],
        "preparation_notes_vishing": [
            "Realizar OSINT en el LinkedIn del objetivo para confirmar su puesto",
            "Verificar que {software} se utiliza realmente (comprobar ofertas de empleo, Shodan)",
            "Falsificar el identificador de llamadas para que coincida con los números conocidos de {company}",
            "Preparar un número de incidencia falso por si quieren verificar",
        ],
        "preparation_notes_physical": [
            "Conseguir el uniforme y atrezo apropiados para la identidad de cobertura",
            "Imprimir órdenes de trabajo con la dirección de {company} y el logotipo de la administración del edificio",
            "Investigar la distribución del edificio a través de Google Maps y registros públicos",
            "Identificar puntos de control de seguridad, lectores de tarjetas y posiciones de cámaras",
            "Conocer el nombre del responsable de administración del edificio o instalaciones por si le cuestionan",
        ],
        "recon_tasks": [
            "Investigar a los empleados de {company} y la estructura organizativa",
            "Identificar personal clave en los departamentos de {departments}",
            "Mapear la topología de red interna y los sistemas críticos",
            "Identificar servicios expuestos a Internet y posibles vectores de ataque",
        ],
        "opsec_notes": [
            "Usar VPN e infraestructura desechable para todas las comunicaciones",
            "Registrar dominios similares al menos 30 días antes",
            "Calentar el dominio de correo con tráfico legítimo antes del phishing",
            "Usar dispositivos separados para cada fase de la operación",
            "Documentar todo para el informe final",
        ],
        "first_names": [
            "Carlos", "María", "Alejandro", "Ana", "Javier", "Carmen",
            "Miguel", "Laura", "Pablo", "Lucía", "Fernando", "Elena",
            "Antonio", "Isabel", "Sergio", "Raquel", "Diego", "Patricia",
        ],
        "last_names": [
            "García", "Rodríguez", "Martínez", "López", "Fernández",
            "González", "Sánchez", "Pérez", "Gómez", "Díaz",
            "Hernández", "Ruiz", "Moreno", "Muñoz", "Álvarez",
        ],
        "months": [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
        ],
    },
}
