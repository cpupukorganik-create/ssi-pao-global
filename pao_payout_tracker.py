import json
import os
from datetime import datetime, timedelta

def get_payout_schedule():
    """
    Menghitung jadwal monitoring saldo berdasarkan umur Batch.
    Asumsi: Merchant membayar 30 hari setelah unit aktif (Net-30).
    """
    vault_path = 'merchant_vault.json'
    history_path = 'payout_history.json'
    
    if not os.path.exists(vault_path):
        return "⚠️ Brankas belum ada."

    try:
        with open(vault_path, 'r') as f:
            vault = json.load(f)
        
        print("\n" + "="*45)
        print("     📅 JADWAL MONITORING SALDO PAYPAL")
        print("="*45)
        print(f"{'NICHE':<18} | {'BATCH':<8} | {'EST. PAYOUT'}")
        print("-" * 45)

        for niche, data in vault.items():
            # Simulasi tanggal peluncuran (kita ambil tanggal hari ini sebagai contoh)
            # Di sistem nyata, ini diambil dari metadata folder
            launch_date = datetime.now() 
            payout_date = launch_date + timedelta(days=30) # Estimasi Net-30
            
            print(f"{niche[:15]:<18} | {data['current_batch']:<8} | {payout_date.strftime('%d %b %Y')}")
            
        print("-" * 45)
        print("💡 Tips: Cek email PayPal 2 hari sebelum tanggal di atas.")
        print("="*45)

    except Exception as e:
        print(f"⚠️ Gagal memuat jadwal: {e}")

if __name__ == "__main__":
    get_payout_schedule()