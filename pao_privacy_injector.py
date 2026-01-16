import os
from dotenv import load_dotenv

load_dotenv()

def inject_privacy_policy():
    factory_path = "pao_factory"
    project_name = os.getenv("PROJECT_NAME", "SSI P.A.O. Global Network")
    email = os.getenv("PAYPAL_RECEIVER_EMAIL", "contact@ssi-pao-global.com")
    
    if not os.path.exists(factory_path):
        print("⚠️ Folder factory tidak ditemukan.")
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    
    privacy_template = f"""
    <section id="privacy-policy" style="margin-top:40px; padding:20px; font-size: 0.8em; color: #666; border-top: 1px dashed #ccc;">
        <h4>Privacy Policy</h4>
        <p>Your privacy is important to us. This policy outlines how <b>{project_name}</b> handles data. 
        We do not collect personal information unless voluntarily provided. 
        Any data shared is used solely for strategic consulting purposes and is protected under global privacy standards.</p>
        <p>For data inquiries, contact: <i>{email}</i></p>
        <p>&copy; 2024 SSI P.A.O. Global Network - All Rights Reserved.</p>
    </section>
    """

    print(f"🛡️ MENYUNTIKKAN KEBIJAKAN PRIVASI KE {len(units)} UNIT...")

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Pastikan tidak menyuntikkan dua kali
            if "privacy-policy" not in content:
                if "</body>" in content:
                    # Disisipkan tepat sebelum tag penutup body
                    new_content = content.replace("</body>", f"{privacy_template}\n</body>")
                    with open(index_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ Privacy Policy Injected: {unit}")

if __name__ == "__main__":
    inject_privacy_policy()