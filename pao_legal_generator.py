import os

def inject_legal_pages(dist_path, niche_name):
    """
    Menyuntikkan halaman kepatuhan hukum standar internasional 
    untuk persyaratan Afiliasi & Google AdSense.
    """
    
    # 1. TEMPLATE PRIVACY POLICY
    privacy_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Privacy Policy - {niche_name}</title>
        <style>body{{font-family:sans-serif; line-height:1.6; padding:40px; color:#333; max-width:900px; margin:auto;}} h1{{color:#2c3e50;}}</style>
    </head>
    <body>
        <h1>Privacy Policy</h1>
        <p>Last Updated: 2025</p>
        <p>At <strong>{niche_name}</strong>, accessible from our website, one of our main priorities is the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by us and how we use it.</p>
        <h2>Log Files</h2>
        <p>We follow a standard procedure of using log files. These files log visitors when they visit websites. All hosting companies do this and a part of hosting services' analytics.</p>
        <h2>Cookies and Web Beacons</h2>
        <p>Like any other website, we use 'cookies'. These cookies are used to store information including visitors' preferences, and the pages on the website that the visitor accessed or visited.</p>
        <h2>Third Party Privacy Policies</h2>
        <p>Our Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies of these third-party ad servers for more detailed information.</p>
        <hr>
        <p><a href="index.html">← Back to Home</a></p>
    </body>
    </html>
    """

    # 2. TEMPLATE DISCLAIMER (Crucial for Affiliates)
    disclaimer_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Disclaimer - {niche_name}</title>
        <style>body{{font-family:sans-serif; line-height:1.6; padding:40px; color:#333; max-width:900px; margin:auto;}} h1{{color:#c0392b;}}</style>
    </head>
    <body>
        <h1>Disclaimer</h1>
        <p>If you require any more information or have any questions about our site's disclaimer, please feel free to contact us.</p>
        <p>All the information on this website - <strong>{niche_name}</strong> - is published in good faith and for general information purpose only. We do not make any warranties about the completeness, reliability and accuracy of this information.</p>
        <h2>Affiliate Disclosure</h2>
        <p>This site may contain links to affiliate websites, and we receive an affiliate commission for any purchases made by you on the affiliate website using such links.</p>
        <p>Any action you take upon the information you find on this website is strictly at your own risk. will not be liable for any losses and/or damages in connection with the use of our website.</p>
        <hr>
        <p><a href="index.html">← Back to Home</a></p>
    </body>
    </html>
    """

    # Proses Penulisan File ke Folder Dist
    pages = {
        "privacy-policy.html": privacy_html,
        "disclaimer.html": disclaimer_html
    }

    for filename, content in pages.items():
        file_path = os.path.join(dist_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
    
    print(f"⚖️ Legal Compliance Injected into {dist_path}")

if __name__ == "__main__":
    # Test internal
    print("Testing Legal Generator...")