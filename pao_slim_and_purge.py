import os
import shutil

# --- KONFIGURASI STRATEGIS ---
TARGET_DIR = 'pao_factory'
MAX_SIZE_MB = 24.5  # Batas aman Cloudflare (25MB)
RETRY_LIMIT = 3

def slim_html_content(content):
    """
    Mendeteksi dan menghapus penyebab file gemuk:
    1. Menghapus Base64 Images yang sangat panjang (Penyebab utama)
    2. Menghapus komentar HTML yang tidak perlu
    """
    import re
    # Hapus Gambar Base64 (data:image/...;base64,xxxx)
    clean_content = re.sub(r'data:image\/[^;]+;base64,[^"\'\s>]+', '#removed_large_image#', content)
    # Hapus komentar HTML
    clean_content = re.sub(r'', '', clean_content, flags=re.DOTALL)
    return clean_content

def process_units():
    print(f"🚀 Memulai Pemindaian Infrastruktur di: {TARGET_DIR}")
    
    if not os.path.exists(TARGET_DIR):
        print("❌ Folder tidak ditemukan!")
        return

    units = [d for d in os.listdir(TARGET_DIR) if os.path.isdir(os.path.join(TARGET_DIR, d))]
    total_deleted = 0
    total_slimmed = 0

    for unit in units:
        unit_path = os.path.join(TARGET_DIR, unit)
        index_path = os.path.join(unit_path, 'index.html')
        
        if not os.path.exists(index_path):
            continue

        attempt = 0
        success = False

        while attempt < RETRY_LIMIT:
            file_size_mb = os.path.getsize(index_path) / (1024 * 1024)
            
            if file_size_mb <= MAX_SIZE_MB:
                success = True
                break
            
            # Jika file gemuk, lakukan operasi pengecilan
            print(f"⚠️ Unit {unit} terlalu gemuk ({file_size_mb:.2f} MB). Mencoba Perbaikan ke-{attempt+1}...")
            
            with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
                original_content = f.read()
            
            slim_content = slim_html_content(original_content)
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(slim_content)
            
            attempt += 1

        # Cek hasil akhir setelah 3 kali percobaan
        final_size_mb = os.path.getsize(index_path) / (1024 * 1024)
        if final_size_mb > MAX_SIZE_MB:
            print(f"💀 GAGAL: Unit {unit} tetap gemuk ({final_size_mb:.2f} MB) setelah {RETRY_LIMIT}x perbaikan. MENGHAPUS UNIT...")
            shutil.rmtree(unit_path)
            total_deleted += 1
        else:
            if attempt > 0:
                print(f"✅ BERHASIL: Unit {unit} sekarang ramping ({final_size_mb:.2f} MB).")
                total_slimmed += 1

    print("\n" + "="*30)
    print(f"📊 LAPORAN AKHIR AUDIT PAO:")
    print(f"- Unit Berhasil Dirampingkan: {total_slimmed}")
    print(f"- Unit Dihapus (Kanker Digital): {total_deleted}")
    print("="*30)
    print("Selesai! Sekarang Sodaraku bisa melakukan 'git push' ulang.")

if __name__ == "__main__":
    process_units()