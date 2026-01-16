import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Inisialisasi Environment
load_dotenv()

def audit_gemini_keys_with_remedy():
    print("="*60)
    print("💎 P.A.O. SYSTEM: ADVANCED GEMINI AUDIT & REMEDY 💎")
    print("="*60)

    # Mengambil kunci dari .env 
    keys = [
        os.getenv("GEMINI_API_KEY_1"),
        os.getenv("GEMINI_API_KEY_2"),
        os.getenv("GEMINI_API_KEY_3")
    ]

    for i, key in enumerate(keys, 1):
        if not key:
            print(f"\n[Key {i}] ❌ STATUS: Kunci Kosong")
            print(f"   💡 REKOMENDASI: Masukkan API Key di file .env pada variabel GEMINI_API_KEY_{i}")
            continue
            
        print(f"\n[Key {i}] Memeriksa Jalur Komunikasi... (Key: {key[:8]}...)")
        
        try:
            # Konfigurasi kunci
            genai.configure(api_key=key)
            
            # Memilih model yang paling stabil
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Tes pengiriman pesan ringan (Ping)
            response = model.generate_content("Ping")
            
            print(f"   ✅ STATUS: AKTIF")
            print(f"   🚀 RESPON: {response.text[:30]}...")
            
        except Exception as e:
            error_msg = str(e)
            print(f"   ❌ STATUS: GAGAL")
            
            # LOGIKA REKOMENDASI PERBAIKAN
            if "403" in error_msg:
                print(f"   ⚠️ DIAGNOSA: Regional Block / Permission Error")
                print(f"   💡 REKOMENDASI: Matikan VPN jika aktif, atau pastikan akun Google Anda")
                print(f"      memiliki akses ke Google AI Studio (aistudio.google.com).")
            elif "429" in error_msg:
                print(f"   ⚠️ DIAGNOSA: Rate Limit Reached (Kuota Habis)")
                print(f"   💡 REKOMENDASI: Akun ini sudah mencapai batas harian. Gunakan Akun {i+1}")
                print(f"      atau tunggu 24 jam untuk reset kuota gratis.")
            elif "API_KEY_INVALID" in error_msg or "400" in error_msg:
                print(f"   ⚠️ DIAGNOSA: Invalid API Key")
                print(f"   💡 REKOMENDASI: Kunci ini tidak valid atau salah ketik. Silakan")
                print(f"      generate ulang kunci baru di Google AI Studio.")
            else:
                print(f"   ⚠️ DIAGNOSA: Unknown Technical Error")
                print(f"   💡 REKOMENDASI: Perbarui library dengan 'pip install -U google-generativeai'")
                print(f"      atau cek koneksi internet Anda.")

    print("\n" + "="*60)
    print("🏁 AUDIT SELESAI. SISTEM SIAP UNTUK LANGKAH BERIKUTNYA.")
    print("="*60)

if __name__ == "__main__":
    audit_gemini_keys_with_remedy()