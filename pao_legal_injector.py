import os
from dotenv import load_dotenv

load_dotenv()

def inject_authority_pages():
    factory_path = "pao_factory"
    phone = os.getenv("GATE_OMEGA_PHONE", "62813...") # Diambil dari .env
    
    if not os.path.exists(factory_path):
        return

    units = [d for d in os.listdir(factory_path) if os.path.isdir(os.path.join(factory_path, d))]
    
    about_template = f"""
    <section id="about-authority" style="margin-top:50px; padding:20px; background:#f9f9f9; border-top: 1px solid #eee;">
        <h3>About SSI P.A.O. Global Network</h3>
        <p>This platform is a certified node of the SSI P.A.O. Global Network, dedicated to providing high-level insights into digital transformation and strategic automation.</p>
        <p><b>Legal Representative:</b> Sang Jenderal - Strategic Consultant.</p>
        <p><b>Inquiries:</b> For high-ticket consulting and strategic partnerships, contact us via <a href="https://wa.me/{phone}">Official Support Channel</a>.</p>
    </section>
    """

    for unit in units:
        index_path = os.path.join(factory_path, unit, "index.html")
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if "</body>" in content and "about-authority" not in content:
                new_content = content.replace("</body>", f"{about_template}\n</body>")
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Authority Injected: {unit}")

if __name__ == "__main__":
    inject_authority_pages()