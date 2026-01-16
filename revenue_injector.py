import os

def inject_revenue_links():
    """
    Menyuntikkan Link WhatsApp Bisnis ke seluruh unit yang sudah ada 
    di pao_factory dan memperbarui Dashboard Utama.
    """
    factory_path = "pao_factory"
    # KONFIGURASI MESIN KASIR
    phone_number = "6281343244527"
    
    if not os.path.exists(factory_path):
        print("❌ Folder pao_factory tidak ditemukan!")
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    print(f"🚀 Memulai Injeksi Pendapatan pada {len(units)} unit...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # PESAN OTOMATIS: Memberikan kesan Admin Profesional & Membatasi Chat/Text Only
            wa_message = f"Halo Admin SSI, saya tertarik dengan unit {unit.replace('-', ' ').title()}. Mohon info detail via chat."
            encoded_message = wa_message.replace(" ", "%20")
            wa_link = f"https://wa.me/{phone_number}?text={encoded_message}"

            # MENYUNTIKKAN LINK KE TOMBOL (Mencari href='#' atau tombol CTA)
            # Kita ganti semua link kosong '#' dengan link WhatsApp Jenderal
            updated_content = content.replace('href="#"', f'href="{wa_link}"')
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ Mesin Kasir Terpasang di: {unit}")

    print("\n💰 SEMUA UNIT TELAH TERHUBUNG KE HOTLINE JENDERAL!")

if __name__ == "__main__":
    inject_revenue_links()