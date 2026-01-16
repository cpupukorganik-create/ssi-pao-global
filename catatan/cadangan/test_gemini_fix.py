import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def audit_final_pao():
    print("="*60)
    print("💎 P.A.O. SYSTEM: API PATH RE-CALIBRATION 💎")
    print("="*60)

    keys = [os.getenv(f"GEMINI_API_KEY_{i}") for i in range(1, 4)]
    
    for i, key in enumerate(keys, 1):
        if not key: continue
        
        print(f"\n[Key {i}] Menguji Jalur Stabil... ({key[:8]}...)")
        try:
            # Inisialisasi Client
            client = genai.Client(api_key=key)
            
            # Mencoba model dengan ID paling dasar
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents="Konfirmasi koneksi P.A.O. Diamond."
            )
            
            print(f"   ✅ STATUS: AKTIF")
            print(f"   🚀 RESPON: {response.text[:40]}...")
            
        except Exception as e:
            error_str = str(e)
            print(f"   ❌ STATUS: GAGAL")
            
            # Jika masih 404, berikan diagnosa spesifik
            if "404" in error_str:
                print(f"   ⚠️ DIAGNOSA: Model 'gemini-1.5-flash' tidak ditemukan di akun ini.")
                print(f"   💡 SARAN: Cek apakah API Key ini dibuat di Google AI Studio")
                print(f"      dan pastikan model 'Gemini 1.5 Flash' tersedia di sana.")
            else:
                print(f"   ⚠️ DETAIL: {error_str[:100]}")

    print("\n" + "="*60)

if __name__ == "__main__":
    audit_final_pao()