from app.intent_matcher import detect_intent

INTENT_WORKFLOW_MAP = {
    "balance_query": "EXISTING_USER_DB",
    "card_pin_change": "EXISTING_USER_DB",
    "card_delivery_estimate": "EXISTING_USER_DB",
    "refund_policy": "RAG",
    "fees_information": "RAG"
}

def route(query: str):
    result = detect_intent(query)

    if not result["confident"]:
        workflow = "FALLBACK"
    else:
        workflow = INTENT_WORKFLOW_MAP.get(
            result["intent"], "FALLBACK"
        )

    return {
        "query": query,
        "matched_intent": result["intent"],
        "confidence": result["confidence"],
        "workflow": workflow
    }
