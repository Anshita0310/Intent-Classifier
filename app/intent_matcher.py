from qdrant_client import QdrantClient
from app.embedder import get_embedding

import os
from dotenv import load_dotenv

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    https=True,
    timeout=60
)


CONFIDENCE_THRESHOLD = 0.75
MARGIN_THRESHOLD = 0.10

def detect_intent(query: str):
    query_vector = get_embedding(query)

    results = client.search(
        collection_name="banking77_intents",
        query_vector=query_vector,
        limit=3
    )

    top = results[0]
    second = results[1]

    confidence = top.score
    margin = top.score - second.score

    if confidence >= CONFIDENCE_THRESHOLD and margin >= MARGIN_THRESHOLD:
        return {
            "intent": top.payload["intent"],
            "confidence": round(confidence, 3),
            "confident": True
        }

    return {
        "intent": "UNKNOWN",
        "confidence": round(confidence, 3),
        "confident": False
    }