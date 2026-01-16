import json
import os

def get_final_link(niche_key):
    """Fungsi untuk mengambil ID dari Brankas dan menyusun Link secara otomatis"""
    vault_path = 'merchant_vault.json'
    
    if not os.path.exists(vault_path):
        print(f"⚠️ File {vault_path} tidak ditemukan!")
        return None

    try:
        with open(vault_path, 'r') as f:
            vault = json.load(f)
        
        # Mencocokkan Niche (contoh: AI_TOOLS)
        if niche_key in vault:
            data = vault[niche_key]
            # Menggabungkan Base URL + ID + Batch Suffix
            link = f"{data['base_url']}{data['your_id']}_{data.get('current_batch', 'B01')}"
            return link
        else:
            print(f"⚠️ Niche '{niche_key}' tidak ditemukan di Brankas.")
            return None
    except Exception as e:
        print(f"⚠️ Error membaca Brankas: {e}")
        return None

def hunt_paypal_merchants(niche):
    """Simulasi pencarian merchant baru (seperti yang sudah ada)"""
    # ... (Ini kode simulasi pencarian yang tadi sudah kita buat) ...
    report = f"\n--- 🎯 MERCHANT PAYPAL DITEMUKAN ---\n"
    report += f"🔹 Nama: Fast-AI Copywriter\n   URL: https://affiliate.fastai.io/join\n"
    report += f"🔹 Nama: DeepMind Design Tool\n   URL: https://merchant.deepmind.net/pp\n"
    return report