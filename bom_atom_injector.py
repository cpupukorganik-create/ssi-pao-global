import os
import re

def atomic_revenue_injection():
    """
    Operasi Penghancuran Total: Mengganti segala bentuk link yang mengandung 
    'impact.com' dengan Hotline WhatsApp Jenderal secara paksa.
    """
    factory_path = "pao_factory"
    phone_number = "6281343244527"
    
    if not os.path.exists(factory_path):
        print("❌ Folder pao_factory tidak ditemukan!")
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    print(f"🚀 Memulai Operasi Bom Atom pada {len(units)} unit...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            wa_message = f"Halo Admin SSI, saya ingin memesan Sesi Strategi untuk unit {unit.replace('-', ' ').title()}."
            wa_link = f"https://wa.me/{phone_number}?text={wa_message.replace(' ', '%20')}"

            # RADAR PENGHANCUR: Mencari pola link yang mengandung impact.com apa pun bentuknya
            # Pola ini akan menangkap href="http://...", href='https://...', dll.
            content = re.sub(r'href=["\']https?://[^"\']*impact\.com[^"\']*["\']', f'href="{wa_link}"', content)
            
            # Ganti juga placeholder standar yang mungkin tertinggal
            content = content.replace('href="#"', f'href="{wa_link}"')
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"💥 RADIKAL: {unit} BERHASIL DIINJEKSI TOTAL.")

if __name__ == "__main__":
    atomic_revenue_injection()