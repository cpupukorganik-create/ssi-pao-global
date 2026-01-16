import auditor_strategic
import datetime

def send_daily_report():
    print("\n" + "="*50)
    print(f"📢 LAPORAN OTOMATIS SYSTEM PAO - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*50)
    
    # Menjalankan fungsi audit yang sudah kita buat
    auditor_strategic.run_global_audit()
    
    print("\n[INFO] Laporan berhasil dibuat. System PAO Berjalan Normal.")
    print("="*50 + "\n")

if __name__ == "__main__":
    send_daily_report()