import os
import re

def ultimate_revenue_injection():
    """
    Operasi Pembersihan Total: Mencari semua link yang mengandung 'impact.com' 
    atau '#' dan menggantinya dengan Hotline WhatsApp Jenderal.
    """
    factory_path = "pao_factory"
    phone_number = "6281343244527"
    
    if not os.path.exists(factory_path):
        print("❌ Folder pao_factory tidak ditemukan!")
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    print(f"🚀 Memulai Operasi Sapu Bersih pada {len(units)} unit...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Draf Pesan Strategis Jenderal
            wa_message = f"Halo Admin SSI, saya ingin memesan Sesi Strategi untuk unit {unit.replace('-', ' ').title()}."
            wa_link = f"https://wa.me/{phone_number}?text={wa_message.replace(' ', '%20')}"

            # TEKNIK RADAR AGRESIF: Menggunakan Regex untuk mencari link impact apa pun
            # Ini akan mengganti semua yang mengandung impact.com/your-link
            content = re.sub(r'href="https?://impact\.com/[^"]+"', f'href="{wa_link}"', content)
            
            # Tetap bersihkan placeholder standar
            content = content.replace('href="#"', f'href="{wa_link}"')
            content = content.replace('href="javascript:void(0)"', f'href="{wa_link}"')
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"🔥 SELESAI DISAPU BERSIH: {unit}")

if __name__ == "__main__":
    ultimate_revenue_injection()