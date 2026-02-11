# AI Code Assistant API

Production-ready FastAPI backend integrating OpenAI API for structured coding assistance.

## Features
- FastAPI REST API
- OpenAI GPT integration
- Structured JSON responses
- Environment variable security
- Production error handling
- Swagger API docs

## Tech Stack
- Python
- FastAPI
- OpenAI SDK
- Uvicorn
- dotenv

## Run Locally

1. Create virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Add OPENAI_API_KEY to .env
4. Run:
   uvicorn main:app --reload

Visit:
http://127.0.0.1:8000/docs
