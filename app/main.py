from fastapi import FastAPI
from scripts import route

app = FastAPI(title="Semantic Intent Routing Demo")

@app.post("/route")
def route_query(payload: dict):
    query = payload.get("query")
    return route(query)
