import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def scan_model_pao():
    print("--- SCANNING MODELS FOR DIAMOND EDITION ---")
    try:
        # Mencari semua model yang mendukung instruksi 'generateContent'
        models = [m for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        print(f"Total Model Ditemukan: {len(models)}")
        pro_found = False
        
        for m in models:
            print(f"🔎 Tersedia: {m.name}")
            if "gemini-1.5-pro" in m.name:
                pro_found = True
        
        if pro_found:
            print("\n✅ STATUS: Gemini 1.5 Pro TERSEDIA!")
            # Tes Jabat Tangan dengan versi spesifik
            model = genai.GenerativeModel('gemini-1.5-pro-latest')
            res = model.generate_content("Konfirmasi: Protokol Diamond Aktif?")
            print(f"🚀 JAWABAN PRO: {res.text}")
        else:
            print("\n❌ ERROR: Model Pro tidak terdaftar dalam API Key ini.")
            
    except Exception as e:
        print(f"❌ KONEKSI GAGAL: {e}")

if __name__ == "__main__":
    scan_model_pao()