import os
import re

def inject_dna_v42():
    factory_path = "pao_factory"
    phone_number = "6281343244527"
    # Gantilah link_afiliasi_default di bawah ini setelah Jenderal dapat dari Lembar Kerja 6
    affiliate_link = "https://ssi-pao-global.pages.dev/check-back-soon" 
    
    if not os.path.exists(factory_path):
        print("❌ Folder pao_factory tidak ditemukan!")
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    print(f"🚀 Memulai Operasi DNA v4.2 pada {len(units)} unit...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            unit_name = unit.replace('-', ' ').title()
            ref_code = f"PAO-{unit.upper()}-PREMIUM"
            
            # Pesan Filter Psikologis
            wa_message = f"Bismillah, Jenderal. Saya telah melihat sistem Anda di unit {unit_name}. Saya siap berkomitmen untuk konsultasi strategis tingkat lanjut. (Ref: {ref_code})"
            wa_link = f"https://api.whatsapp.com/send?phone={phone_number}&text={wa_message.replace(' ', '%20')}"

            # BLOK TOMBOL BARU (ALPHA & OMEGA)
            # Kita ganti area tombol lama dengan desain Jalur Ganda
            dual_path_html = f"""
            <div class="imperial-gateways" style="margin-top: 30px; text-align: center;">
                <a href="{affiliate_link}" class="btn-alpha" style="display: block; background: #222; color: #fff; padding: 15px; margin-bottom: 10px; text-decoration: none; border-radius: 5px; font-weight: bold; border: 1px solid #444;">
                    [GATE ALPHA] Acquire the Professional Tool
                </a>
                
                <a href="{wa_link}" class="btn-omega" style="display: block; background: #007bff; color: #fff; padding: 15px; text-decoration: none; border-radius: 5px; font-weight: bold; box-shadow: 0 4px 15px rgba(0,123,255,0.3);">
                    [GATE OMEGA] Claim Strategic Consultation with The Architect
                </a>
                
                <p style="font-size: 12px; color: #888; margin-top: 10px; font-style: italic;">
                    *Limited to 3 Strategic Partners per Week to maintain quality.
                </p>
            </div>
            """

            # Teknik Injeksi: Kita cari penanda akhir konten (sebelum footer atau setelah deskripsi)
            # Untuk template ini, kita suntikkan di atas tag </footer> atau di akhir body
            if "</footer>" in content:
                new_content = content.replace("</footer>", dual_path_html + "</footer>")
            else:
                new_content = content.replace("</body>", dual_path_html + "</body>")
            
            # Tambahkan juga script paksa di header agar link api.whatsapp bekerja mulus
            js_fix = f"<script>window.wa_link = '{wa_link}';</script></head>"
            new_content = new_content.replace("</head>", js_fix)

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ DNA v4.2 Terinjeksi: {unit}")

if __name__ == "__main__":
    inject_dna_v42()