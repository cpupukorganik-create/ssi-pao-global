import os

def generate_global_sitemap():
    """
    Menghasilkan sitemap XML murni dengan pembersihan karakter khusus
    agar valid dan tidak menyebabkan Parse Error.
    """
    factory_path = "pao_factory"
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    xml_content += '  <url><loc>https://ssi-pao-global.pages.dev/</loc></url>\n'
    
    if os.path.exists(factory_path):
        units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
        for unit in units:
            # KRUSIAL: Membersihkan karakter '&' agar XML Valid
            clean_unit_name = unit.replace("&", "&amp;")
            unit_url = f"https://ssi-pao-global.pages.dev/pao_factory/{clean_unit_name}/"
            xml_content += f'  <url><loc>{unit_url}</loc></url>\n'
            
    xml_content += '</urlset>'
    
    with open("pao_sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content.strip())
    print("✅ SITEMAP XML VALID BERHASIL DICETAK.")