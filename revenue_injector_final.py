import os
import master_config

def mass_revenue_deployment():
    factory_path = "pao_factory"
    # Kode Iklan Tier 3 (Adsterra/Fallback)
    tier_3_code = master_config.CPM_AD_CODE 
    
    for unit in os.listdir(factory_path):
        index_file = os.path.join(factory_path, unit, "index.html")
        if os.path.isfile(index_file):
            # VALIDASI: Cek Ukuran File (Minimal 500 bytes agar tidak kosong)
            if os.path.getsize(index_file) < 500:
                print(f"⚠️ Unit {unit} rusak/kosong. Skip.")
                continue
                
            with open(index_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            # EKSEKUSI WATERFALL
            # 1. Cek Tier 1 (Impact/Direct), Jika belum ada, biarkan placeholder.
            # 2. Injeksi Tier 3 (Adsterra) sebagai jaring pengaman.
            if "adsterra" not in content.lower():
                updated = content.replace("", f"\n{tier_3_code}\n")
                with open(index_file, "w", encoding="utf-8") as f:
                    f.write(updated)
                print(f"✅ Waterfall Active (Tier 3): {unit}")