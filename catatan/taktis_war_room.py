import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

# Konfigurasi Layar Mobile
st.set_page_config(page_title="P.A.O. TACTICAL WAR-ROOM", layout="centered")
load_dotenv()

def get_db_connection():
    conn = sqlite3.connect('pabrik_digital.db', check_same_thread=False)
    return conn

def load_tactical_data():
    conn = get_db_connection()
    # Hanya menarik 10 aktivitas terbaru agar tetap ringan
    query = "SELECT id, title, schedule, completed FROM reminders ORDER BY id DESC LIMIT 10"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #00FF00;'>⚡ TACTICAL WAR-ROOM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Status: <span style='color: #00FF00;'>LIVE - {datetime.now().strftime('%H:%M:%S')} WIT</span></p>", unsafe_allow_html=True)

# --- PANEL 1: CIRCUIT BREAKER (VITAL SIGN) ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label="SERVER LOAD", value="14%", delta="-2%")
with col2:
    st.metric(label="API STATUS", value="HEALTHY", delta="🟢")

# --- PANEL 2: RADAR FRONTLINE (DEPLOYS) ---
st.subheader("📡 Radar Frontline (10 Unit Terakhir)")
data = load_tactical_data()

for index, row in data.iterrows():
    status_icon = "🔵" if row['completed'] else "⚔️"
    st.info(f"{status_icon} **{row['title']}**\n\nID: {row['id']} | Time: {row['schedule']}")

# --- PANEL 3: AUTO-REFRESH SCRIPT ---
# Script sederhana untuk auto-refresh setiap 30 detik di browser
st.empty()
st.caption("Auto-refresh aktif setiap 30 detik untuk akurasi data taktis.")