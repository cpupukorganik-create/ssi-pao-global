import os

def get_batch_stats():
    """
    Fungsi Inti: Mengambil data numerik untuk Dashboard.
    Mengembalikan: (jumlah_batch, jumlah_unit)
    """
    path = "pao_factory"
    
    # Jika folder belum ada, aset masih nol
    if not os.path.exists(path):
        return 0, 0
    
    # Menghitung semua folder di dalam pao_factory
    try:
        units = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        total_units = len(units)
        
        # Logika Batch: Setiap kelipatan 200 dianggap 1 Batch
        # Jika ada sisa (misal 205 unit), tetap dihitung batch berjalan berikutnya
        if total_units == 0:
            active_batches = 0
        else:
            active_batches = (total_units // 200) + (1 if total_units % 200 > 0 else 0)
            
        return active_batches, total_units
    except Exception:
        return 0, 0

def summarize_factory_batches():
    """
    Fungsi Laporan: Mencetak ringkasan ke terminal (dipakai di akhir Auto-Pilot).
    """
    batches, units = get_batch_stats()
    progress = (units / 10000) * 100
    
    print("\n" + "="*40)
    print("       📊 LAPORAN KEKUATAN ASSET")
    print("="*40)
    print(f" 🏭 Unit Terverifikasi : {units}")
    print(f" 📦 Batch Terdistribusi : {batches}")
    print(f" 🎯 Capaian Target      : {progress:.2f}% dari 10.000")
    print("-" * 40)
    return batches

if __name__ == "__main__":
    # Test Mandiri
    summarize_factory_batches()