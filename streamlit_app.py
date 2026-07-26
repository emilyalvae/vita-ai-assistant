import streamlit as st

from app.agents.graph import graph


# Configuración página

st.set_page_config(
    page_title="Vita - Clínica Vitalis",
    page_icon="🏥"
)


# Título

st.title("🏥 Vita - Asistente Virtual")
st.write(
    "Hola, soy Vita, el asistente virtual de la Clínica Vitalis."
)


# Entrada usuario

pregunta = st.text_input(
    "¿En qué puedo ayudarte?"
)


# Botón

if st.button("Enviar"):

    if pregunta:

        with st.spinner("Vita está pensando..."):


            resultado = graph.invoke(
                {
                    "pregunta": pregunta
                }
            )


        st.subheader("Respuesta")

        st.write(
            resultado["respuesta"]
        )


        st.divider()


        st.subheader("Información del agente")


        col1, col2 = st.columns(2)


        with col1:

            st.write(
                "Decisión del triaje:"
            )

            st.info(
                resultado["triaje"]["decision"]
            )


        with col2:

            st.write(
                "Acción final:"
            )

            st.success(
                resultado["accion_final"]
            )


        # Citaciones

        if resultado["citaciones"]:

            st.divider()

            st.subheader(
                "📚 Fuentes utilizadas"
            )


            for i, documento in enumerate(
                resultado["citaciones"]
            ):

                with st.expander(
                    f"Citación {i+1}"
                ):

                    st.write(
                        documento.metadata["source"]
                    )

                    st.write(
                        documento.page_content
                    )

    else:

        st.warning(
            "Escribe una pregunta."
        )