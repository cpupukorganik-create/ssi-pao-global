import os
import re
from dotenv import load_dotenv

load_dotenv()

def super_revenue_injection():
    factory_path = "pao_factory"
    phone_number = "6281343244527"
    
    # MENGAMBIL GATEWAY DARI .ENV
    paypal_email = os.getenv("PAYPAL_RECEIVER_EMAIL")
    affiliate_id = os.getenv("AFFILIATE_GLOBAL_ID")
    amal_percent = os.getenv("AMAL_JARIYAH_PERCENT")
    
    # Link Afiliasi Dinamis dengan ID Jenderal
    affiliate_link = f"https://ssi-pao-global.pages.dev/check-back-soon?ref={affiliate_id}"
    
    if not os.path.exists(factory_path):
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    print(f"🚀 Injeksi Gateway Financial pada {len(units)} unit...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            unit_name = unit.replace('-', ' ').title()
            wa_message = f"Bismillah, Jenderal. Saya tertarik dengan unit {unit_name}. (Ref ID: {affiliate_id})"
            wa_link = f"https://api.whatsapp.com/send?phone={phone_number}&text={wa_message.replace(' ', '%20')}"

            # UI GATEWAY ALPHA-OMEGA + BADGE AMAL
            dual_path_html = f"""
            <div class="imperial-gateways" style="margin-top: 30px; text-align: center; border: 2px solid #007bff; padding: 20px; border-radius: 15px; background: rgba(0,123,255,0.05);">
                <div style="margin-bottom: 15px; font-size: 14px; color: #4ade80; font-weight: bold;">
                    🌿 SOSIAL KOMITMEN: {amal_percent}% dari keuntungan unit ini didonasikan untuk Amal Jariyah.
                </div>
                
                <a href="{affiliate_link}" class="btn-alpha" style="display: block; background: #222; color: #fff; padding: 15px; margin-bottom: 10px; text-decoration: none; border-radius: 8px; font-weight: bold; border: 1px solid #444;">
                    [GATE ALPHA] Secure Professional License (Ref: {affiliate_id})
                </a>
                
                <a href="{wa_link}" class="btn-omega" style="display: block; background: #007bff; color: #fff; padding: 15px; text-decoration: none; border-radius: 8px; font-weight: bold; box-shadow: 0 4px 15px rgba(0,123,255,0.3);">
                    [GATE OMEGA] Direct Consultation via WhatsApp
                </a>
                
                <p style="font-size: 11px; color: #888; margin-top: 15px;">
                    Verified Receiver: {paypal_email[:3]}***@{paypal_email.split('@')[1]}
                </p>
            </div>
            """
            
            # (Gunakan logika penggantian teks yang sama seperti sebelumnya)
            if "</footer>" in content:
                new_content = content.replace("</footer>", dual_path_html + "</footer>")
            else:
                new_content = content.replace("</body>", dual_path_html + "</body>")

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"🔱 GATEWAY SETTLED: {unit}")

if __name__ == "__main__":
    super_revenue_injection()