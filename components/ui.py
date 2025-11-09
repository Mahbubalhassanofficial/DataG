import streamlit as st
from datetime import datetime

# ===============================================================
# 🌐 1. Custom CSS Injection (Royal Blue & Silver Theme)
# ===============================================================
def inject_custom_css():
    st.markdown("""
    <style>
    /* === GLOBAL BACKGROUND === */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f9fafc 0%, #eef2f7 100%);
    }

    /* === SIDEBAR === */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002855 0%, #00509e 100%);
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        font-family: 'Segoe UI', sans-serif;
    }

    /* === HEADERS === */
    h1, h2, h3, h4 {
        color: #002855;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }

    /* === BUTTONS === */
    div.stButton > button {
        background-color: #00509e;
        color: #ffffff;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        border: none;
        transition: all 0.25s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #0074cc;
        transform: scale(1.03);
    }

    /* === TABLES === */
    .stDataFrame, .stTable {
        border-radius: 10px;
        border: 1px solid #c7d2e0;
    }

    /* === FOOTER === */
    footer {visibility: hidden;}
    .footer-custom {
        font-size: 0.9rem;
        text-align: center;
        color: #444;
        padding: 1.5rem 0;
        background-color: #f2f4f8;
        border-top: 1px solid #c7d2e0;
    }
    a.lab-link {
        color: #00509e;
        font-weight: 700;
        text-decoration: none;
    }
    a.lab-link:hover {
        color: #0074cc;
        text-decoration: underline;
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
