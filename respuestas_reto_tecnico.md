# Respuestas — Reto Técnico Analista de Analítica Legal SURA

---

## RETO 1 — PARTE 1: Gestión de Tutelas

**Dataset:** 12.952 tutelas · 47 columnas · Notificaciones desde 2013 hasta abr-2026

---

### ¿Dónde se concentran los principales riesgos?

| Regional | Tutelas | % |
|---|---|---|
| ANTIOQUIA | 6.128 | 47% |
| NORTE | 2.013 | 16% |
| CENTRO | 1.736 | 13% |
| OCCIDENTE | 1.602 | 12% |
| EJE CAFETERO | 1.396 | 11% |

Las combinaciones regional–causal de mayor presión:

1. **ANTIOQUIA | EPS_PRESTACIONES ECONÓMICAS** — 713 casos
2. **ANTIOQUIA | EPS_MEDICINA LABORAL** — 445
3. **CENTRO | ARL_SALUD INTEGRAL** — 410
4. **NORTE | ARL_SALUD INTEGRAL** — 410
5. **ANTIOQUIA | EPS_AFILIACIONES** — 409

Riesgo de incumplimiento de términos: **1.150 contestaciones (8,9%) se entregaron fuera del vencimiento de admisión**, y **963 tutelas (7,4%) no tienen fecha de contestación registrada**.

---

### ¿Qué etapas del proceso presentan mayores incumplimientos?

| Estado (etapa activa) | Casos |
|---|---|
| Espera de Fallo | 298 |
| Fallo Primera Instancia (cumplimiento pendiente) | 269 |
| Espera Fallo 2 | 267 |
| Gestión fallo 1 área | 1.407 |
| Gestión fallo 2 área | 86 |
| Impugnación | 8 |

**846 tutelas están en etapas activas de riesgo** (pendientes de resolución o cumplimiento). La etapa de contestación/admisión es donde se registra el mayor incumplimiento formal (8,9% fuera de término).

La etapa de **cumplimiento de fallo 1** es el cuello de botella principal: "Gestión fallo 1 área" (1.407 casos) indica que el área técnica aún no ha cerrado el expediente tras el fallo.

---

### ¿Qué variables impactan la oportunidad de respuesta?

Tiempo promedio de respuesta (notificación → contestación): **media 2,9 días, mediana 2,2 días**. El 99,2% responde dentro de los 10 días. Sin embargo esto puede ser engañoso: el 7,4% de las tutelas no tiene fecha de contestación registrada.

Variables con mayor impacto:

| Variable | Efecto |
|---|---|
| **Regional** | ANTIOQUIA es la más lenta (3,0 días media); CENTRO la más ágil (2,5 días) |
| **Area causal** | ARL_SALUD INTEGRAL y EPS_PRESTACIONES ECONÓMICAS concentran la mayor carga y el mayor riesgo de demora |
| **Calidad del dato** | 54,4% de nulos en `Area causal` y 67,3% en `Fecha de Contestación` limitan la medición real de oportunidad |
| **Medida provisional** | Las tutelas con medida provisional tienen términos reducidos (no cuantificable directamente, pero es un factor conocido) |

---

### ¿Qué regionales, áreas o causales generan mayor presión operativa?

**Por Regional:** ANTIOQUIA es la región crítica en volumen absoluto (casi la mitad del portafolio).

**Por Causal (área):**

| Causal | Casos |
|---|---|
| ARL_SALUD INTEGRAL | 1.529 |
| EPS_PRESTACIONES ECONÓMICAS | 1.160 |
| EPS_AFILIACIONES | 952 |
| EPS_MEDICINA LABORAL | 821 |
| ARL_GESTIÓN INTEGRAL DE PAGOS | 406 |

Las 4 causales principales concentran el **41% de las tutelas con causal registrada** (el otro 59% tiene el campo nulo, lo cual es una alerta de calidad de dato).

**Sobre favorabilidad:** Tasa de fallo favorable 1ra instancia = **51,3%** (6.220 favorables vs 5.842 desfavorables). Prácticamente 50/50, lo que indica riesgo jurídico alto y necesidad de análisis por causal para identificar dónde se pierde más.

---

### ¿Qué casos deberían priorizarse?

Criterios de priorización (en orden):

1. **Estado "Espera de Fallo"** (298 casos) — riesgo de fallo desfavorable inminente sin acción
2. **Estado "Fallo Primera Instancia"** (269) — fallo emitido, cumplimiento no iniciado
3. **Estado "Espera Fallo 2"** (267) — impugnaciones pendientes
4. Cualquier tutela con `Fecha Vencimiento Admision` superada **sin contestación registrada** — incumplimiento legal directo
5. Regionales ANTIOQUIA + causales EPS_MEDICINA LABORAL y EPS_PRESTACIONES ECONÓMICAS (mayor concentración de fallos desfavorables esperados)

---

## RETO 1 — PARTE 2: Gestión Contractual

**Dataset:** 52.004 registros · 22 columnas · 10 compañías del Grupo SURA

---

### ¿Cuál es el estado actual de la operación contractual?

| Estado | Contratos | % |
|---|---|---|
| Activo | 22.453 | 43,2% |
| Finalizado | 29.551 | 56,8% |

Dentro de los activos, por estado interno del contrato:

- Publicado: 19.009
- Borrador: 2.250 (contratos sin publicar — riesgo de validez)
- Vencido: 860 (activos pero el sistema ya los marca como vencidos)

**Alerta crítica:** 1.417 contratos tienen `Estado = Activo` pero su `Fecha de expiración` ya pasó (fecha < hoy). Son contratos jurídicamente vencidos que el sistema aún no ha cerrado.

**Contratos de abogados externos:** 1.661 en total, **1.099 activos** — relevante para el Reto 2.

---

### ¿Qué contratos requieren atención prioritaria y dónde se concentran los riesgos de vencimiento?

| Ventana de vencimiento | Contratos activos |
|---|---|
| **Ya vencidos** (activos con fecha pasada) | **1.417** |
| Vence **hoy** | 22 |
| ≤ 30 días | 874 |
| 31–60 días | 1.504 |
| 61–90 días | 1.185 |
| +90 días | 17.006 |

**Atención inmediata:** 2.313 contratos (1.417 vencidos + 22 que vencen hoy + 874 en ≤30 días).

Por compañía, los más urgentes (vencen en ≤90 días):

| Compañía | Contratos |
|---|---|
| SEGUROS DE VIDA SURAMERICANA | 1.007 |
| ARL (ramo SURA) | 638 |
| EPS SURA | 544 |
| SEGUROS GENERALES | 335 |

---

### ¿Qué compañías o tipos de contrato generan mayor carga operativa?

**Por compañía:**

- SEGUROS DE VIDA SURAMERICANA: 15.788 contratos (30%)
- SEGUROS DE VIDA ARL: 7.818 (15%)
- EPS SURA: 5.340 (10%)

**Por tipo de contrato (top 5):**

| Tipo | Total |
|---|---|
| PRESTACIÓN DE SERVICIOS | 11.066 |
| ARL PREVENCIÓN | 4.455 |
| MARCO DE SERVICIOS | 4.387 |
| PRESTACIÓN SERVICIOS NEGOCIO (PÓLIZA SALUD) | 3.289 |
| CGR – SALUD ARL | 2.571 |

**Por departamento (área operativa):** ARL Salud (5.538), ARL Prevención (4.940) y Talento Humano (4.518) concentran la mayor carga de gestión.

---

### ¿Existen concentraciones de contratos próximos a expirar?

Sí. **3.585 contratos activos vencen en los próximos 90 días**, distribuidos en múltiples tipos:

- PRESTACIÓN DE SERVICIOS ARL PREVENCIÓN: **798** — mayor riesgo concentrado
- PRESTACIÓN DE SERVICIOS general: 679
- ALIANZA COMERCIAL TALENTO HUMANO: 315
- **ABOGADOS EXTERNOS: 243** (22% del portafolio activo de esta categoría vence en <90 días)

La mayor concentración temporal de vencimientos está en la ventana **31–60 días** (1.504 contratos), lo que crea un pico de carga de renovación para el equipo legal en junio 2026.

---

### ¿Qué variables deberían monitorearse de forma permanente?

1. **Fecha de expiración vs. Estado** — inconsistencia: 1.417 activos ya vencidos sin cierre
2. **Estado del contrato = "Borrador"** activos (2.250) — contratos sin publicar que pueden carecer de validez legal
3. **Días al vencimiento por compañía y tipo** — alerta en ≤30 días
4. **Contratos ABOGADOS EXTERNOS** — directamente ligados al proceso de facturación (Reto 2)
5. **Tipo de periodo de vigencia** — contratos de vigencia fija vs. indefinida requieren tratamiento distinto
6. **Importe del contrato sin valor registrado** — riesgo de contratos sin valorización

---

## RETO 2 — Proceso de Facturación de Abogados Externos

*(Análisis documental — sin base de datos asociada)*

---

### ¿Qué controles concretos permitirían prevenir pérdidas, mejorar eficiencia y asegurar trazabilidad?

| # | Control | Problema que resuelve | Tipo | Métrica de efectividad |
|---|---|---|---|---|
| 1 | **Formulario digital único de recepción** (portal web o Teams) con campos obligatorios (radicado CaseTracking, periodo, valor, contrato asociado) | Facturas enviadas por correo sin validación → extravíos y duplicados | Tecnológico | % facturas ingresadas por canal digital vs. correo |
| 2 | **Número de radicado único** generado automáticamente al ingresar la factura | Falta de trazabilidad individual de cada factura | Tecnológico/operativo | 0 facturas sin radicado en el sistema |
| 3 | **Cruce automático con CaseTracking** antes de la autorización | Cobros por casos no gestionados o valores no justificados | Tecnológico | % facturas rechazadas automáticamente por inconsistencia |
| 4 | **Tablero de estados** visible para el abogado externo, el apoderado interno y el área de pagos (ej. SharePoint + Power BI) | Falta de visibilidad → reenvíos, duplicados, consultas innecesarias | Tecnológico | Reducción de consultas de estado por correo |
| 5 | **Alerta automática de SLA de pago** (ej. 30 días desde aprobación) | Retrasos en pago no detectados a tiempo | Tecnológico/gestión | % facturas pagadas dentro del SLA |
| 6 | **Conciliación mensual automatizada** entre facturas recibidas, aprobadas y pagos ejecutados | Pérdidas no detectadas y dobles pagos | Gestión/control | 0 diferencias no explicadas al cierre mensual |

---

### ¿Cómo sería un flujo de trabajo estructurado?

```
┌─────────────────────────────────────────────────────────────────┐
│  ETAPA 1 — RECEPCIÓN                                            │
│  Actor: Abogado externo                                         │
│  Input: Factura + soporte de actividades                        │
│  Acción: Ingreso por portal/formulario digital (canal único)    │
│  Control: Validación automática de campos obligatorios          │
│  Output: Radicado único asignado, confirmación al abogado       │
└──────────────────────┬──────────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  ETAPA 2 — VALIDACIÓN TÉCNICA                                   │
│  Actor: Sistema (automático) + Coordinador legal (excepciones)  │
│  Input: Factura radicada + datos CaseTracking                   │
│  Acción: Cruce automático de casos facturados vs. gestionados   │
│  Control: Reglas de negocio (montos, períodos, contrato vigente)│
│  Output: Aprobado automático o enviado a revisión manual        │
└──────────────────────┬──────────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  ETAPA 3 — AUTORIZACIÓN                                         │
│  Actor: Abogado interno apoderado                               │
│  Input: Factura validada + resumen de actividades               │
│  Acción: Aprobación/rechazo en el sistema (no por correo)       │
│  Control: Plazo máximo de respuesta (ej. 5 días hábiles)        │
│  Output: Factura autorizada o devuelta con motivo claro         │
└──────────────────────┬──────────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  ETAPA 4 — LEGALIZACIÓN Y REGISTRO                              │
│  Actor: Área contable / Asuntos Legales                         │
│  Input: Factura autorizada                                      │
│  Acción: Registro en sistema contable, vinculación al contrato  │
│  Control: Verificación NIT, retenciones, imputación presupuestal│
│  Output: Factura legalizada, lista para pago                    │
└──────────────────────┬──────────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  ETAPA 5 — PAGO Y SEGUIMIENTO                                   │
│  Actor: Ajustador / Tesorería                                   │
│  Input: Factura legalizada                                      │
│  Acción: Ejecución del pago dentro del SLA                      │
│  Control: Alerta automática si SLA de pago se aproxima          │
│  Output: Confirmación de pago, cierre del expediente            │
└─────────────────────────────────────────────────────────────────┘
```

---

### ¿Qué roles intervienen y qué puede automatizarse?

| Rol | Tarea manual actual | Automatizable |
|---|---|---|
| Abogado externo | Envía factura por correo sin formato | → Formulario digital con validaciones en línea |
| Coordinador legal | Revisa manualmente cada factura | → Solo excepciones (cruce CaseTracking falla) |
| Abogado interno | Autoriza por correo sin trazabilidad | → Botón de aprobación en sistema con fecha/hora |
| Área contable | Transcribe datos de factura al sistema | → Integración directa formulario → ERP |
| Tesorería/ajustador | Recibe notificación manual | → Notificación automática al aprobar legalización |
| Todos | Consultan estado por correo | → Tablero de estados en tiempo real (Power BI/SharePoint) |

**Punto crítico de mejora:** el proceso actual depende de correo electrónico y acciones individuales no registradas, lo que hace imposible auditar dónde se pierde una factura. El primer paso más impactante es el **canal único de entrada con radicado automático**.
