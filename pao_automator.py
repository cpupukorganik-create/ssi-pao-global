import json
import os

def auto_increment_batch():
    """
    Fungsi untuk menaikkan angka BATCH di merchant_vault.json secara otomatis.
    Contoh: BATCH_01 menjadi BATCH_02
    """
    vault_path = 'merchant_vault.json'
    
    # 1. Cek apakah file Brankas ada
    if not os.path.exists(vault_path):
        print("⚠️ Brankas (merchant_vault.json) tidak ditemukan!")
        return

    try:
        # 2. Baca isi Brankas
        with open(vault_path, 'r') as f:
            vault = json.load(f)
        
        # 3. Iterasi (Ulangi) untuk setiap niche di dalam Brankas
        for niche in vault:
            current = vault[niche].get('current_batch', 'BATCH_00')
            
            # Pisahkan teks 'BATCH' dan angka '01'
            prefix, num = current.split('_')
            
            # Tambah angka +1
            new_num = int(num) + 1
            
            # Simpan kembali dengan format dua digit (01, 02, dst)
            vault[niche]['current_batch'] = f"{prefix}_{new_num:02d}"
        
        # 4. Simpan kembali file JSON yang sudah diperbarui
        with open(vault_path, 'w') as f:
            json.dump(vault, f, indent=4)
            
        print(f"✅ Sistem Logistik: Batch Amunisi berhasil dinaikkan.")
        
    except Exception as e:
        print(f"⚠️ Error pada sistem otomasi batch: {e}")

if __name__ == "__main__":
    # Test jalankan fungsi jika file dipanggil langsung
    auto_increment_batch()