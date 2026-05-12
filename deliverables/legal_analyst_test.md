# Prueba técnica – Analista legal (SURA Colombia)

## 1) Objetivo
Construir una prueba completa con dos datasets para analizar riesgos legales, responder preguntas de negocio y proponer mejoras accionables para el área jurídica.

## 2) Datasets usados

### Dataset 1: Litigios
Archivo: `/data/dataset_1_litigios.csv`

Variables clave: tipo de proceso, región, monto reclamado, estado, días abiertos, resultado, reserva contable.

### Dataset 2: Contratos
Archivo: `/data/dataset_2_contratos.csv`

Variables clave: categoría, valor anual, riesgo de cumplimiento, vencimiento, cláusulas de protección de datos, auditoría e incidentes.

## 3) Preguntas y respuestas

### Pregunta 1. ¿Cuál es el nivel actual de exposición legal en litigios?
- Casos totales: **12**
- Casos abiertos: **7 (58,3%)**
- Monto reclamado total: **USD 1.180.000**
- Monto en casos abiertos: **USD 825.000 (69,9% del total)**

**Respuesta:** la exposición está concentrada en casos abiertos, que representan casi 70% del monto total reclamado.

### Pregunta 2. ¿Qué tan robusta es la cobertura de reservas contables?
- Reserva total: **USD 850.000**
- Cobertura sobre monto reclamado: **72,03%**

**Respuesta:** hay una brecha aproximada de **USD 330.000** frente al total reclamado. Conviene revisar suficiencia de reserva por tipo de proceso.

### Pregunta 3. ¿Qué procesos concentran más riesgo económico?
- Laboral: **USD 605.000**
- Civil: **USD 295.000**
- Regulatorio: **USD 165.000**
- Consumidor: **USD 115.000**

**Respuesta:** los procesos **laborales** concentran más de la mitad de la exposición (51,3%), por lo que deberían ser prioridad en prevención y estrategia procesal.

### Pregunta 4. ¿Qué señales de eficiencia/prolongación hay en gestión judicial?
- Promedio de días en casos abiertos: **333,57 días**

**Respuesta:** el tiempo promedio es alto y sugiere necesidad de estrategia de cierre temprano (conciliación selectiva, priorización por probabilidad de pérdida y cuantía).

### Pregunta 5. ¿Cuál es el desempeño histórico de cierre?
En casos cerrados (5):
- Ganados: **20%**
- Conciliados: **40%**
- Perdidos: **40%**

**Respuesta:** la tasa de pérdida + conciliación (80%) indica oportunidad de fortalecer defensa temprana y calidad probatoria.

### Pregunta 6. ¿Qué tan concentrado está el riesgo contractual?
- Contratos totales: **10**
- Valor anual total: **USD 2.350.000**
- Riesgo alto: **5 contratos (50%)**, con **USD 1.360.000 (57,9%)**

**Respuesta:** la mayor parte del valor contractual está en contratos de riesgo alto.

### Pregunta 7. ¿Qué alertas de cumplimiento contractual son más críticas?
- Contratos que vencen en <=60 días: **6**
- Sin cláusula de protección de datos: **5**
- Sin auditoría a proveedor: **7**
- Incidentes reportados (12 meses): **13**

**Respuesta:** hay riesgo operativo y regulatorio inmediato por volumen de renovaciones cercanas y controles incompletos.

### Pregunta 8. ¿Dónde está la prioridad inmediata de intervención?
Contratos de riesgo alto **sin cláusula de datos** y **sin auditoría**:
- C-001, C-003, C-010
- Valor conjunto: **USD 730.000**
- Incidentes: **9**

**Respuesta:** estos 3 contratos son prioridad 1 para mitigación en el próximo ciclo.

## 4) Propuestas de mejora
1. **Modelo de priorización legal (score 0-100):** combinar monto, probabilidad de pérdida, días abiertos, etapa procesal y criticidad regulatoria.
2. **Gobierno de reservas:** comité mensual legal-financiero para recalibrar reservas por cartera de riesgo.
3. **Playbook de cierre temprano:** criterios de conciliación por umbrales de costo-tiempo-riesgo.
4. **Política contractual mínima obligatoria:** cláusulas de protección de datos, auditoría y SLA de incidentes para contratos críticos.
5. **Control de vencimientos:** tablero de alertas a 90/60/30 días con responsables por categoría y región.
6. **Lecciones aprendidas:** para cada caso perdido/conciliado, registrar causa raíz y acción preventiva en negocio.

## 5) Insights de valor para decisión
- **Insight 1:** el riesgo legal está más concentrado en **laboral** que en cualquier otra tipología.
- **Insight 2:** la exposición abierta supera 2/3 del monto reclamado, por lo que reducir backlog judicial impacta directamente el riesgo.
- **Insight 3:** en contratos, el riesgo alto no es marginal: concentra casi 58% del valor anual.
- **Insight 4:** 3 contratos explican la mayor parte de incidentes del segmento más crítico; su intervención rápida puede dar impacto visible en corto plazo.

## 6) Siguiente iteración recomendada
- Añadir probabilidad de pérdida por caso, costo legal externo y etapa procesal.
- Integrar variables de impacto reputacional y afectación a cliente.
- Automatizar dashboard en Power BI/Looker con actualización periódica.
