# 🎯 Intent Classifier

A production-ready intent classification API built with **FastAPI**, **Google Gemini**, and **Qdrant**. User queries are embedded using Gemini's generative AI, stored and searched in a Qdrant vector database, and matched to the closest known intent — enabling fast, semantic intent detection without traditional ML training loops.

---

## How It Works

1. **Ingestion** — Intent examples are embedded using the Google Generative AI API and stored as vectors in a Qdrant collection (`scripts/`)
2. **Classification** — When a query arrives via the FastAPI endpoint, it is embedded with the same model and a nearest-neighbour search is run against Qdrant
3. **Response** — The closest matching intent label is returned along with a similarity score

This approach is embedding-based rather than fine-tuning-based, making it easy to add or update intents without retraining a model.

---

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI + Uvicorn |
| LLM / Embeddings | Google Generative AI (`google-generativeai`) |
| Vector Store | Qdrant (`qdrant-client`) |
| Data Handling | Hugging Face Datasets, Pandas, NumPy |
| Config | `python-dotenv` |
| Language | Python 3 |

---

## Project Structure

```
Intent-Classifier/
├── app/                    # FastAPI application
│   └── ...                 # Routes, models, classifier logic
├── scripts/                # Data ingestion & vector indexing scripts
│   └── ...                 # Embed intents and upsert to Qdrant
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.9+
- A running [Qdrant](https://qdrant.tech/) instance (local or cloud)
- A [Google AI Studio](https://aistudio.google.com/) API key for Gemini

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Anshita0310/Intent-Classifier.git
cd Intent-Classifier
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_generative_ai_key
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_api_key   # if using Qdrant Cloud
```

### 5. Start Qdrant (local)

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

## Usage

### Step 1 — Index your intents

Run the ingestion script to embed your intent dataset and load it into Qdrant:

```bash
python scripts/ingest.py
```

### Step 2 — Start the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Step 3 — Classify a query

```bash
curl -X POST "http://localhost:8000/classify" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather like today?"}'
```

Example response:

```json
{
  "intent": "weather_query",
  "score": 0.94
}
```

### Interactive API Docs

FastAPI provides auto-generated documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Dependencies

```
fastapi
uvicorn
python-dotenv
google-generativeai
qdrant-client
datasets==2.14.5
pyarrow==12.0.1
numpy==1.26.4
pandas==2.1.4
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project does not currently specify a license. All rights reserved by the author.
