import time
import os
import shutil
import subprocess
from niche_hunter import hunt_niche
from pao_factory_manager import PAOFactory
from generate_sitemap import generate_global_sitemap
from index_manager import update_index_html, generate_imperial_dashboard
from pao_super_injector import super_revenue_injection
from pao_telegram_bot import notify_jenderal  # <--- Integrasi Intelijen
from dotenv import load_dotenv

load_dotenv()

def run_emperor_loop(iterations=1):
    print(f"👑 IMPERIAL LOOP V7.5 - STATUS: TELEGRAM SYNC ACTIVE")
    factory = PAOFactory()

    for i in range(iterations):
        print(f"\n📡 MEMPRODUKSI GELOMBANG KE-{i+1}...")
        try:
            niches_data = hunt_niche()
            if not niches_data:
                continue

            for item in niches_data.get('niches', []):
                # 1. Produksi Unit
                file_path = factory.create_unit(item['niche_name'], item['keyword_focus'])
                
                # 2. Ambil Nama Folder untuk Laporan
                folder_slug = os.path.basename(os.path.dirname(file_path))
                live_url = f"https://ssi-pao-global.pages.dev/pao_factory/{folder_slug}/"
                
                # 3. KIRIM LAPORAN INTELIJEN KE TELEGRAM
                report_msg = (
                    f"✅ <b>UNIT BARU TERDETEKSI</b>\n"
                    f"Niche: {item['niche_name']}\n"
                    f"Status: DNA V8.0 Active\n"
                    f"URL: {live_url}"
                )
                notify_jenderal(report_msg)
                
                time.sleep(1)

            # 4. Injeksi Massal DNA V8.0
            super_revenue_injection()

        except Exception as e:
            notify_jenderal(f"❌ <b>GANGGUAN PRODUKSI:</b>\n{str(e)}")

    # --- SINKRONISASI GLOBAL ---
    generate_global_sitemap()
    generate_imperial_dashboard()
    
    # Konsolidasi & Deploy (Pastikan folder fleet_deployment siap)
    # ... (logika deployment Jenderal tetap sama)
    
    notify_jenderal("🏁 <b>MISI SELESAI:</b> Armada Global telah diperbarui.")

if __name__ == "__main__":
    iterasi = int(input("Masukkan jumlah gelombang (contoh: 5): "))
    run_emperor_loop(iterasi)