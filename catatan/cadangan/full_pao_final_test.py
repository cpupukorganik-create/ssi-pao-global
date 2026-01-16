import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def run_ultimate_test():
    print("\n" + "="*50)
    print("💎 P.A.O. SYSTEM ULTIMATE DIAGNOSTIC (STABLE VERSION) 💎")
    print("="*50)

    # --- BAGIAN 1: MULTI-ACCOUNT GEMINI ---
    print("\n[1] TESTING MULTI-ACCOUNT GEMINI...")
    keys = [os.getenv(f"GEMINI_API_KEY_{i}") for i in range(1, 4)]
    
    for i, k in enumerate(keys, 1):
        if not k:
            continue
        success = False
        # Percobaan Jalur 1
        try:
            genai.configure(api_key=k)
            model = genai.GenerativeModel('gemini-1.5-flash')
            res = model.generate_content("Ping")
            print(f"   ✅ Key {i}: AKTIF (Jalur Utama)")
            success = True
        except Exception:
            # Percobaan Jalur 2 (Fallback Path)
            try:
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                res = model.generate_content("Ping")
                print(f"   ✅ Key {i}: AKTIF (Jalur Alternatif)")
                success = True
            except Exception as e:
                print(f"   ❌ Key {i}: GAGAL! (Cek API Key di Google AI Studio)")

    # --- BAGIAN 2: DEEPSEEK (AUTO-FALLBACK CHECK) ---
    print("\n[2] TESTING DEEPSEEK STRUCTURAL ENGINE...")
    try:
        url = f"{os.getenv('DEEPSEEK_BASE_URL')}/chat/completions"
        headers = {"Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"}
        res = requests.post(url, json={"model": "deepseek-chat", "messages": [{"role": "user", "content": "Hi"}]}, headers=headers, timeout=5)
        if res.status_code == 200:
            print("   ✅ DeepSeek: SIAP")
        else:
            print(f"   ⚠️ DeepSeek: Off-line (Status {res.status_code}). P.A.O. Conductor akan otomatis pakai Gemini.")
    except Exception:
        print("   ⚠️ DeepSeek: Tidak Terjangkau. Menggunakan Mode Full Gemini.")

    # --- BAGIAN 3: TELEGRAM ---
    print("\n[3] TESTING TELEGRAM NOTIFICATION...")
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": "🚀 P.A.O. System: Mesin AI Siap Tempur!"}, timeout=5)
        print("   ✅ Telegram: TERKONEKSI")
    except Exception:
        print("   ❌ Telegram: GAGAL")

    print("\n" + "="*50)
    print("🏁 DIAGNOSA SELESAI.")
    print("="*50)

if __name__ == "__main__":
    run_ultimate_test()