import streamlit as st
from datetime import datetime

# ===============================================================
# 🌐 1. Custom CSS Injection (Royal Blue & Silver Theme – Enhanced)
# ===============================================================
def inject_custom_css():
    st.markdown("""
    <style>
    /* === REMOVE DEFAULT BACKGROUND AND ENSURE FULL-COLOR COVERAGE === */
    html, body, [class*="ViewContainer"], [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #eaf0f7 0%, #f5f7fa 100%) !important;
        background-color: #eaf0f7 !important;
        color: #111 !important;
    }

    /* === MAIN CONTAINER CLEANUP === */
    [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {
        background: none !important;
    }

    /* === SIDEBAR === */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002855 0%, #00509e 100%) !important;
        color: white !important;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    /* === HEADERS === */
    h1, h2, h3, h4 {
        color: #002855 !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-weight: 700 !important;
    }

    /* === BUTTONS === */
    div.stButton > button {
        background-color: #00509e !important;
        color: #ffffff !important;
        border-radius: 6px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.25s ease-in-out !important;
    }
    div.stButton > button:hover {
        background-color: #0074cc !important;
        transform: scale(1.03) !important;
    }

    /* === DATAFRAME / TABLE === */
    .stDataFrame, .stTable {
        border-radius: 10px !important;
        border: 1px solid #c7d2e0 !important;
        background-color: #ffffff !important;
    }

    /* === FOOTER === */
    footer {visibility: hidden !important;}
    .footer-custom {
        font-size: 0.9rem !important;
        text-align: center !important;
        color: #444 !important;
        padding: 1.5rem 0 !important;
        background: linear-gradient(90deg, #eaf0f7 0%, #f5f7fa 100%) !important;
        border-top: 1px solid #c7d2e0 !important;
    }

    /* === LINKS === */
    a.lab-link {
        color: #00509e !important;
        font-weight: 700 !important;
        text-decoration: none !important;
    }
    a.lab-link:hover {
        color: #0074cc !important;
        text-decoration: underline !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ===============================================================
# 🧭 2. Footer with Full Branding and Website Link
# ===============================================================
def footer_brand():
    st.markdown(f"""
    <div class="footer-custom">
        <strong>Developed by Mahbub Hassan</strong><br>
        Department of Civil Engineering, Faculty of Engineering, Chulalongkorn University<br>
        Founder, <a href="https://www.bdeshi-lab.org/" class="lab-link" target="_blank">B'Deshi Emerging Research Lab</a><br>
        Email: <a href="mailto:mahbub.hassan@ieee.org" class="lab-link">mahbub.hassan@ieee.org</a><br>
        🌐 <a href="https://www.bdeshi-lab.org/" class="lab-link" target="_blank">www.bdeshi-lab.org</a><br>
        © {datetime.now().year} · All rights reserved.
    </div>
    """, unsafe_allow_html=True)
