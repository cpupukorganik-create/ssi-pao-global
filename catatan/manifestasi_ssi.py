import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Mengambil Kunci dari Gedung Brankas .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Menggunakan model yang sudah teruji stabil di lingkungan Anda
model_name = os.getenv("MODEL_NAME", "gemini-flash-latest")

def manifestasi_aset_ssi():
    print(f"--- 🏗️ PROTOKOL MANIFESTASI: SSI TOOLS COMPARISON ---")
    print(f"Status: Menggunakan Kekuatan {model_name.upper()}...")
    
    # Prompt Strategis untuk menghasilkan Landing Page High-Conversion
    prompt = """
    Role: Senior Web Architect & Cyber Security Content Specialist.
    Task: Create a high-performance, single-page HTML5 website for 'Self-Sovereign Identity (SSI) Tools'.
    
    Technical Requirements:
    1. Framework: Use Tailwind CSS via CDN (Clean & Modern).
    2. Visual Style: High-tech, trustworthy, minimalist, dark mode optimized.
    3. Content Structure (English for Global Market):
       - Hero: Impactful H1 about taking control of your digital identity.
       - Concept: Brief explanation of 'What is SSI?' and why it matters in 2025.
       - Comparison Table: Compare 3 major tools/solutions (e.g., YubiKey for hardware, 
         Evernym for enterprise, and a Decentralized Wallet). Include columns: Security, 
         Ease of Use, and Best For.
       - CTA: Direct links to security resources/affiliates.
    4. Performance: LCP must be under 1.2s (avoid heavy assets).
    
    Output: Only raw HTML/CSS code without any markdown explanation.
    """

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        
        # Membersihkan output dari tag markdown jika AI menyertakannya
        raw_html = response.text.replace('```html', '').replace('```', '').strip()
        
        # Nama file aset pertama kita
        filename = "index_ssi_alpha.html"
        
        # Proses Penulisan Aset
        with open(filename, "w", encoding="utf-8") as f:
            f.write(raw_html)
            
        print(f"\n✅ MANIFESTASI BERHASIL!")
        print(f"📂 Lokasi Aset: F:\\BisnisDigital\\SystemPAO\\{filename}")
        print(f"💡 Perintah: Silakan klik dua kali file tersebut untuk melihat 'Wajah' bisnis Anda.")

    except Exception as e:
        print(f"\n❌ GAGAL MANIFESTASI: {e}")

if __name__ == "__main__":
    manifestasi_aset_ssi()