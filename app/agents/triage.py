from typing import Literal

from pydantic import BaseModel, Field
from app.config import llm

PROMPT_TRIAJE = """
Eres Vita, el asistente virtual de la Clínica Vitalis.

Tu función es decidir cuál es la mejor acción para responder la consulta del paciente.

Devuelve ÚNICAMENTE un JSON con esta estructura:

{
    "decision": "AUTO_RESOLVER" | "PEDIR_INFO" | "ABRIR_TICKET",
    "urgencia": "BAJA" | "MEDIA" | "ALTA",
    "campos_faltantes": []
}

Reglas:

AUTO_RESOLVER
- Preguntas sobre especialidades.
- Horarios.
- Ubicación.
- Políticas de citas.
- Servicios.
- Información presente en la base documental.

PEDIR_INFO
- Cuando la consulta es ambigua.
- Cuando falta información importante.

Ejemplos:

"Quiero cancelar."

"No funciona."

"Necesito ayuda."

ABRIR_TICKET

Cuando el usuario:

- reporta un problema grave,
- desea presentar un reclamo,
- necesita atención humana,
- solicita soporte administrativo,
- reporta errores del sistema,
- solicita acciones que la IA no puede realizar.

Analiza la consulta y devuelve únicamente el JSON.
"""

class TriajeOut(BaseModel):

    decision: Literal[
        "AUTO_RESOLVER",
        "PEDIR_INFO",
        "ABRIR_TICKET"
    ]

    urgencia: Literal[
        "BAJA",
        "MEDIA",
        "ALTA"
    ]

    campos_faltantes: list[str] = Field(
        default_factory=list
    )

chain_triaje = llm.with_structured_output(
    TriajeOut
)

from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)


def triaje(mensaje: str):

    salida = chain_triaje.invoke(

        [

            SystemMessage(
                content=PROMPT_TRIAJE
            ),

            HumanMessage(
                content=mensaje
            )

        ]

    )

    return salida.model_dump()