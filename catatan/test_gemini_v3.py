import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def test_pao_v3():
    print("="*60)
    print("💎 P.A.O. SYSTEM: GEMINI 3 FLASH ACTIVATION 💎")
    print("="*60)

    key = os.getenv("GEMINI_API_KEY_1")
    
    try:
        # Menggunakan SDK terbaru dengan Model V3 yang terdeteksi
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents="Konfirmasi: Protokol Diamond P.A.O. System Aktif pada Jalur V3."
        )
        
        print(f"✅ STATUS: KONEKSI GEMINI 3 BERHASIL!")
        print(f"🚀 RESPON: {response.text[:100]}")
        
    except Exception as e:
        print(f"❌ GAGAL: {e}")

    print("="*60)

if __name__ == "__main__":
    test_pao_v3()