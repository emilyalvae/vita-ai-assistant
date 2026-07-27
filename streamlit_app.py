import streamlit as st
from pathlib import Path
from PIL import Image
from app.agents.graph import graph

BASE_DIR = Path(__file__).parent

logo = Image.open(BASE_DIR / "assets" / "logo.png")
# -------------------------------------------------
# Configuración
# -------------------------------------------------

st.set_page_config(
    page_title="Vita - Clínica Vitalis",
    page_icon=logo,
    layout="centered"
)
# -------------------------------------------------
# Encabezado
# -------------------------------------------------

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(logo, width=220)

st.markdown(
    """
    <h1 style="text-align:center; margin-bottom:0;">
        Clínica Vitalis
    </h1>

    <h3 style="text-align:center; color:gray;">
        🤖 Vita - Asistente Virtual
    </h3>

    <p style="text-align:center;">
        Bienvenido.<br><br>
        Soy <b>Vita</b>, el asistente virtual de la
        <b>Clínica Vitalis</b>.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()
# -------------------------------------------------
# Entrada
# -------------------------------------------------
pregunta = st.text_input(
    "¿En qué puedo ayudarte?",
    placeholder="Ejemplo: ¿Qué especialidades tiene la clínica?"
)


# -------------------------------------------------
# Botón
# -------------------------------------------------

col1, col2, col3 = st.columns([2, 1, 1])

with col3:
    consultar = st.button(
        "🔍 Consultar",
        width="stretch"
    )

if pregunta:

    with st.spinner("Vita está buscando la mejor respuesta..."):

        resultado = graph.invoke(
            {
                "pregunta": pregunta
            }
        )

    st.success("Consulta procesada correctamente.")

    st.subheader("💬 Respuesta")

    st.write(
        resultado["respuesta"]
    )

    st.divider()

    with st.expander(
        "🤖 Información del agente"
    ):

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("**Decisión del triaje**")

            st.info(
                resultado["triaje"]["decision"]
            )

        with col2:

            st.markdown("**Acción final**")

            st.success(
                resultado["accion_final"]
            )

    if resultado["citaciones"]:

        st.divider()

        st.subheader("📚 Fuentes utilizadas")

        for i, documento in enumerate(
            resultado["citaciones"]
        ):

            with st.expander(
                f"Documento {i+1}"
            ):

                st.caption(
                    documento.metadata["source"]
                )

                st.write(
                    documento.page_content
                )

else:

    st.warning(
        "⚠️ Escribe una consulta antes de continuar."
    )


st.divider()

st.caption(
    "Vita AI Assistant • LangGraph • LangChain • FAISS • Google Gemini"
)