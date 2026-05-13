# AI Knowledge Engine

> Ein KI-gestütztes Wissensmanagementsystem – PDFs hochladen, Fragen stellen, Antworten erhalten.

---

## Inhaltsverzeichnis

- [Projektbeschreibung](#projektbeschreibung)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Projektstruktur](#projektstruktur)
- [Installation](#installation)
- [Starten der Anwendung](#starten-der-anwendung)
- [API-Übersicht](#api-übersicht)
- [Entstehung](#entstehung)

---

## Projektbeschreibung

Der **AI Knowledge Engine** ist ein vollständiges RAG-System (**Retrieval-Augmented Generation**), das es ermöglicht, eigene PDF-Dokumente hochzuladen und diese anschließend per natürlicher Sprache zu befragen. Das System extrahiert den Text, speichert ihn als semantische Vektoren und beantwortet Fragen präzise auf Basis der eigenen Inhalte – ohne Halluzinationen durch externes Wissen.

Das Projekt eignet sich für persönliche Wissensdatenbanken, interne Dokumentensuche oder als Grundlage für produktive KI-Assistenten.

---

## Features

- **PDF-Upload** – Dokumente per Drag-and-Drop oder API hochladen
- **Semantische Suche** – relevante Textabschnitte werden per Vektorähnlichkeit gefunden
- **KI-Antworten** – Google Gemini generiert präzise Antworten auf Basis des Dokumenteninhalts
- **Quellenangaben** – jede Antwort enthält die verwendeten Textstellen mit Score und Herkunft
- **REST API** – vollständig dokumentierte API via FastAPI und interaktives Swagger UI
- **Web-Frontend** – einfaches HTML-Interface direkt im Browser nutzbar
- **Health Check** – Endpunkt zur Systemüberwachung

---

## Tech Stack

| Komponente | Technologie |
|---|---|
| **Backend-Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Vektordatenbank** | [ChromaDB](https://www.trychroma.com/) |
| **KI-Modell** | [Google Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/) |
| **PDF-Verarbeitung** | [pypdf](https://pypdf.readthedocs.io/) |
| **Programmiersprache** | Python 3.11+ |
| **Server** | Uvicorn (ASGI) |

---

## Projektstruktur

```
AI-Knowledge-Engine/
├── src/
│   ├── main.py               # FastAPI-Anwendung & Routing
│   ├── routers/
│   │   ├── documents.py      # PDF-Upload-Endpunkt
│   │   ├── query.py          # Frage-Antwort-Endpunkt
│   │   └── health.py         # Health-Check-Endpunkt
│   └── services/
│       ├── pdf.py            # Textextraktion & Chunking
│       ├── vectorstore.py    # ChromaDB-Integration
│       └── llm.py            # Google Gemini-Integration
├── static/
│   └── index.html            # Web-Frontend
├── data/
│   └── chromadb/             # Lokale Vektordatenbank
├── docs/                     # Dokumentation
├── requirements.txt
├── .env                      # API-Keys (nicht eingecheckt)
└── README.md
```

---

## Installation

### Voraussetzungen

- Python 3.11 oder höher
- Ein Google Gemini API-Key ([kostenlos erhältlich](https://aistudio.google.com/))

### 1. Repository klonen

```bash
git clone https://github.com/sarehbahrani/AI-Knowledge-Engine.git
cd AI-Knowledge-Engine
```

### 2. Virtuelle Umgebung erstellen und aktivieren

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 4. Umgebungsvariablen konfigurieren

Eine `.env`-Datei im Projektverzeichnis anlegen:

```env
GEMINI_API_KEY=dein_api_key_hier
```

---

## Starten der Anwendung

```bash
uvicorn src.main:app --reload
```

Die Anwendung ist nun erreichbar unter:

| URL | Beschreibung |
|---|---|
| `http://localhost:8000` | Web-Frontend |
| `http://localhost:8000/docs` | Interaktives API-Dokumentation (Swagger UI) |
| `http://localhost:8000/health` | Health Check |

---

## API-Übersicht

### PDF hochladen

```http
POST /documents/upload
Content-Type: multipart/form-data

file: <PDF-Datei>
```

### Wissensbasis befragen

```http
POST /query
Content-Type: application/json

{
  "question": "Was sind die wichtigsten Erkenntnisse?",
  "n_results": 3
}
```

**Antwort:**

```json
{
  "question": "Was sind die wichtigsten Erkenntnisse?",
  "answer": "Basierend auf dem Dokument ...",
  "sources": [
    {
      "text": "...",
      "source": "dokument.pdf",
      "chunk_index": 4,
      "score": 0.91
    }
  ]
}
```

---

## Entstehung

Dieses Projekt wurde entwickelt mit:

- **[Claude Code](https://claude.ai/code)** von Anthropic – KI-gestützte Entwicklungsumgebung für schnelles, qualitativ hochwertiges Software-Engineering
- **Graphify-Methode** – ein strukturierter Ansatz zur iterativen Entwicklung und Visualisierung von KI-Systemen

---

<p align="center">
  Built with Claude Code &nbsp;·&nbsp; Graphify Method &nbsp;·&nbsp; Python
</p>
