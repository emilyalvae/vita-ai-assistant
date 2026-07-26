from .state import AgentState

def arista_decision_triaje(state: AgentState):

    print("Decidiendo el flujo después del nodo 'triaje'...")

    decision = state["triaje"]["decision"]

    if decision == "AUTO_RESOLVER":
        return "rag"
    elif decision == "PEDIR_INFO":
        return "info"
    else:
        return "ticket"

KEYWORDS_ABRIR_TICKET = [
    "reclamo",
    "queja",
    "urgencia",
    "emergencia",
    "problema",
    "error",
    "administración",
    "recepción",
]

def arista_decision_rag(state: AgentState):

    print("Decidiendo el flujo después del nodo 'auto_resolver'...")

    if state["rag_exito"]:
        return "ok"

    pregunta = state["pregunta"].lower()

    if any(keyword in pregunta for keyword in KEYWORDS_ABRIR_TICKET):
        return "ticket"

    return "info"