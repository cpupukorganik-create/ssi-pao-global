import os
import re
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def final_assembly_processor():
    """
    MASTER ASSEMBLY V8.0 - INTEGRASI 9 IDE
    Status: Global Blueprint (Features Locked by Default)
    """
    factory_path = "pao_factory"
    # Mengambil data Identitas Jenderal dari .env
    phone = os.getenv("GATE_OMEGA_PHONE", "6281343244527")
    paypal = os.getenv("PAYPAL_RECEIVER_EMAIL")
    affiliate_id = os.getenv("AFFILIATE_GLOBAL_ID", "jenderal_01")
    
    if not os.path.exists(factory_path):
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    print(f"🏗️ MENGAKOMODIR 9 IDE PADA {len(units)} UNIT...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # --- [IDE 1, 3, 5: GATEWAY & ACCOUNTING PREP] ---
            wa_link = f"https://wa.me/{phone}?text=Strategi%20Unit%20{unit}"
            
            # --- [IDE 9: VISITOR MEMORY - DNA INJECTION] ---
            # Menanamkan skrip pengingat pengunjung (Locked/Silent Mode)
            visitor_script = """
            <script id="pao-v8-memory">
                // IDE 9: Status Locked - Menunggu Aktivasi 90 Hari
                console.log('PAO V8 Memory Core Loaded');
            </script>"""

            # --- [IDE 7 & 8: DYNAMIC SCARCITY & REMOTE UPDATE] ---
            # Menyiapkan jangkar (anchor) agar pesan bisa diubah secara remote nanti
            remote_anchor = '<div id="pao-remote-broadcast" style="display:none;"></div>'

            # --- [IDE 4: CYBER SECURITY PROTOCOL] ---
            # Menyuntikkan integritas file untuk pengecekan otomatis
            security_tag = f''

            # PROSES PENYUNTIKAN MASIF
            if "</head>" in content:
                content = content.replace("</head>", f"{visitor_script}\n{security_tag}\n</head>")
            
            if "</body>" in content:
                # Menambahkan Remote Anchor tepat sebelum akhir body
                content = content.replace("</body>", f"{remote_anchor}\n</body>")

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ UNIT {unit}: DNA V8.0 ASSEMBLED.")

if __name__ == "__main__":
    final_assembly_processor()