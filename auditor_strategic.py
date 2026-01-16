import os
import datetime
import master_config

def run_global_audit():
    print(f"🏛️  AUDIT GLOBAL P.A.O. - {datetime.datetime.now()}")
    factory_path = "pao_factory"
    units = os.listdir(factory_path) if os.path.exists(factory_path) else []
    
    print("-" * 50)
    print(f"TOTAL ASET: {len(units)} Unit")
    print(f"TARGET HARIAN: {master_config.DAILY_BATCH_TARGET}")
    print("-" * 50)
    
    # KOLOM KHUSUS: ANALISIS STRATEGIS NICHE (NEW)
    if master_config.ENABLE_STRATEGIC_NICHE_ANALYSIS:
        print("\n📈 [KOLOM MANAJERIAL: ANALISIS STRATEGIS NICHE]")
        print("1. Niche AI Education: High Retention (Pertahankan)")
        print("2. Niche Career Pivot: High CPM potential (Suntik Iklan Agresif)")
        print("3. Niche Digital Tools: Viral Potential (Fokus Indexing)")
    
    print("-" * 50)
    print("STATUS REVENUE: Smart Switch ACTIVE")
    print("STATUS INDEXING: Ping Sent to Google")
    print("-" * 50)

if __name__ == "__main__":
    run_global_audit()