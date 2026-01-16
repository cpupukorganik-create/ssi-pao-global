import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def audit_modern_pao():
    print("="*60)
    print("💎 P.A.O. SYSTEM: MODERN SDK DIAGNOSTIC 💎")
    print("="*60)

    keys = [os.getenv(f"GEMINI_API_KEY_{i}") for i in range(1, 4)]
    
    for i, key in enumerate(keys, 1):
        if not key: continue
        
        print(f"\n[Key {i}] Menguji Jalur Modern... ({key[:8]}...)")
        try:
            # Inisialisasi menggunakan SDK terbaru
            client = genai.Client(api_key=key)
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents="Konfirmasi koneksi P.A.O. System."
            )
            print(f"   ✅ STATUS: AKTIF")
            print(f"   🚀 RESPON: {response.text[:40]}...")
        except Exception as e:
            print(f"   ❌ STATUS: GAGAL")
            print(f"   ⚠️ DETAIL: {str(e)[:100]}")

    print("\n" + "="*60)

if __name__ == "__main__":
    audit_modern_pao()