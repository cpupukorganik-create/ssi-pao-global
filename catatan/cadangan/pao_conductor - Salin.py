import os
import google.generativeai as genai
import requests
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()

# Konfigurasi Gilir Kunci Gemini
gemini_keys = [os.getenv("GEMINI_API_KEY_1"), os.getenv("GEMINI_API_KEY_2"), os.getenv("GEMINI_API_KEY_3")]
active_gemini_keys = [k for k in gemini_keys if k]
key_rotator = cycle(active_gemini_keys)

def call_ai_orchestrator(prompt, task_type="content"):
    # A. LOGIKA DEEPSEEK (Arsitek Struktur)
    if task_type == "structure":
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            return call_ai_orchestrator(prompt, task_type="content") # Fallback jika key kosong
            
        print("\n--- 🏗️ DEEPSEEK MODE: Membangun Struktur ---")
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        
        try:
            response = requests.post(f"{os.getenv('DEEPSEEK_BASE_URL')}/chat/completions", json=data, headers=headers, timeout=15)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                print(f"⚠️ DeepSeek Error {response.status_code}. Fallback ke Gemini...")
                return call_ai_orchestrator(prompt, task_type="content")
        except Exception as e:
            return call_ai_orchestrator(prompt, task_type="content")

    # B. LOGIKA GEMINI (Kurator Konten - Jalur Stabil)
    current_key = next(key_rotator)
    print(f"\n--- 💎 GEMINI MODE: Konten (Key: {current_key[:8]}...) ---")
    
    try:
        genai.configure(api_key=current_key)
        # Perbaikan Path Model untuk menghindari 404
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ Gemini Error: {e}. Mencoba kunci cadangan...")
        return call_ai_orchestrator(prompt, task_type="content")