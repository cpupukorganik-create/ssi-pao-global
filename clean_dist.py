import os
import shutil

def clean_battlefield():
    """
    Menghapus folder dist lama untuk persiapan produksi V6 yang lebih segar.
    Tetap mempertahankan pao_factory (Induk Konten).
    """
    print("🧹 MENGINISIASI PEMBERSIHAN MEDAN TEMPUR...")
    
    # Mencari semua folder yang diawali dengan 'dist'
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and f.startswith('dist')]
    
    if not folders:
        print("✨ Medan tempur sudah bersih. Tidak ada folder 'dist' yang ditemukan.")
        return

    for folder in folders:
        try:
            shutil.rmtree(folder)
            print(f"🗑️ Berhasil menghapus: {folder}")
        except Exception as e:
            print(f"⚠️ Gagal menghapus {folder}: {e}")

    print("\n✅ PEMBERSIHAN SELESAI. Sistem siap untuk Produksi Otomatis V6!")

if __name__ == "__main__":
    confirm = input("Apakah Jenderal yakin ingin menghapus SEMUA folder 'dist'? (y/n): ")
    if confirm.lower() == 'y':
        clean_battlefield()
    else:
        print("❌ Pembersihan dibatalkan.")