import streamlit as st
from datetime import datetime

# ===============================================================
# 🌐 1. Custom CSS Injection (Royal Blue & Silver Theme – Enhanced)
# ===============================================================
def inject_custom_css():
    st.markdown("""
    <style>
    /* === RESET ALL DEFAULTS === */
    html, body {
        background-color: #eaf0f7 !important;
        color: #111 !important;
    }

    /* === STREAMLIT APP VIEW === */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #eaf0f7 0%, #f4f7fb 100%) !important;
    }

    /* === MAIN PAGE BODY === */
    .main, .block-container {
        background: transparent !important;
        background-color: transparent !important;
        color: #111 !important;
        box-shadow: none !important;
    }

    /* === SIDEBAR === */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002855 0%, #004b93 100%) !important;
        color: #ffffff !important;
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

    /* === TABLES === */
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
        background: linear-gradient(90deg, #eaf0f7 0%, #f4f7fb 100%) !important;
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

    /* === INPUT BOXES === */
    input, select, textarea, .stNumberInput input {
        background-color: #f0f4fa !important;
        border: 1px solid #c5d1e0 !important;
        color: #002855 !important;
        border-radius: 6px !important;
    }
    input:focus, select:focus, textarea:focus {
        outline: 2px solid #00509e !important;
        background-color: #ffffff !important;
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
# ===============================================================
# ⚠️ 3. Disclaimer Section
# ===============================================================
def disclaimer_note():
    st.markdown("""
    <div style="
        text-align: center;
        font-size: 0.85rem;
        color: #666;
        margin-top: -0.5rem;
        margin-bottom: 1rem;
        font-style: italic;
    ">
        ⚠️ <strong>Disclaimer:</strong> This tool is developed solely for academic learning and research training purposes.
        It is not intended for commercial use or for generating real survey data.
    </div>
    """, unsafe_allow_html=True)
