from langgraph.graph import START, END, StateGraph

from .state import AgentState
from .nodes import (
    nodo_triaje,
    nodo_auto_resolver,
    nodo_pedir_info,
    nodo_abrir_ticket,
)
from .edges import arista_decision_triaje, arista_decision_rag

workflow = StateGraph(AgentState)


workflow.add_node("triaje", nodo_triaje)
workflow.add_node("auto_resolver", nodo_auto_resolver)
workflow.add_node("pedir_info", nodo_pedir_info)
workflow.add_node("abrir_ticket", nodo_abrir_ticket)

workflow.add_edge(START, "triaje")

workflow.add_conditional_edges(
    "triaje",
    arista_decision_triaje,
    {
        "rag": "auto_resolver",
        "info": "pedir_info",
        "ticket": "abrir_ticket",
    },
)

workflow.add_conditional_edges(
    "auto_resolver",
    arista_decision_rag,
    {
        "ok": END,
        "info": "pedir_info",
        "ticket": "abrir_ticket",
    },
)

workflow.add_edge("pedir_info", END)
workflow.add_edge("abrir_ticket", END)

graph = workflow.compile()