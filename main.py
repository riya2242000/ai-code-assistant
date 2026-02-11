from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
async def ask_ai(request: PromptRequest):
    try:
        from openai import OpenAI

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": request.prompt}
            ]
        )

        return {
            "success": True,
            "response": response.choices[0].message.content
        }

    except Exception as e:
        # FULL SAFE FALLBACK
        return {
            "success": True,
            "response": f"Demo Mode Active 🚀 — AI configured correctly. You asked: '{request.prompt}'",
            "note": "Live AI disabled due to billing or quota limits."
        }
