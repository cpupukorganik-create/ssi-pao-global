import os
import json
from dotenv import load_dotenv

load_dotenv()

class LegacyVault:
    """
    Brankas Rahasia Imperium P.A.O.
    Mengelola link afiliasi, pembagian hak Ummat, dan data sensitif.
    """
    def __init__(self):
        self.vault_path = "pao_legacy_core.json"
        self.load_vault()

    def load_vault(self):
        # Data default jika file belum ada
        default_data = {
            "monetization": {
                "primary_affiliate": "https://impact.com/your-link",
                "paypal_me": f"https://paypal.me/{os.getenv('PAYPAL_RECEIVER_EMAIL')}",
                "global_cta": "Secure Your Digital Identity Now"
            },
            "legacy_instructions": {
                "owner": "Sang Jenderal",
                "purpose": "Pendidikan 5 Putra-Putri & Amal Jariyah",
                "tithe_percent": int(os.getenv("AMAL_JARIYAH_PERCENT", 10))
            },
            "redirect_rules": {
                "/secure": "https://identity-tool-affiliate.com/ref=jenderal",
                "/vault": "https://hardware-wallet-provider.com/ref=jenderal"
            }
        }

        if not os.path.exists(self.vault_path):
            with open(self.vault_path, 'w') as f:
                json.dump(default_data, f, indent=4)
            self.data = default_data
        else:
            with open(self.vault_path, 'r') as f:
                self.data = json.load(f)

    def get_affiliate_link(self, niche="default"):
        # Logika memilih link berdasarkan niche (v4.2)
        return self.data["monetization"]["primary_affiliate"]

    def calculate_tithe(self, revenue):
        """Menghitung Hak Ummat 10% (Perisai Langit)"""
        return revenue * (self.data["legacy_instructions"]["tithe_percent"] / 100)

if __name__ == "__main__":
    vault = LegacyVault()
    print("✅ Brankas Rahasia Berhasil Diinisialisasi.")
    print(f"🎯 Misi: {vault.data['legacy_instructions']['purpose']}")