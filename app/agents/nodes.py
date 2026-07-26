from .state import AgentState
from app.rag.search import search_rag
from app.agents.triage import triaje
from app.rag.pipeline import retriever


def nodo_triaje(state: AgentState) -> AgentState:
    """
    Placeholder.
    En la siguiente clase llamará al modelo
    para decidir si usar RAG,
    pedir información o abrir ticket.
    """

    print("Ejecutando nodo 'triaje'...")

    return {
        "triaje": triaje(
            state["pregunta"]
        )
    }


def nodo_auto_resolver(state: AgentState) -> AgentState:

    print("Ejecutando nodo 'auto_resolver'...")

    respuesta_rag = search_rag(
    state["pregunta"],
    retriever
)
    update: AgentState = {

        "respuesta": respuesta_rag["answer"],

        "citaciones": respuesta_rag["citations"],

        "documentos_encontrados":
            respuesta_rag["documents_found"],

        "rag_exito":
            respuesta_rag["documents_found"]

    }

    if respuesta_rag["documents_found"]:

        update["accion_final"] = "AUTO_RESOLVER"

    else:

        update["accion_final"] = "PEDIR_INFO"

    return update


def nodo_pedir_info(state: AgentState) -> AgentState:

    print("Ejecutando nodo 'pedir_info'...")

    return {

        "respuesta": (
            "Necesito un poco más de información "
            "para poder ayudarte."
        ),

        "citaciones": [],

        "accion_final": "PEDIR_INFO"

    }


def nodo_abrir_ticket(state: AgentState) -> AgentState:

    print("Ejecutando nodo 'abrir_ticket'...")

    tri = state["triaje"]

    return {

        "respuesta": (
            f"Se debe generar un ticket "
            f"con prioridad {tri['urgencia']}."
        ),

        "citaciones": [],

        "accion_final": "ABRIR_TICKET"

    }