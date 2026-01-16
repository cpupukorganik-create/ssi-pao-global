import os
import time
from dotenv import load_dotenv
import pao_intelijen
import pao_analytics_helper  # Diperlukan untuk menghitung batch yang sudah ada

load_dotenv()

def build_factory_imperium(revisi_mode=False):
    """
    Fungsi Utama: Mencetak 200 Unit Baru dengan penamaan Batch yang Unik.
    Menjamin Progress Bar di Dashboard bertambah (tidak menimpa folder lama).
    """
    # 1. Tentukan Niche
    niche = pao_intelijen.evaluasi_performa_niche() if revisi_mode else "Niche-Superior-AI"
    
    # 2. Pastikan Folder Induk 'pao_factory' Ada
    base_path = "pao_factory"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"📁 Folder Utama '{base_path}' diciptakan.")

    # 3. Tentukan Nomor Batch Berikutnya
    # Kita ambil data batch yang sudah ada, lalu tambah 1
    current_batch_count, _ = pao_analytics_helper.get_batch_stats()
    next_batch_num = current_batch_count + 1
    
    print(f"🚀 Memulai Produksi Fisik BATCH-{next_batch_num:02d} | Niche: {niche}")
    print("------------------------------------------------------------")

    # 4. Produksi 200 Unit Baru dengan Label Batch yang Unik
    success_count = 0
    for i in range(1, 201):
        # KUNCI: Nama folder unik agar tidak menimpa hasil sebelumnya
        unit_name = f"B{next_batch_num:02d}-U{i:03d}-{niche.lower()[:10]}"
        unit_dir = os.path.join(base_path, unit_name)
        
        try:
            if not os.path.exists(unit_dir):
                os.makedirs(unit_dir)
            
            index_path = os.path.join(unit_dir, "index.html")
            
            # Template HTML dengan placeholder untuk Injeksi Dolar
            html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{niche} - Batch {next_batch_num}</title>
    <style>
        body {{ font-family: sans-serif; text-align: center; background: #fafafa; padding: 40px; }}
        .card {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.08); display: inline-block; }}
        .cta {{ background: #0070ba; color: white; padding: 18px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>{niche} Mastery</h2>
        <p>Deployment ID: {unit_name}</p>
        <br><br>
        <a href="#" class="cta">SECURE YOUR ACCESS</a>
    </div>
</body>
</html>"""

            with open(index_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            
            success_count += 1
            if i % 50 == 0:
                print(f"✅ {i} Unit baru dari Batch {next_batch_num} telah berdiri...")
                
        except Exception as e:
            print(f"⚠️ Error pada unit {i}: {e}")

    print("------------------------------------------------------------")
    print(f"🏆 TOTAL PRODUKSI BARU: {success_count} Unit")
    print(f"📊 BATCH {next_batch_num} SELESAI. Silakan cek Progress Bar di Dashboard!")

if __name__ == "__main__":
    build_factory_imperium()