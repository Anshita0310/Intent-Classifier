from datasets import load_dataset
from qdrant_client import QdrantClient
from app.embedder import get_embedding
import uuid
dataset = load_dataset("PolyAI/banking77", split="train")


import os
from dotenv import load_dotenv

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    https=True,
    timeout=60
)

# Create collection
client.recreate_collection(
    collection_name="banking77_intents",
    vectors_config={
        "size": 768,
        "distance": "Cosine"
    }
)

points = []

for row in train_data:
    vector = get_embedding(row["text"])
    points.append({
        "id": str(uuid.uuid4()),
        "vector": vector,
        "payload": {
            "intent": row["label"],
            "text": row["text"]
        }
    })

client.upsert(
    collection_name="banking77_intents",
    points=points
)

print("✅ Banking77 indexed into Qdrant")
