from app.agents.graph import graph


mensajes_de_prueba = [
    "¿Qué especialidades médicas tiene la clínica?",
    "¿Cómo puedo cancelar una cita médica?",
    "Quiero presentar un reclamo.",
    "Necesito ayuda.",
    "¿Quién fue Napoleón Bonaparte?"
]


for pregunta in mensajes_de_prueba:

    resultado = graph.invoke(
        {
            "pregunta": pregunta
        }
    )

    print("\n==========================")

    print("\nPREGUNTA:")
    print(pregunta)

    print("\nDECISIÓN:")
    print(resultado["triaje"]["decision"])

    print("\nURGENCIA:")
    print(resultado["triaje"]["urgencia"])

    print("\nACCIÓN FINAL:")
    print(resultado["accion_final"])

    print("\nRESPUESTA:")
    print(resultado["respuesta"])


    if resultado["citaciones"]:

        print("\nCITACIONES:")

        for i, documento in enumerate(resultado["citaciones"]):

            print(f"\n--- Citación {i+1} ---")

            print(
                "Archivo:",
                documento.metadata["source"]
            )

            print(
                "Contenido:",
                documento.page_content[:300]
            )