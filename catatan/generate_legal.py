import os

def create_legal_pages():
    print("--- ⚖️ GENERATING LEGAL & TRUST PAGES ---")
    
    pages = {
        "privacy.html": "<h1>Privacy Policy</h1><p>We value your digital autonomy. No personal data is collected on this SSI research site.</p>",
        "terms.html": "<h1>Terms of Service</h1><p>Information provided is for educational purposes regarding Self-Sovereign Identity tools.</p>"
    }
    
    for filename, content in pages.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"<html><body style='font-family:sans-serif; padding:40px;'>{content}<br><a href='index_ssi_alpha.html'>Back to Home</a></body></html>")
        print(f"✅ Created: {filename}")

if __name__ == "__main__":
    create_legal_pages()