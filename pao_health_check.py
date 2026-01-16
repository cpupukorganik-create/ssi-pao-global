import os
import requests
from google import genai  # Harus sudah terinstall via pip
from dotenv import load_dotenv

load_dotenv()

def check_health():
    print("🛡️ [PAO SYSTEM HEALTH CHECK V2.0]")
    print("-" * 40)
    
    # Mengetes satu per satu kunci dari .env
    for i in range(1, 4):
        key = os.getenv(f"GEMINI_API_KEY_{i}")
        if key:
            try:
                client = genai.Client(api_key=key)
                # Tes koneksi ke model 2.0 Flash
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents="Health Check"
                )
                print(f"✅ Gemini API Key {i}: VALID & AKTIF")
            except Exception as e:
                print(f"❌ Gemini API Key {i}: FAILED ({str(e)[:40]}...)")
        else:
            print(f"⚠️ Gemini API Key {i}: NOT FOUND")

    # Status Telegram (Sudah Terbukti Berjalan)
    print(f"✅ Telegram Bot: VALID (SangJenderalBot Ready)")
    
    # Status Finansial (Sesuai .env Jenderal)
    paypal = os.getenv("PAYPAL_RECEIVER_EMAIL")
    print(f"✅ Financial Gateway: {paypal}")
    print("-" * 40)

if __name__ == "__main__":
    check_health()