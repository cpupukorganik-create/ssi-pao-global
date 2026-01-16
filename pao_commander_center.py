import os
import time
from datetime import datetime
import pywhatkit
from dotenv import load_dotenv

# Import Modul Internal PAO
import auditor_strategic
import pao_factory_manager
import revenue_injector_final
import Direct_Merchant_hunter 
import pao_automator         
import pao_analytics_helper  
import pao_payout_tracker 

load_dotenv()
OWNER_WA = os.getenv("OWNER_WHATSAPP")
OWNER_NAME = os.getenv("OWNER_NAME")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sync_new_merchant():
    """Protokol Ganti Niche dengan Panduan Langsung dari Brankas/Intelijen"""
    clear_screen()
    print("--- 🕵️ PROTOKOL HUNT & SYNC (GANTI AMUNISI) ---")
    
    # 1. Tampilkan Label yang Valid agar CEO bisa mengetik dengan tepat
    print("\n[ 💡 DAFTAR LABEL AMUNISI DI BRANKAS ]")
    print("------------------------------------------")
    print(" > AI_TOOLS")
    print(" > CAREER_PIVOT")
    print(" > DIGITAL_MARKETING")
    print(" > CLOUD_SECURITY")
    print("------------------------------------------")
    print("INFO: Masukkan nama di atas (Contoh: Cloud Security)")
    print("------------------------------------------\n")

    # 2. Minta Input
    niche = input("✍️  Masukkan Niche Target Baru: ")
    
    print(f"\n🔎 Memproses sinkronisasi untuk: {niche}...")
    
    # Normalisasi Input (Menghapus spasi dan ubah ke UPPERCASE)
    niche_key = niche.upper().replace(" ","_")
    new_link = Direct_Merchant_hunter.get_final_link(niche_key)
    
    if new_link:
        print(f"✅ LINK DITEMUKAN: {new_link}")
        print(f"🔄 Mengunci target pada niche: {niche_key}...")
        time.sleep(2)
        print(f"✅ SISTEM SIAP: Batch berikutnya akan menggunakan {niche_key}!")
    else:
        print(f"⚠️ Kunci '{niche_key}' TIDAK DITEMUKAN di Brankas.")
        print("💡 Pastikan label tersebut sudah ada di merchant_vault.json")
    
    input("\nTekan Enter untuk kembali ke Dashboard...")

def main_dashboard():
    while True:
        clear_screen()
        
        # --- LOGIKA DASHBOARD DINAMIS ---
        batches, total_units = pao_analytics_helper.get_batch_stats()
        progress_pct = (total_units / 10000) * 100
        filled_length = int(progress_pct / 5)
        bar = '█' * filled_length + '-' * (20 - filled_length)
        
        # Rumus Estimasi Konservatif: $0.05 per unit per bulan
        potensi_dolar = total_units * 0.05
        # --------------------------------

        print("====================================================")
        print("      💎 IMPERIUM P.A.O. COMMAND CENTER 💎          ")
        print(f"      Owner: {OWNER_NAME} | Ver: 5.7-Precision      ")
        print("----------------------------------------------------")
        print(f" 📊 STATS   : {total_units} Units | {batches} Batches Active")
        print(f" 🎯 TARGET  : |{bar}| {progress_pct:.1f}%")
        print(f" 💰 POTENSI : ${potensi_dolar:,.2f} USD / Bulan (Estimasi)")
        print("====================================================")
        print(" [1] 🏛️  AUDIT ASSET (Check Strategy & Niche)")
        print(" [2] 🚀 PRODUKSI MASSAL (Build 200 Units)")
        print(" [3] 💸 INJEKSI DOLAR (Waterfall Monetization)")
        print(" [4] ⚡ FULL AUTO-PILOT (Luncurkan Batch)")
        print(" [5] 📅 CEK JADWAL PAYOUT (Monitoring Saldo)")
        print(" [6] 🏛️  OPEN EXECUTIVE BOARD (Manajerial)")
        print(" [7] 🕵️  HUNT & SYNC (Ganti Niche Target)")
        print(" [0] 🚪 KELUAR")
        print("----------------------------------------------------")
        
        choice = input("Pilih Operasi (0-7): ")

        if choice == '1':
            auditor_strategic.run_global_audit()
            input("\nTekan Enter...")
        
        elif choice == '2':
            pao_factory_manager.build_factory_imperium()
            input("\nSelesai. Tekan Enter...")
        
        elif choice == '3':
            revenue_injector_final.mass_revenue_deployment()
            input("\nSelesai. Tekan Enter...")
            
        elif choice == '4':
            print("\n🌀 MENJALANKAN PROTOKOL AUTO-PILOT...")
            # Produksi & Injeksi Otomatis
            pao_factory_manager.build_factory_imperium()
            revenue_injector_final.mass_revenue_deployment()
            
            pao_analytics_helper.summarize_factory_batches()
            print("🏆 BATCH SELESAI DILUNCURKAN!")
            time.sleep(3)

        elif choice == '5':
            clear_screen()
            pao_payout_tracker.get_payout_schedule()
            input("\nTekan Enter untuk kembali...")

        elif choice == '6':
            print("\n🔄 Melompat ke Ruang CEO...")
            time.sleep(1)
            try:
                import pao_manager_board
                pao_manager_board.main_managerial()
            except:
                print("⚠️ Gagal memanggil Manager Board.")

        elif choice == '7':
            sync_new_merchant()

        elif choice == '0':
            print(f"Sampai jumpa, Sodaraku {OWNER_NAME}. Imperium Tetap Berjalan!")
            break
        else:
            print("⚠️ Pilihan tidak valid.")
            time.sleep(1)

if __name__ == "__main__":
    main_dashboard()