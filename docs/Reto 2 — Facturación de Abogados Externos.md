# Reto 2 — Facturación de Abogados Externos

### Controles y Rediseño del Proceso · Analítica Legal — SURA

El proceso actual depende de correos electrónicos, planillas Excel y validaciones manuales entre auxiliares, aprendices, abogados internos y ajustadores. Los principales riesgos son pérdida de facturas o soportes, pagos duplicados o errados, demoras en autorización, falta de trazabilidad y baja capacidad analítica. La propuesta se construye desde una mirada de **riesgo y control**: pocos controles, simples, con responsable claro y con evidencia auditable.

---

## a) Cinco controles concretos

Cada control se describe con el riesgo que mitiga, la mecánica de operación, el responsable y la evidencia que deja en el sistema.

#### Control 1 — Punto único de recepción con radicado automático

| | |
|---|---|
| **Riesgo que mitiga** | Pérdida de facturas, recepciones por correos personales, falta de trazabilidad inicial. |
| **Cómo opera** | Formulario digital único (SharePoint / Power Apps) como única vía de radicación. El sistema asigna un consecutivo `FAC-AAAA-NNNNN`, registra fecha y hora, y notifica al auxiliar asignado. No se reciben facturas por correo. |
| **Responsable** | Auxiliar administrativo (operación) · Líder de proceso (gobierno). |
| **Evidencia** | Log de radicación con sello de tiempo y archivo adjunto inmutable. |

#### Control 2 — Validación automática de campos mínimos contra CaseTracking

| | |
|---|---|
| **Riesgo que mitiga** | Facturas incompletas, devoluciones repetidas, captura manual de datos por el auxiliar. |
| **Cómo opera** | Al radicar, el formulario consulta CaseTracking y bloquea el envío si faltan o no coinciden: número de siniestro, radicado judicial, centro de costos, abogado asignado o soportes obligatorios. El abogado externo solo puede enviar cuando los campos cumplen. |
| **Responsable** | Sistema (validación automática) · Analista (excepciones). |
| **Evidencia** | Checklist de validación adjunto al radicado. |

#### Control 3 — Doble aprobación y segregación de funciones

| | |
|---|---|
| **Riesgo que mitiga** | Pagos no autorizados, autorización por persona distinta al responsable del caso, fraude. |
| **Cómo opera** | La factura avanza a "Pagable" únicamente con dos aprobaciones digitales: (i) abogado interno responsable del caso, valida pertinencia técnica; (ii) coordinador o líder de área, valida monto y centro de costos sobre un umbral definido. Quien radica no puede aprobar. |
| **Responsable** | Abogado interno + coordinador. |
| **Evidencia** | Registro de aprobador, fecha y comentario en el flujo. |

#### Control 4 — Conciliación previa al pago (anti-duplicidad y antifraude)

| | |
|---|---|
| **Riesgo que mitiga** | Pago duplicado, pago a NIT incorrecto, pago sobre factura ya legalizada. |
| **Cómo opera** | Antes de enviar al ajustador, el sistema cruza automáticamente NIT del proveedor + número de factura + siniestro contra el histórico. Si encuentra coincidencia previa, alerta y bloquea el avance. Verifica también que el proveedor esté activo en el maestro. |
| **Responsable** | Sistema (regla) · Analista (resolución de alertas). |
| **Evidencia** | Reporte de excepciones diario. |

#### Control 5 — Tablero de seguimiento y alertas por SLA

| | |
|---|---|
| **Riesgo que mitiga** | Demoras, facturas estancadas, falta de visibilidad para tomar decisiones. |
| **Cómo opera** | Tablero Power BI con el estado de cada factura (Radicada → Validada → Autorizada → Legalizada → Pagada), días en cada etapa y facturas vencidas frente a SLA pactado. Alerta automática al responsable cuando una factura supera el SLA de su etapa. |
| **Responsable** | Líder de proceso (gobierno) · Gerencia (decisión). |
| **Evidencia** | Tablero en línea + correo de alerta con bitácora. |

> **Cobertura:** C1 y C2 previenen pérdidas e ineficiencias en origen · C3 asegura autorización y trazabilidad · C4 garantiza integridad del pago · C5 habilita analítica y cumplimiento oportuno.

---

## b) Flujo propuesto

### Etapas, roles y controles

| # | Etapa | Responsable | Qué hace | Control |
|:-:|-------|-------------|----------|:-------:|
| 1 | **Radicación** | Abogado externo | Carga factura y soportes en formulario único; el sistema valida y emite radicado. | C1, C2 |
| 2 | **Validación operativa** | Auxiliar / Analista | Revisa excepciones marcadas por el sistema; no diligencia por el proveedor. | C2 |
| 3 | **Autorización técnica** | Abogado interno | Aprueba o rechaza pertinencia del cobro desde el flujo (sin correos). | C3 |
| 4 | **Autorización financiera** | Coordinador / líder | Aprueba monto y centro de costos cuando supera el umbral definido. | C3, C4 |
| 5 | **Legalización** | Sistema + Aprendiz | Carga automática a Cargas Masivas P8 si aplica "Competitividad"; el resto avanza directo. | C4 |
| 6 | **Pago** | Ajustador | Recibe orden de pago con todos los datos ya validados y ejecuta el pago. | C4 |
| 7 | **Seguimiento y cierre** | Líder de proceso | Monitorea tablero, gestiona alertas SLA y responde consultas con un clic. | C5 |

### Automatización clave

- **Formulario único** (Power Apps / SharePoint) reemplaza el correo como canal de recepción.
- **Workflow** (Power Automate) orquesta aprobaciones, notifica responsables y mueve estados.
- **Integración / API** con CaseTracking para validación y con Cargas Masivas P8 para legalización.
- **Power BI** consume la base del flujo y entrega tablero ejecutivo con SLA en tiempo real.

### Trazabilidad

Cada factura tiene un identificador único y un historial inmutable de estados, responsables, fechas y comentarios. El abogado externo consulta el estado de su factura en un portal de autoservicio sin necesidad de enviar correos. La gerencia ve el panorama completo en tiempo real.

### Gestión de riesgos y calidad

- Validación en origen (C2) evita ingreso de datos incorrectos aguas abajo.
- Segregación de funciones y doble aprobación (C3) reducen el riesgo de fraude.
- Conciliación automática (C4) previene pagos duplicados o a proveedores inactivos.
- Tablero con SLA (C5) hace visible cualquier desviación antes de que escale.

**Indicadores priorizados:** % facturas radicadas correctamente al primer intento · tiempo medio Radicación → Pago · % pagos dentro de SLA · facturas devueltas por proveedor · monto pendiente por antigüedad.

---

*El rediseño no cambia el propósito del proceso —recepción, validación, autorización, pago y seguimiento—, solo lo centraliza en una herramienta única, automatiza las validaciones repetitivas y deja evidencia auditable de cada paso. Pocos controles, claros, con responsable y con dato.*