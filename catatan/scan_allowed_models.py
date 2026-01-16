import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def scan_my_keys():
    print("🔎 MENCARI MODEL YANG TERSEDIA UNTUK KUNCI ANDA...")
    key = os.getenv("GEMINI_API_KEY_1")
    genai.configure(api_key=key)
    
    try:
        # Meminta daftar model yang bisa dipakai oleh kunci ini
        available_models = genai.list_models()
        print("\n✅ Kunci Terhubung! Berikut model yang bisa Anda gunakan:")
        for m in available_models:
            if 'generateContent' in m.supported_generation_methods:
                print(f"👉 {m.name}")
    except Exception as e:
        print(f"❌ Gagal List Model: {e}")

if __name__ == "__main__":
    scan_my_keys()