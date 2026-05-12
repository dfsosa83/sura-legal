# Plan de Trabajo — Reto Técnico Analista de Analítica Legal SURA

**Principio rector:** Claridad sobre complejidad. Cada paso debe producir una respuesta concreta a una pregunta del negocio.

---

## Estructura de archivos

```
sura-legal/
├── data/
│   ├── tutelas - Detalle1.csv                         # Reto 1 – Parte 1 (47 cols)
│   └── pivot_area - Data.csv                          # Reto 1 – Parte 2 (22 cols)
├── notebooks/
│   ├── 01_tutelas_exploration.ipynb                   # Exploración inicial tutelas
│   ├── 02_tutelas_quality.ipynb                       # Calidad y normalización tutelas
│   ├── 03_tutelas_analysis.ipynb                      # Indicadores y hallazgos tutelas
│   ├── 04_contracts_exploration.ipynb                 # Exploración inicial contratos
│   └── 05_contracts_analysis.ipynb                   # Indicadores y hallazgos contratos
├── outputs/
│   ├── tutelas_dashboard.xlsx                         # Tablero final tutelas (Excel)
│   └── contracts_dashboard.xlsx                       # Tablero final contratos (Excel)
├── docs/
│   ├── ejecutivo_tutelas.docx                         # Documento ejecutivo ≤2 pág. Reto 1-P1
│   ├── ejecutivo_contratos.docx                       # Documento ejecutivo ≤2 pág. Reto 1-P2
│   └── reto2_flujo_facturacion.docx                   # Propuesta flujo + controles Reto 2
└── plan.md
```

---

## RETO 1 — PARTE 1: Gestión de Tutelas

### Notebook 01 · Exploración inicial (`01_tutelas_exploration.ipynb`)

**Objetivo:** Entender qué hay en el dato antes de concluir nada.

- Cargar el archivo y revisar estructura: columnas, tipos de dato, tamaño
- Identificar campos clave: fechas, estados, regionales, causales, etapas, fallos
- Revisar distribuciones básicas: conteos, rangos de fechas, valores únicos
- Mapear el ciclo de vida de una tutela en los datos (¿qué columnas marcan cada etapa?)
- Preguntas a responder aquí:
  - ¿Cuántas tutelas hay en total? ¿Cuál es el período cubierto?
  - ¿Qué estados, etapas y causales existen?
  - ¿Cuántas regionales/áreas aparecen?
  - ¿Hay campos con alto porcentaje de nulos?

---

### Notebook 02 · Calidad y normalización (`02_tutelas_quality.ipynb`)

**Objetivo:** Dejar el dato limpio y confiable para el análisis.

- Revisar nulos por columna y definir tratamiento (flag, imputar, excluir)
- Estandarizar fechas (formato único, detectar fechas imposibles)
- Normalizar textos: mayúsculas, tildes, nombres de regionales/causales inconsistentes
- Detectar duplicados (mismo radicado, misma fecha)
- Crear columna `calidad_dato` (OK / Incompleto / Inconsistente) por registro
- Documentar hallazgos de calidad como hallazgo para el ejecutivo
- Preguntas a responder aquí:
  - ¿Qué porcentaje del dato es confiable?
  - ¿Existen inconsistencias sistemáticas en alguna regional o área?

---

### Notebook 03 · Análisis e indicadores (`03_tutelas_analysis.ipynb`)

**Objetivo:** Responder cada pregunta del reto con un número o un patrón claro.

#### Bloque A — Oportunidad y términos
- Calcular días hábiles entre radicación y respuesta
- Definir regla de oportunidad (término legal de tutela: 10 días hábiles para respuesta)
- Indicadores:
  - % tutelas respondidas a tiempo
  - Promedio de días de respuesta por regional / causal / etapa
  - Top 5 casos con mayor retraso
- Pregunta respondida: *¿Qué etapas presentan mayores incumplimientos? ¿Qué variables impactan la oportunidad?*

#### Bloque B — Concentración de riesgos
- Agrupar por regional, causal, tipo de proceso, etapa
- Calcular volumen y % de incumplimiento por cada agrupación
- Identificar las 3 combinaciones regional-causal con mayor presión
- Pregunta respondida: *¿Dónde se concentran los principales riesgos? ¿Qué regionales/áreas generan mayor presión operativa?*

#### Bloque C — Favorabilidad
- Calcular tasa de fallo favorable / desfavorable / impugnado
- Cruzar favorabilidad con causal y regional
- Pregunta respondida: *¿Cuál es la favorabilidad de las tutelas?*

#### Bloque D — Casos críticos y priorización
- Definir criterio de criticidad: vencido + sin respuesta + alta causal de riesgo
- Generar lista priorizada de casos activos que requieren acción inmediata
- Pregunta respondida: *¿Qué casos deberían priorizarse?*

#### Bloque E — Cuellos de botella
- Calcular tiempo promedio por etapa del proceso (si la data lo permite)
- Identificar etapa con mayor tiempo de espera acumulado
- Pregunta respondida: *¿Qué etapas del proceso presentan cuellos de botella?*

---

## RETO 1 — PARTE 2: Gestión Contractual

### Notebook 04 · Exploración inicial contratos (`04_contracts_exploration.ipynb`)

**Objetivo:** Entender la estructura del portafolio contractual.

- Cargar y revisar estructura: columnas, tipos, tamaño
- Identificar campos clave: fechas de inicio/vencimiento, estado, compañía, tipo de contrato
- Distribuciones básicas: estados, compañías, tipos de contrato
- Preguntas a responder aquí:
  - ¿Cuántos contratos hay? ¿Cuáles son los estados posibles?
  - ¿Qué compañías concentran más contratos?
  - ¿Cuál es el período de vigencia típico?

---

### Notebook 05 · Análisis de contratos (`05_contracts_analysis.ipynb`)

**Objetivo:** Responder cada pregunta del reto con indicadores concretos.

#### Bloque A — Estado actual del portafolio
- Indicadores base:
  - Total contratos por estado (activo, vencido, en renovación, etc.)
  - % activos vs. vencidos vs. próximos a vencer
- Pregunta respondida: *¿Cuál es el estado actual de la operación contractual?*

#### Bloque B — Contratos próximos a vencer
- Calcular días hasta vencimiento para contratos activos
- Categorizar: vence en ≤30 días / 31-60 días / 61-90 días / +90 días
- Identificar contratos vencidos sin renovación registrada
- Pregunta respondida: *¿Qué contratos requieren atención prioritaria? ¿Dónde se concentran los riesgos de vencimiento?*

#### Bloque C — Concentración y carga operativa
- Agrupar por compañía y tipo de contrato
- Identificar quién genera mayor volumen y mayor riesgo de vencimiento simultáneo
- Pregunta respondida: *¿Qué compañías o tipos de contrato generan mayor carga operativa?*

#### Bloque D — Alertas y anomalías
- Contratos sin fecha de vencimiento registrada
- Contratos con fecha de inicio posterior a fecha de vencimiento
- Contratos activos sin actualizaciones recientes (si hay campo de modificación)
- Pregunta respondida: *¿Existen inconsistencias? ¿Qué variables deberían monitorearse permanentemente?*

---

## RETO 2 — Proceso de Facturación (sin datos, trabajo documental)

### Documento `reto2_flujo_facturacion.docx`

#### Parte A — 5 controles concretos
Para cada control especificar:
- Problema que resuelve (de los identificados en el enunciado)
- Tipo: tecnológico / operativo / de gestión
- Cómo se implementa (qué herramienta o práctica)
- Qué métrica confirmaría que funciona

Controles a proponer (mínimo 5):
1. Formulario digital de recepción con validación automática de campos obligatorios
2. Número de radicado único por factura desde el ingreso al sistema
3. Tablero de trazabilidad con estados visibles para todos los actores
4. Regla de devolución automática (no manual) cuando el CaseTracking no cuadra
5. Alerta automática de vencimiento de SLA de pago por factura
6. (Adicional) Conciliación periódica automatizada entre facturas recibidas y pagos ejecutados

#### Parte B — Flujo rediseñado
Modelar en 5 etapas claras:
1. **Recepción** — canal único (formulario/portal), validación automática en el momento
2. **Validación técnica** — cruce automático con CaseTracking, solo excepciones van a manual
3. **Autorización** — notificación al abogado interno vía sistema (no correo), con plazo definido
4. **Legalización y registro** — automatizado para todas las facturas (no solo "Competitividad")
5. **Pago y seguimiento** — envío automático al ajustador, estado visible en tiempo real

Para cada etapa: actor responsable, input, output, control de calidad.

---

## Deliverables finales a entregar

| Entregable | Formato | Fuente |
|---|---|---|
| Análisis tutelas (visualizaciones + KPIs) | Excel o Power BI | Notebooks 01-03 |
| Ejecutivo tutelas | Documento ≤2 pág | Notebook 03 hallazgos |
| Análisis contratos (tablero ejecutivo) | Excel o Power BI | Notebooks 04-05 |
| Ejecutivo contratos | Documento ≤2 pág | Notebook 05 hallazgos |
| Controles + flujo facturación | Documento | Trabajo manual |
| Propuesta automatización (Reto 1 P1 y P2) | Sección en ejecutivos | Inferido del análisis |

---

## Orden de ejecución recomendado

```
Día 1 (hoy)
  ├── 01_tutelas_exploration    → entender el dato
  ├── 04_contracts_exploration  → entender el dato
  └── 02_tutelas_quality        → limpiar antes de analizar

Día 2
  ├── 03_tutelas_analysis       → todos los bloques A-E
  ├── 05_contracts_analysis     → todos los bloques A-D
  └── Construir dashboards en Excel/Power BI desde los outputs

Día 3 (mañana, antes del mediodía)
  ├── Redactar ejecutivo tutelas
  ├── Redactar ejecutivo contratos
  └── Redactar Reto 2 (controles + flujo)
```

---

## Reglas de trabajo

- Un notebook = un propósito. No mezclar exploración con análisis.
- Cada indicador debe tener una pregunta de negocio asociada.
- Si el dato no permite responder algo, documentarlo como hallazgo de calidad.
- El documento ejecutivo no describe el tablero — interpreta los hallazgos.
- Evitar jerga técnica en los documentos ejecutivos; lenguaje del negocio jurídico.
