import os
import shutil

# --- KONFIGURASI AMBANG BATAS ---
TARGET_DIR = 'pao_factory'
MAX_SIZE_MB = 24.5  # Batas aman Cloudflare

def fast_precision_purge():
    print(f"🚀 Memulai Mekanisme Klasifikasi & Eksekusi di: {TARGET_DIR}")
    
    if not os.path.exists(TARGET_DIR):
        print("❌ Folder target tidak ditemukan!")
        return

    units = [d for d in os.listdir(TARGET_DIR) if os.path.isdir(os.path.join(TARGET_DIR, d))]
    
    count_slim = 0
    count_fat = 0
    
    print("-" * 50)
    for unit in units:
        unit_path = os.path.join(TARGET_DIR, unit)
        index_path = os.path.join(unit_path, 'index.html')
        
        if os.path.exists(index_path):
            # Timbang berat file tanpa membukanya (Hemat Memori)
            file_size_mb = os.path.getsize(index_path) / (1024 * 1024)
            
            if file_size_mb > MAX_SIZE_MB:
                print(f"💀 [GEMUK] {unit} ({file_size_mb:.2f} MB) -> LANGSUNG DIHAPUS")
                shutil.rmtree(unit_path)
                count_fat += 1
            else:
                # File kecil tetap dipertahankan
                count_slim += 1
    
    print("-" * 50)
    print(f"📊 LAPORAN KLASIFIKASI FINAL:")
    print(f"✅ Pasukan Sehat (Tetap Ada): {count_slim} Unit")
    print(f"🗑️ Pasukan Gemuk (Telah Musnah): {count_fat} Unit")
    print("-" * 50)
    print("Selesai! Sekarang folder Anda sudah bersih dari penghambat Cloudflare.")

if __name__ == "__main__":
    fast_precision_purge()