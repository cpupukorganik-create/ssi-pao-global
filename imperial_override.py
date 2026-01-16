import os

def imperial_force_override():
    """
    Operasi Overwrite Sektor Utama: Menyuntikkan Skrip Penangkapan Klik 
    langsung ke Header HTML untuk membelokkan semua link asing.
    """
    factory_path = "pao_factory"
    phone_number = "6281343244527"
    
    if not os.path.exists(factory_path):
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    print(f"🚀 Memulai Pengambilalihan Paksa pada {len(units)} unit...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            wa_message = f"Halo Admin SSI, saya ingin memesan Sesi Strategi untuk unit {unit.replace('-', ' ').title()}."
            wa_link = f"https://wa.me/{phone_number}?text={wa_message.replace(' ', '%20')}"

            # SKRIP PENANGKAP (JS OVERRIDE)
            # Skrip ini akan mencegat semua klik yang mengarah ke impact.com secara realtime
            js_override = f"""
            <script>
                document.addEventListener('click', function(e) {{
                    let target = e.target.closest('a');
                    if (target && (target.href.includes('impact.com') || target.href === window.location.href + '#')) {{
                        e.preventDefault();
                        window.location.href = '{wa_link}';
                    }}
                }}, true);
            </script>
            </head>"""

            # Suntikkan skrip tepat sebelum tag </head>
            if "</head>" in content:
                updated_content = content.replace("</head>", js_override)
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"🔱 IMPERIAL OVERRIDE SUKSES: {unit}")

if __name__ == "__main__":
    imperial_force_override()