import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def tes_jalur_pasti():
    # Menggunakan ID model yang terdeteksi di log scan Anda sebelumnya
    model_name = "gemini-flash-latest"
    
    print(f"--- MENGAKTIFKAN LOGIKA PASTI {model_name.upper()} ---")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("P.A.O. System memanggil. Konfirmasi kesiapan operasional jalur Flash-Latest.")
        
        print(f"\n🚀 RESPON SISTEM: {response.text}")
        print(f"\n✅ ALHAMDULILLAH! Jalur {model_name} TERBUKA.")
        print("Sistem P.A.O. Diamond Edition resmi ONLINE.")
        
    except Exception as e:
        print(f"\n❌ DIAGNOSA LANJUTAN: {e}")

if __name__ == "__main__":
    tes_jalur_pasti()