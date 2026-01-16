import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

def hunt_niche():
    print("🔎 RADAR ALPHA: Mengaktifkan Jalur V3 (Direct Connection)...")
    key = os.getenv("GEMINI_API_KEY_1")
    client = genai.Client(api_key=key) 
    
    prompt = "Find 5 high-potential digital niches for late 2025. Output strict JSON with 'niches' list containing 'niche_name', 'score', and 'keyword_focus'."

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=prompt
        )
        
        text = response.text
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]
            
        data = json.loads(text.strip())
        for item in data['niches']:
            print(f"✅ Terdeteksi: {item['niche_name']} (Score: {item.get('score', 0)})")
        return data

    except Exception as e:
        print(f"❌ Radar Failure: {e}")
        return None