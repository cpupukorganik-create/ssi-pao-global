import os
import time
from datetime import datetime
from dotenv import load_dotenv
import pao_intelijen

load_dotenv()
OWNER_NAME = os.getenv("OWNER_NAME")

def count_real_assets():
    """Menghitung jumlah unit web asli di folder produksi"""
    path = "pao_factory"
    if not os.path.exists(path):
        return 0
    # Menghitung folder di dalam pao_factory
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return len(folders)

def revenue_report():
    os.system('cls' if os.name == 'nt' else 'clear')
    total_unit = count_real_assets()
    target_rev = 1.0 # Target $1 per unit
    potential_daily = total_unit * target_rev
    
    print("====================================================")
    print("      📈 REAL-TIME REVENUE ANALYTICS (RIIL)         ")
    print("====================================================")
    print(f" 🏭 Total Aset Riil di Folder: {total_unit} Unit")
    print(f" 🎯 Target Revenue/Unit    : ${target_rev}")
    print(f" 💰 Estimasi Bruto/Hari    : ${potential_daily}")
    print("-" * 50)
    
    percent_amal = int(os.getenv("AMAL_JARIYAH_PERCENT", 10))
    amal_nominal = potential_daily * (percent_amal / 100)
    print(f" 🌙 Alokasi Amal ({percent_amal}%): ${amal_nominal:.2f}")
    print(f" 💎 Profit Bersih CEO      : ${potential_daily - amal_nominal:.2f}")
    print("====================================================")
    print(" *Data berdasarkan jumlah folder di /pao_factory")
    input("\nTekan Enter untuk kembali...")

def main_managerial():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================================")
        print("      💎 IMPERIUM P.A.O. EXECUTIVE BOARD 💎          ")
        print(f"      CEO: {OWNER_NAME}                             ")
        print("====================================================")
        print(" [1] 📈 REAL REVENUE ANALYTICS")
        print(" [2] 🧠 INTELLIGENCE REPORT")
        print(" [3] 🌍 MARKET EXPANSION")
        print(" [4] 💰 WITHDRAWAL PROTOCOL")
        print(" [5] 🛠️  OPEN COMMANDER CENTER (Operasional)")
        print(" [0] 🚪 EXIT STRATEGY")
        print("----------------------------------------------------")
        
        choice = input("Pilih Keputusan Strategis (0-5): ")
        if choice == '1': revenue_report()
        elif choice == '2':
            niche = pao_intelijen.evaluasi_performa_niche()
            print(f"\n🧠 Rekomendasi: Fokus Niche {niche}"); input("Enter...")
        elif choice == '5':
            print("\n🔄 Melompat ke Lantai Operasional..."); time.sleep(1)
            import pao_commander_center
            pao_commander_center.main_dashboard() # Langsung panggil fungsinya
        elif choice == '0': break

if __name__ == "__main__":
    main_managerial()