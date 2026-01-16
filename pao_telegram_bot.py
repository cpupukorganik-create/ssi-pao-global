import os
import requests
from dotenv import load_dotenv

load_dotenv()

class PAOTelegramGuard:
    def __init__(self):
        # Ambil kredensial dari .env (Jenderal harus membuat Bot via @BotFather)
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send_report(self, message):
        """ Mengirimkan laporan intelijen langsung ke HP Jenderal """
        if not self.token or not self.chat_id:
            print("⚠️ Telegram Credentials belum diset di .env")
            return

        payload = {
            "chat_id": self.chat_id,
            "text": f"🛡️ [PAO COMMAND CENTER]\n\n{message}",
            "parse_mode": "HTML"
        }
        
        try:
            response = requests.post(self.api_url, data=payload)
            return response.json()
        except Exception as e:
            print(f"❌ Gagal mengirim laporan Telegram: {e}")

# Fungsi Instan untuk Notifikasi Darurat (Ide No. 4)
def notify_jenderal(msg):
    guard = PAOTelegramGuard()
    guard.send_report(msg)

if __name__ == "__main__":
    # Uji coba koneksi pertama
    notify_jenderal("<b>STATUS: AKTIF</b>\nSistem Intelijen P.A.O V8.0 siap melapor, Jenderal!")