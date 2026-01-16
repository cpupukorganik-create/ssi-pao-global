import os
import random
from google import genai
from dotenv import load_dotenv

load_dotenv()

# DAFTAR KUNCI API UNTUK ROTASI
API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3")
]

def call_ai_orchestrator(prompt):
    # Memilih kunci secara acak untuk distribusi beban (Load Balancing)
    active_key = random.choice([k for k in API_KEYS if k])
    try:
        client = genai.Client(api_key=active_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Act as an SEO Expert & Web Developer. {prompt}"
        )
        return response.text
    except Exception as e:
        print(f"❌ API Error: {e}. Switching logic activated.")
        return "<html><body>Protocol Diamond: Maintenance Mode.</body></html>"