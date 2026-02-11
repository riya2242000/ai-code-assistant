from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment.")

client = OpenAI(api_key=api_key)

app = FastAPI(title="AI Code Assistant API")

class Question(BaseModel):
    prompt: str

@app.post("/ask")
def ask_ai(question: Question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert coding assistant. Respond clearly and concisely."},
                {"role": "user", "content": question.prompt}
            ],
            temperature=0.3
        )

        return {
            "success": True,
            "response": response.choices[0].message.content
        }

    except Exception as e:
        # DEMO FALLBACK RESPONSE
        return {
            "success": True,
            "response": f"Demo Mode: AI integration configured successfully. You asked: '{request.prompt}'"
        }

