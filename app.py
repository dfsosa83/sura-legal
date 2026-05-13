"""
Dashboard interactivo — Reto Técnico Analítica Legal SURA
Autor: dfsosa83
Fecha: mayo 2026

Estructura:
  - Barra lateral con navegación entre secciones
  - Sección 1: Gestión de Tutelas
  - Sección 2: Portafolio Contractual
  - Sección 3: Propuesta de Facturación
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ──────────────────────────────────────────────
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Analítica Legal — SURA",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Rutas base (relativas al archivo app.py)
BASE = Path(__file__).parent
OUTPUTS = BASE / "outputs"
DATA    = BASE / "data"

# ──────────────────────────────────────────────
# PALETA DE COLORES SURA
# ──────────────────────────────────────────────
SURA_YELLOW   = "#E3E829"   # Amarillo SURA principal
SURA_BLUE     = "#3C86B4"   # Azul 03
SURA_BLUE2    = "#A8CDE2"   # Azul 01 (más claro)
SURA_GREEN    = "#52C599"   # Esmeralda
SURA_GREEN2   = "#A3E1C2"   # Esmeralda claro
SURA_RED      = "#9E3541"   # Vino (riesgo alto)
SURA_RED2     = "#DE9CA6"   # Vino claro
SURA_CAMEL    = "#D5AB80"   # Camel (riesgo medio)
SURA_GRAY     = "#727272"   # Gris oscuro
SURA_GRAY2    = "#C8C8C8"   # Gris claro

# CSS personalizado con identidad visual SURA
st.markdown("""
<style>
    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background-color: #1a2d42;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stRadio p {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] h2 {
        color: #E3E829 !important;
    }
    /* ── Encabezados principales ── */
    h1 {
        color: #1a2d42;
        border-bottom: 4px solid #E3E829;
        padding-bottom: 8px;
    }
    h2 { color: #3C86B4; }
    h3 { color: #3C86B4; }
    /* ── Tarjetas de métricas ── */
    [data-testid="stMetric"] {
        background-color: #f5f8fb;
        border-left: 4px solid #E3E829;
        border-radius: 4px;
        padding: 12px 16px;
    }
    [data-testid="stMetricLabel"] { color: #1a2d42 !important; font-weight: 600; }
    [data-testid="stMetricValue"] { color: #3C86B4 !important; font-size: 2rem !important; }
    /* ── Botón de descarga ── */
    .stDownloadButton > button {
        background-color: #E3E829;
        color: #1a2d42;
        font-weight: 700;
        border: none;
        border-radius: 4px;
    }
    .stDownloadButton > button:hover {
        background-color: #FFE946;
        color: #1a2d42;
    }
    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid #E3E829;
    }
    .stTabs [aria-selected="true"] {
        background-color: #E3E829 !important;
        color: #1a2d42 !important;
        font-weight: 700;
        border-radius: 4px 4px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# HELPERS — funciones reutilizables
# ──────────────────────────────────────────────

@st.cache_data  # guarda el resultado en caché para no releer el CSV en cada interacción
def cargar_tutelas_criticas():
    return pd.read_csv(OUTPUTS / "casos_criticos_priorizados.csv")

@st.cache_data
def cargar_contratos_criticos():
    return pd.read_csv(OUTPUTS / "contratos_criticos_90dias.csv")

@st.cache_data
def cargar_tutelas_raw():
    """Carga solo las columnas necesarias del dataset original de tutelas."""
    cols = [
        "Fecha y hora notificación tutela",
        "Fecha Vencimiento Admision",
        "Fecha y hora de Contestación",
        "Regional T",
        "Area causal",
        "Clasificación fallo 1ra Instancia",
        "Estado del ciclo de vida",
    ]
    df = pd.read_csv(DATA / "tutelas - Detalle1.csv", encoding="utf-8",
                     sep=None, engine="python", usecols=cols)
    df["Fecha y hora notificación tutela"] = pd.to_datetime(
        df["Fecha y hora notificación tutela"], errors="coerce")
    df["Fecha Vencimiento Admision"] = pd.to_datetime(
        df["Fecha Vencimiento Admision"], errors="coerce")
    df["Fecha y hora de Contestación"] = pd.to_datetime(
        df["Fecha y hora de Contestación"], errors="coerce")
    # Solo el período real del análisis: 2026
    df = df[df["Fecha y hora notificación tutela"].dt.year == 2026]
    return df

@st.cache_data
def cargar_contratos_raw():
    """Carga solo las columnas necesarias del dataset original de contratos."""
    cols = [
        "Estado",
        "Tipo de contrato",
        "Organización - Departamento",
        "Contrato - Fecha de expiración",
        "Compañía Contratante / NIT / Representante Legal de la Compañía Contratante / Cédula de Ciudadanía",
    ]
    df = pd.read_csv(DATA / "pivot_area - Data.csv", encoding="utf-8",
                     sep=None, engine="python", usecols=cols)
    df["Contrato - Fecha de expiración"] = pd.to_datetime(
        df["Contrato - Fecha de expiración"], errors="coerce", dayfirst=True)
    # Renombramos la columna larga para facilitar su uso
    df = df.rename(columns={
        "Compañía Contratante / NIT / Representante Legal de la Compañía Contratante / Cédula de Ciudadanía": "Compañía"
    })
    return df

def tarjeta_kpi(col, valor, etiqueta, color="#1f77b4", ayuda=None):
    """Muestra una tarjeta de KPI con valor grande y etiqueta debajo."""
    col.metric(label=etiqueta, value=valor, help=ayuda)


# ──────────────────────────────────────────────
# BARRA LATERAL — navegación principal
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<div style='text-align:center; padding: 12px 0 4px 0;'>
    <span style='font-size:2.2rem; font-weight:900; letter-spacing:4px; color:#E3E829;'>SURA</span>
</div>
<div style='text-align:center; padding-bottom:4px;'>
    <span style='font-size:0.8rem; color:#A8CDE2; letter-spacing:2px; text-transform:uppercase;'>Analítica Legal</span>
</div>
<hr style='border:1px solid #E3E829; margin:8px 0'>
""", unsafe_allow_html=True)

    seccion = st.radio(
        "Navegar a:",
        options=["⚖️  Gestión de Tutelas", "📋  Portafolio Contractual", "🧾  Proceso de Facturación"],
        index=0,
    )

    st.markdown("---")
    st.caption("Corte: 13 mayo 2026 · Reto Técnico SURA")


# ══════════════════════════════════════════════
# SECCIÓN 1 — GESTIÓN DE TUTELAS
# ══════════════════════════════════════════════
if seccion == "⚖️  Gestión de Tutelas":

    st.title("⚖️ Gestión de Tutelas 2026")
    st.markdown("Período analizado: **enero – abril 2026** · Registros: **12.751 tutelas**")
    st.markdown("---")

    # ── KPI cards ──────────────────────────────
    st.subheader("Indicadores clave")
    k1, k2, k3, k4 = st.columns(4)

    tarjeta_kpi(k1, "90.7 %", "⏱ Oportunidad de respuesta",
                ayuda="Tutelas contestadas antes del vencimiento de admisión")
    tarjeta_kpi(k2, "51.0 %", "✅ Favorabilidad 1ra instancia",
                ayuda="Fallos favorables sobre total de fallos emitidos")
    tarjeta_kpi(k3, "1,110", "🔴 Casos críticos activos",
                ayuda="Expedientes con score de criticidad alto (sin contestar, fallo desfavorable o medida provisional)")
    tarjeta_kpi(k4, "858", "⚠️ Sin contestación registrada",
                ayuda="Tutelas sin fecha de contestación en el sistema — riesgo de incumplimiento")

    st.markdown("---")

    # ── Filtros interactivos ────────────────────
    st.subheader("Casos críticos priorizados")
    df_crit = cargar_tutelas_criticas()

    col_f1, col_f2 = st.columns(2)

    with col_f1:
        regionales = ["Todas"] + sorted(df_crit["Regional T"].dropna().unique().tolist())
        regional_sel = st.selectbox("Filtrar por Regional:", regionales)

    with col_f2:
        causales = ["Todas"] + sorted(df_crit["Area causal"].dropna().unique().tolist())
        causal_sel = st.selectbox("Filtrar por Área causal:", causales)

    # Aplicar filtros
    df_filtrado = df_crit.copy()
    if regional_sel != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Regional T"] == regional_sel]
    if causal_sel != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Area causal"] == causal_sel]

    st.markdown(f"**{len(df_filtrado)} casos** con los filtros seleccionados")

    # Tabla de casos críticos
    st.dataframe(
        df_filtrado.sort_values("score", ascending=False).reset_index(drop=True),
        use_container_width=True,
        height=350,
    )

    # Botón para descargar la lista filtrada
    csv_export = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Descargar lista filtrada (CSV)",
        data=csv_export,
        file_name="casos_criticos_filtrados.csv",
        mime="text/csv",
    )

    st.markdown("---")

    # ── Gráficas ────────────────────────────────
    st.subheader("Análisis visual")

    tab1, tab2, tab3 = st.tabs(["Oportunidad por regional", "Distribución de fallos", "Concentración de riesgo"])

    with tab1:
        # Calcular oportunidad por regional desde el raw
        df_raw = cargar_tutelas_raw()
        df_valid = df_raw.dropna(subset=["Fecha y hora de Contestación", "Fecha Vencimiento Admision"])
        df_valid = df_valid.copy()
        df_valid["oportuno"] = df_valid["Fecha y hora de Contestación"] <= df_valid["Fecha Vencimiento Admision"]

        op_regional = (
            df_valid.groupby("Regional T")["oportuno"]
            .agg(["sum", "count"])
            .rename(columns={"sum": "Oportunos", "count": "Total"})
            .assign(pct=lambda x: (x["Oportunos"] / x["Total"] * 100).round(1))
            .reset_index()
            .sort_values("pct")
        )

        fig = px.bar(
            op_regional,
            x="pct", y="Regional T",
            orientation="h",
            text="pct",
            labels={"pct": "% Oportuno", "Regional T": "Regional"},
            title="% Oportunidad de respuesta por regional",
            color="pct",
            color_continuous_scale=[SURA_RED, SURA_CAMEL, SURA_GREEN],
            range_color=[80, 100],
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig.update_layout(coloraxis_showscale=False, height=350)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Favorabilidad por área causal
        df_raw2 = cargar_tutelas_raw()
        df_fav = (
            df_raw2.dropna(subset=["Clasificación fallo 1ra Instancia", "Area causal"])
            .groupby(["Area causal", "Clasificación fallo 1ra Instancia"])
            .size()
            .reset_index(name="n")
        )
        # Solo las 8 causales con más casos
        top_causales = df_fav.groupby("Area causal")["n"].sum().nlargest(8).index
        df_fav = df_fav[df_fav["Area causal"].isin(top_causales)]

        fig2 = px.bar(
            df_fav,
            x="n", y="Area causal",
            color="Clasificación fallo 1ra Instancia",
            orientation="h",
            title="Distribución de fallos por área causal (top 8)",
            labels={"n": "Casos", "Area causal": "", "Clasificación fallo 1ra Instancia": "Fallo"},
            color_discrete_map={
                "Fallo favorable": SURA_GREEN,
                "Fallo desfavorable": SURA_RED,
                "Desistimiento": SURA_GRAY2,
            },
        )
        fig2.update_layout(height=400, legend_title_text="Resultado")
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        # Mapa de calor regional × causal
        df_raw3 = cargar_tutelas_raw()
        heat = (
            df_raw3.dropna(subset=["Regional T", "Area causal"])
            .groupby(["Regional T", "Area causal"])
            .size()
            .reset_index(name="Casos")
        )
        pivot = heat.pivot(index="Area causal", columns="Regional T", values="Casos").fillna(0)

        fig3 = px.imshow(
            pivot,
            text_auto=True,
            color_continuous_scale=[SURA_BLUE2, SURA_BLUE, "#1a2d42"],
            title="Concentración de tutelas — Regional × Área causal",
            labels={"color": "Casos"},
            aspect="auto",
        )
        fig3.update_layout(height=450)
        st.plotly_chart(fig3, use_container_width=True)


# ══════════════════════════════════════════════
# SECCIÓN 2 — PORTAFOLIO CONTRACTUAL
# ══════════════════════════════════════════════
elif seccion == "📋  Portafolio Contractual":

    st.title("📋 Portafolio Contractual 2026")
    st.markdown("Corte: **13 mayo 2026** · Total en sistema: **52.004 contratos**")
    st.markdown("---")

    # ── KPI cards ──────────────────────────────
    st.subheader("Indicadores clave")
    k1, k2, k3, k4 = st.columns(4)

    tarjeta_kpi(k1, "22,453", "📁 Contratos activos",
                ayuda="Contratos con Estado = Activo a la fecha de corte")
    tarjeta_kpi(k2, "1,870", "🔴 Vencidos sin cierre",
                ayuda="Activos cuya fecha de expiración ya pasó y no tienen renovación registrada")
    tarjeta_kpi(k3, "890", "⚠️ Vencen en ≤ 30 días",
                ayuda="Requieren decisión inmediata: renovar o cerrar")
    tarjeta_kpi(k4, "3,600", "📅 Vencen en ≤ 90 días",
                ayuda="Ventana de atención prioritaria antes de agosto 2026")

    st.markdown("---")

    # ── Filtros ─────────────────────────────────
    st.subheader("Contratos en riesgo — próximos 90 días")
    df_cont = cargar_contratos_criticos()

    col_f1, col_f2 = st.columns(2)

    with col_f1:
        alertas = ["Todas"] + sorted(df_cont["alerta"].dropna().unique().tolist())
        alerta_sel = st.selectbox("Filtrar por nivel de alerta:", alertas)

    with col_f2:
        deptos = ["Todos"] + sorted(df_cont["Organización - Departamento"].dropna().unique().tolist())
        depto_sel = st.selectbox("Filtrar por Departamento:", deptos)

    # Aplicar filtros
    df_cf = df_cont.copy()
    if alerta_sel != "Todas":
        df_cf = df_cf[df_cf["alerta"] == alerta_sel]
    if depto_sel != "Todos":
        df_cf = df_cf[df_cf["Organización - Departamento"] == depto_sel]

    st.markdown(f"**{len(df_cf)} contratos** con los filtros seleccionados")

    st.dataframe(
        df_cf.sort_values("dias_hasta_venc").reset_index(drop=True),
        use_container_width=True,
        height=350,
    )

    csv_cont = df_cf.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Descargar lista filtrada (CSV)",
        data=csv_cont,
        file_name="contratos_criticos_filtrados.csv",
        mime="text/csv",
    )

    st.markdown("---")

    # ── Gráficas ────────────────────────────────
    st.subheader("Análisis visual")

    tab1, tab2, tab3 = st.tabs(["Estado del portafolio", "Vencimientos por departamento", "Curva de vencimientos"])

    with tab1:
        df_raw_c = cargar_contratos_raw()
        estado_cnt = df_raw_c["Estado"].value_counts().reset_index()
        estado_cnt.columns = ["Estado", "Contratos"]

        fig = px.pie(
            estado_cnt,
            names="Estado",
            values="Contratos",
            title="Estado general del portafolio",
            color_discrete_sequence=[SURA_GREEN, SURA_GRAY2],
            hole=0.4,
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # % en riesgo por departamento
        today = pd.Timestamp("2026-05-13")
        df_raw_c2 = cargar_contratos_raw()
        activos = df_raw_c2[df_raw_c2["Estado"] == "Activo"].copy()
        activos["en_riesgo"] = activos["Contrato - Fecha de expiración"] <= (today + pd.Timedelta(days=90))

        riesgo_depto = (
            activos.groupby("Organización - Departamento")["en_riesgo"]
            .agg(["sum", "count"])
            .rename(columns={"sum": "En riesgo", "count": "Total"})
            .assign(pct=lambda x: (x["En riesgo"] / x["Total"] * 100).round(1))
            .nlargest(12, "Total")
            .reset_index()
            .sort_values("pct", ascending=True)
        )

        fig2 = px.bar(
            riesgo_depto,
            x="pct", y="Organización - Departamento",
            orientation="h",
            text="pct",
            title="% contratos en riesgo (≤90 días) por departamento — top 12",
            labels={"pct": "% En riesgo", "Organización - Departamento": ""},
            color="pct",
            color_continuous_scale=[SURA_GREEN, SURA_CAMEL, SURA_RED],
        )
        fig2.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig2.update_layout(coloraxis_showscale=False, height=420)
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        # Curva de vencimientos mes a mes
        df_raw_c3 = cargar_contratos_raw()
        activos3 = df_raw_c3[df_raw_c3["Estado"] == "Activo"].dropna(subset=["Contrato - Fecha de expiración"]).copy()
        activos3["mes_venc"] = activos3["Contrato - Fecha de expiración"].dt.to_period("M").astype(str)

        # Solo los próximos 18 meses
        today_str = pd.Timestamp("2026-05-13")
        limite = today_str + pd.DateOffset(months=18)
        activos3 = activos3[
            (activos3["Contrato - Fecha de expiración"] >= today_str) &
            (activos3["Contrato - Fecha de expiración"] <= limite)
        ]
        curva = activos3.groupby("mes_venc").size().reset_index(name="Vencimientos")

        fig3 = px.bar(
            curva,
            x="mes_venc", y="Vencimientos",
            title="Proyección de vencimientos — próximos 18 meses",
            labels={"mes_venc": "Mes", "Vencimientos": "Contratos que vencen"},
            color="Vencimientos",
            color_continuous_scale=[SURA_GREEN, SURA_CAMEL, SURA_RED],
        )
        fig3.update_layout(coloraxis_showscale=False, xaxis_tickangle=-45)
        st.plotly_chart(fig3, use_container_width=True)


# ══════════════════════════════════════════════
# SECCIÓN 3 — PROCESO DE FACTURACIÓN
# ══════════════════════════════════════════════
elif seccion == "🧾  Proceso de Facturación":

    st.title("🧾 Proceso de Facturación — Abogados Externos")
    st.markdown("Reto 2 · Diagnóstico y propuesta de rediseño del proceso actual")
    st.markdown("---")

    # ── Diagnóstico del problema ────────────────
    st.subheader("¿Cuál es el problema?")
    st.error(
        "El proceso actual de facturación es **manual y descentralizado**: las facturas llegan "
        "por correo electrónico sin formato fijo, sin número de radicado, sin cruce automático "
        "con el sistema CaseTracking y sin trazabilidad de estado. Esto genera pérdidas de "
        "facturas, duplicados, demoras en el pago y falta de auditoría."
    )

    st.markdown("---")

    # ── Controles propuestos ────────────────────
    st.subheader("6 controles concretos")

    controles = [
        {
            "num": "1",
            "control": "Formulario digital único de recepción",
            "problema": "Facturas por correo sin formato → extravíos y duplicados",
            "tipo": "Tecnológico",
            "metrica": "% facturas ingresadas por canal digital",
        },
        {
            "num": "2",
            "control": "Número de radicado único automático",
            "problema": "Falta de trazabilidad individual por factura",
            "tipo": "Tecnológico / Operativo",
            "metrica": "0 facturas sin radicado en el sistema",
        },
        {
            "num": "3",
            "control": "Cruce automático con CaseTracking",
            "problema": "Cobros por casos no gestionados o montos no justificados",
            "tipo": "Tecnológico",
            "metrica": "% facturas rechazadas automáticamente por inconsistencia",
        },
        {
            "num": "4",
            "control": "Tablero de estados en tiempo real",
            "problema": "Falta de visibilidad → reenvíos, duplicados, consultas por correo",
            "tipo": "Tecnológico",
            "metrica": "Reducción de consultas de estado por correo",
        },
        {
            "num": "5",
            "control": "Alerta automática de SLA de pago",
            "problema": "Retrasos en pago no detectados a tiempo",
            "tipo": "Tecnológico / Gestión",
            "metrica": "% facturas pagadas dentro del SLA (ej. 30 días)",
        },
        {
            "num": "6",
            "control": "Conciliación mensual automatizada",
            "problema": "Pérdidas no detectadas y dobles pagos al cierre",
            "tipo": "Gestión / Control",
            "metrica": "0 diferencias no explicadas al cierre mensual",
        },
    ]

    st.dataframe(
        pd.DataFrame(controles).rename(columns={
            "num": "#", "control": "Control", "problema": "Problema que resuelve",
            "tipo": "Tipo", "metrica": "Métrica de éxito"
        }),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    # ── Flujo rediseñado ────────────────────────
    st.subheader("Flujo rediseñado — 5 etapas")

    etapas = [
        ("1 · Recepción", "Abogado externo", "Portal/formulario digital (canal único)", "Validación automática de campos obligatorios", "Radicado único + confirmación al abogado"),
        ("2 · Validación técnica", "Sistema + Coordinador (excepciones)", "Factura radicada + CaseTracking", "Cruce automático de casos y montos", "Aprobado automático o a revisión manual"),
        ("3 · Autorización", "Abogado interno apoderado", "Factura validada + resumen actividades", "Plazo máximo de respuesta (5 días hábiles)", "Factura autorizada o devuelta con motivo"),
        ("4 · Legalización", "Área contable / Asuntos Legales", "Factura autorizada", "Verificación NIT, retenciones, imputación", "Factura legalizada, lista para pago"),
        ("5 · Pago y seguimiento", "Ajustador / Tesorería", "Factura legalizada", "Alerta si SLA de pago se aproxima", "Confirmación de pago, cierre del expediente"),
    ]

    for etapa, actor, entrada, control, salida in etapas:
        with st.expander(f"**{etapa}** — Actor: {actor}"):
            col_a, col_b, col_c = st.columns(3)
            col_a.markdown(f"**Entrada**\n\n{entrada}")
            col_b.markdown(f"**Control**\n\n{control}")
            col_c.markdown(f"**Salida**\n\n{salida}")

    st.markdown("---")

    # ── Tabla de automatización por rol ─────────
    st.subheader("¿Qué puede automatizarse?")

    roles = pd.DataFrame([
        ("Abogado externo",    "Envía factura por correo sin formato",        "Formulario digital con validaciones en línea"),
        ("Coordinador legal",  "Revisa manualmente cada factura",             "Solo interviene en excepciones (cruce falla)"),
        ("Abogado interno",    "Autoriza por correo sin trazabilidad",        "Botón de aprobación en sistema con fecha/hora"),
        ("Área contable",      "Transcribe datos de factura al sistema",      "Integración directa formulario → ERP"),
        ("Tesorería/ajustador","Recibe notificación manual",                  "Notificación automática al aprobar legalización"),
        ("Todos",              "Consultan estado de facturas por correo",     "Tablero de estados en tiempo real"),
    ], columns=["Rol", "Tarea manual actual", "Propuesta de automatización"])

    st.dataframe(roles, use_container_width=True, hide_index=True)

    st.success(
        "**Punto de mayor impacto:** implementar el canal único de entrada con radicado automático "
        "elimina la fuente principal de pérdidas y habilita toda la trazabilidad posterior."
    )
