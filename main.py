import streamlit as st
import os

# Configure la page
st.set_page_config(
    page_title="CV en ligne - Florent Cramette",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Fonction pour charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Charger le CSS
load_css(os.path.join("assets", "style.css"))

# Titre principal
st.markdown("<h1 style='text-align: center;'>Bienvenue sur mon CV interactif</h1>", unsafe_allow_html=True)

# Afficher une image
st.image(os.path.join("assets", "board_nom.JPG"), caption="Florent Cramette", use_container_width=True)


