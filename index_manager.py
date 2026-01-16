import os

def generate_imperial_dashboard():
    """
    Menciptakan Etalase Megah dengan Sertifikat Verifikasi Google.
    """
    factory_path = "pao_factory"
    # KODE VERIFIKASI JENDERAL
    google_verify = '<meta name="google-site-verification" content="google388c433d395ecb52" />'
    
    units = []
    if os.path.exists(factory_path):
        units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]

    html_content = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {google_verify}
        <title>Imperial Hub | P.A.O. Global Network</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #0a0a0a; color: #e5e5e5; font-family: 'Inter', sans-serif; }}
            .glow-card {{ 
                transition: all 0.3s ease; 
                border: 1px solid #333;
                background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
            }}
            .glow-card:hover {{ 
                transform: translateY(-5px); 
                border-color: #4ade80; 
                box-shadow: 0 0 20px rgba(74, 222, 128, 0.2); 
            }}
        </style>
    </head>
    <body class="p-8">
        <header class="max-w-6xl mx-auto mb-12 text-center">
            <h1 class="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-green-400 to-blue-500 mb-4">
                IMPERIAL HUB
            </h1>
            <p class="text-gray-400 text-xl">Mengelola {len(units)} Aset Digital Global dalam Satu Komando</p>
        </header>

        <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {"".join([f'''
            <a href="/pao_factory/{unit}/" class="glow-card p-6 rounded-2xl block">
                <div class="flex items-center mb-4">
                    <div class="w-10 h-10 bg-green-500/20 rounded-lg flex items-center justify-center mr-3">
                        <span class="text-green-400 font-bold">PAO</span>
                    </div>
                    <h3 class="text-lg font-semibold truncate">{unit.replace("-", " ").title()}</h3>
                </div>
                <p class="text-sm text-gray-500 mb-4">Aset Digital Terverifikasi & Patuh Hukum.</p>
                <span class="text-xs text-green-400 font-mono tracking-widest">UNIT ACTIVE >></span>
            </a>
            ''' for unit in units])}
        </div>

        <footer class="mt-20 text-center text-gray-600 text-sm">
            <p>&copy; 2024 P.A.O. System - Strategic Solutions International</p>
        </footer>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"🏛️ DASHBOARD BESAR DISIGEL GOOGLE: {len(units)} Unit Terdaftar.")

def update_index_html(dist_folder, niche_name, folder_slug):
    """
    Memasang Redirection Dashboard Kecil dengan Segel Google.
    """
    google_verify = '<meta name="google-site-verification" content="google388c433d395ecb52" />'
    file_path = os.path.join(dist_folder, "index.html")
    content = f"""
    <html>
    <head>
        {google_verify}
        <meta http-equiv='refresh' content='0; url=/pao_factory/{folder_slug}/' />
    </head>
    </html>
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_imperial_dashboard()