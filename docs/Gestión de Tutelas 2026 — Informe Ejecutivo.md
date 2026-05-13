**# Gestión de Tutelas 2026 — Informe Ejecutivo**

<div style="background:#2E4057; color:white; padding:9px 18px; border-radius:5px; margin:10px 0; font-size:0.88em; letter-spacing:0.02em;">

📅 <strong>Período:</strong> enero – abril 2026 &nbsp;·&nbsp; <strong>Corte:</strong> 12 mayo 2026 &nbsp;·&nbsp; 📂 <strong>Registros:</strong> 12,726 tutelas &nbsp;·&nbsp; ✅ <strong>Calidad dato:</strong> 99.8 % OK

</div>

**---**

**## El reloj corre — y el margen es mínimo**

Cada tutela activa un contador: ***\*48 horas\**** para contestar. El equipo responde: ***\*90.7 %\**** de los expedientes se contestan a tiempo. Un número que, a primera vista, tranquiliza.

Pero la mediana real de respuesta es ***\*53 horas\**** — 5 horas sobre el límite —, y solo el 34.6 % de los casos se resuelve con holgura. La mayoría de los "cumplimientos" son milimétricos. En el período analizado, ***\*1,107 contestaciones llegaron tarde\**** y ***\*858 expedientes activos aún no tienen respuesta registrada\****. El incumplimiento no se distribuye uniformemente: CENTRO acumula la tasa más baja (***\*87.0 %\****) y ANTIOQUIA concentra el mayor volumen absoluto con 540 tardíos. El cruce `ANTIOQUIA × EPS_Medicina Laboral` es la combinación de mayor riesgo del sistema (51 incumplimientos, 12.1 %).

<img src="../outputs/fig1_oportunidad_regional.png" style="width:92%; margin:8px 0;">

El cuello de botella no está en la respuesta interna — la etapa Notificación → Contestación tarda solo ***\*2 días\**** (mediana). Está en la segunda instancia: ***\*Fallo 1ra → Notif. 2da\**** demora ***\*31 días\**** (P90: 43 días). Tiempo judicial, pero aprovechable con un monitor activo.

**---**

**## Dónde se concentra la exposición — y lo que no aparece en los reportes**

La favorabilidad global en primera instancia es del ***\*51.0 %\****: uno de cada dos fallos es adverso para SURA — más de ***\*5,700 obligaciones de cumplimiento\**** en el período. El patrón no es uniforme: ARL y Vida superan el 75 % de favorabilidad; ***\*EPS_Prestaciones Económicas cae al 42.2 %\**** en más de 1,000 casos anuales. La diferencia no es aleatoria — sugiere jurisprudencia adversa no gestionada.

El mapa de calor `Regional × Área Causal` revela las combinaciones con mayor exposición real, incluyendo un punto caliente invisible al análisis convencional de volumen: `CENTRO × Seguros Empresariales` acumula ***\*47 % de incumplimiento\**** sobre 21 expedientes.

<img src="../outputs/fig4_mapa_riesgo.png" style="width:92%; margin:8px 0;">

| Prioridad | Riesgo | Indicador |

|:---:|:---|:---|

| 🔴 | Expedientes sin contestación registrada | 858 activos — sin defensa ante el juez |

| 🔴 | Casos críticos activos (score ≥ 3) | ***\*1,110 · 10.0 %\**** del total activo |

| 🔴 | ANTIOQUIA × EPS_Medicina Laboral | 51 tardíos · 12.1 % de tasa |

| 🔴 | CENTRO × Seguros Empresariales | 47 % de incumplimiento · punto caliente oculto |

| 🟡 | Favorabilidad EPS_Prestaciones Económicas | 42.2 % — pérdida sistemática en +1,000 casos/año |

| 🟡 | `Área causal` sin registrar en EPS | 54.3 % nulos — benchmarking por negocio imposible |

**---**

**## Plan de acción y propuesta de automatización**

***\*🔴 Inmediato (≤ 30 días):\**** Activar revisión de los ***\*1,110 casos críticos\**** (lista en `casos_criticos_priorizados.csv`; 12 con score máximo 7). Auditar ***\*858 expedientes sin contestación\****. Intervenir `CENTRO × Seguros Empresariales` con refuerzo directo.

***\*🟡 Corto plazo (30–90 días):\**** Alerta automática a las ***\*40 h\**** sin contestación (8 h de margen real antes del vencimiento). Monitor de segunda instancia: con 31 días de ventana, preparar impugnaciones antes de que el juez actúe. Revisión de estrategia argumentativa en EPS_Prestaciones Económicas.

***\*⚫ Estructural (90+ días):\**** `Área causal` obligatoria en el sistema de radicación EPS. Tablero de carga crítica por abogado — el análisis revela concentración de riesgo en pocos profesionales, hoy invisible.

La operación ***\*reacciona bien, pero de forma reactiva\****. La propuesta de automatización convierte ese ciclo:

| Iniciativa | Plazo | Impacto |

|:---|:---:|:---|

| Validación `Área causal` obligatoria en radicación | 30 d | Elimina nulos estructurales en el origen |

| Alertas SLA escalonadas: aviso 24 h / alerta 40 h / crítico 47 h | 45 d | Previene ~60 % de tardíos evitables |

| Score de criticidad batch nocturno → lista diaria | 60 d | Priorización automática sin trabajo manual |

| Monitor Fallo 1ra → 2da: tarea automática a 20 días del fallo | 60 d | Convierte espera judicial en preparación activa |

| Pipeline de informe ejecutivo semanal automatizado | 90 d | Reporte periódico a costo marginal cero |

\> **La prioridad 0 no es el dashboard — es el registro completo en la fuente. Ninguna automatización sostiene lo que no se captura.**

**---**

<div style="font-size:0.82em; color:#566573; margin-top:6px;">

📊 Análisis completo: <code>outputs/informe_tutelas_2026.html</code> &nbsp;·&nbsp; 📋 Casos críticos: <code>outputs/casos_criticos_priorizados.csv</code> &nbsp;·&nbsp; 🔧 Python · pandas · matplotlib · 41 variables

</div>