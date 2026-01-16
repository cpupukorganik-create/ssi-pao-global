import os
from google import genai
from dotenv import load_dotenv
from pao_legacy_core import LegacyVault

load_dotenv()
vault = LegacyVault()

def call_ai_orchestrator(prompt, task_type="content", niche="global"):
    key = os.getenv("GEMINI_API_KEY_1")
    client = genai.Client(api_key=key)
    
    affiliate_link = vault.get_affiliate_link(niche)
    enhanced_prompt = f"{prompt}\n\nIntegrate naturally: {affiliate_link}"

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=enhanced_prompt
        )
        return response.text
    except Exception as e:
        return f"Error V3 Conductor: {str(e)}"