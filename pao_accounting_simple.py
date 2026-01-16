import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class PAOAccounting:
    def __init__(self):
        self.log_file = "financial_legacy.json"
        self.amal_rate = float(os.getenv("AMAL_JARIYAH_PERCENT", 10)) / 100
        
    def record_transaction(self, unit_name, amount, currency="USD"):
        """ Mencatat transaksi masuk dan memisahkan porsi amal """
        amal_amount = amount * self.amal_rate
        net_profit = amount - amal_amount
        
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "unit": unit_name,
            "gross_amount": amount,
            "amal_jariyah": amal_amount,
            "net_profit": net_profit,
            "currency": currency
        }
        
        data = []
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                data = json.load(f)
        
        data.append(entry)
        
        with open(self.log_file, "w") as f:
            json.dump(data, f, indent=4)
            
        print(f"💰 Transaksi Tercatat! Unit: {unit_name} | Amal: {amal_amount} {currency}")

    def generate_report(self):
        """ Menampilkan total akumulasi amal dan profit """
        if not os.path.exists(self.log_file):
            print("📭 Belum ada data transaksi.")
            return

        with open(self.log_file, "r") as f:
            data = json.load(f)
            
        total_gross = sum(item['gross_amount'] for item in data)
        total_amal = sum(item['amal_jariyah'] for item in data)
        total_net = sum(item['net_profit'] for item in data)
        
        print("\n" + "="*40)
        print("📜 LAPORAN KEUANGAN IMPERIUM P.A.O")
        print("="*40)
        print(f"💵 Total Gross Revenue : {total_gross:,.2f}")
        print(f"🌿 Total Amal Jariyah  : {total_amal:,.2f} (WAJIB DISALURKAN)")
        print(f"💎 Net Profit Jenderal : {total_net:,.2f}")
        print("="*40)
        print(f"📊 Jumlah Transaksi    : {len(data)}")
        print("="*40)

if __name__ == "__main__":
    acc = PAOAccounting()
    # Contoh penggunaan jika ada closing di WhatsApp:
    # unit = input("Masukkan nama unit yang terjual: ")
    # nilai = float(input("Masukkan nilai transaksi: "))
    # acc.record_transaction(unit, nilai)
    acc.generate_report()