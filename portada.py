import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Best Ranked Of Google Play", layout="wide")

# Importa y aplica la fuente de Google Fonts usando CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fugaz+One&display=swap');
    
    .container {
        font-family: 'Fugaz One', sans-serif;
        text-align: center;
        background-color: #5a00e0;
        color: white;
        padding: 80px;
    }
    .main-text {
        font-size: 72px;
        font-weight: bold;
        color: #ffffff;
    }
    .sub-text {
        font-size: 72px;
        font-weight: bold;
        color: #000000;
        margin-top: -30px;
    }
    .description {
        font-size: 32px;
        color: #ffffff;
        margin-top: -30px;
    }
    .button {
        margin-top: 40px;
        padding: 12px 32px;
        font-size: 24px;
        background-color: transparent;
        color: white;
        border: 2px solid white;
        border-radius: 8px;
        cursor: pointer;
        text-decoration: none;
    }
    .button:hover {
        background-color: white;
        color: #5a00e0;
    }
    </style>
    """, unsafe_allow_html=True)

# Contenido de la página
st.markdown("""
    <div class="container">
        <div class="main-text">Best</div>
        <div class="sub-text">Ranked</div>
        <div class="description">Of Google Play</div>
        <a href="#" class="button">Empezar</a>
    </div>
    """, unsafe_allow_html=True)
