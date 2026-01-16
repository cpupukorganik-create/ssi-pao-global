import os
from datetime import datetime

# Konfigurasi
BASE_URL = "https://ssi-pao-global.pages.dev/"
TARGET_FOLDER = "./dist" # Sesuaikan dengan folder output Anda

def create_sitemap():
    files = [f for f in os.listdir(TARGET_FOLDER) if f.endswith('.html')]
    
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for file in files:
        url = f"{BASE_URL}{file}"
        lastmod = datetime.now().strftime('%Y-%m-%d')
        
        sitemap_content += f"  <url>\n"
        sitemap_content += f"    <loc>{url}</loc>\n"
        sitemap_content += f"    <lastmod>{lastmod}</lastmod>\n"
        sitemap_content += f"    <priority>0.80</priority>\n"
        sitemap_content += f"  </url>\n"

    sitemap_content += '</urlset>'

    with open(os.path.join(TARGET_FOLDER, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print(f"✅ Sitemap.xml berhasil dibuat dengan {len(files)} halaman!")

if __name__ == "__main__":
    create_sitemap()