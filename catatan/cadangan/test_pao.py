import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load kunci dari brankas .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("--- MENGAKTIFKAN LOGIKA GEMINI 2.5 PRO ---")
try:
    # Mengunci ke model tercanggih yang tersedia di akun Anda
    model = genai.GenerativeModel('gemini-2.5-pro')
    res = model.generate_content("Konfirmasi Protokol P.A.O. Diamond Edition. Apakah Anda siap untuk ekspansi pasar global?")
    print(f"\n🚀 RESPON PRO: {res.text}")
    print("\n✅ KONEKSI SEMPURNA. DNA DIAMOND AKTIF!")
except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")