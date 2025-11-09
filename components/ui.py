import streamlit as st
from datetime import datetime

def inject_custom_css():
    st.markdown("""
    <style>
    /* === GLOBAL BACKGROUND === */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ffffff 0%, #f6ecf2 100%);
    }

    /* === SIDEBAR === */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #b5121b 0%, #f9e0e7 100%);
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* === HEADERS === */
    h1, h2, h3, h4 {
        color: #b5121b;
        font-family: 'Trebuchet MS', sans-serif;
        font-weight: 700;
    }

    /* === BUTTONS === */
    div.stButton > button {
        background-color: #b5121b;
        color: #ffffff;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        border: none;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #8a0e15;
        transform: scale(1.02);
    }

    /* === TABLES === */
    .stDataFrame, .stTable {
        border-radius: 10px;
        border: 1px solid #dcd0d5;
    }

    /* === FOOTER === */
    footer {visibility: hidden;}
    .footer-custom {
        font-size: 0.9rem;
        text-align: center;
        color: #6b6b6b;
        padding: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
