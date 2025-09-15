import streamlit as st
import os

# Configuration de la page
st.set_page_config(page_title="Centres d'intérêt", page_icon="🌍")

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(os.path.join("assets", "style.css"))

st.markdown("<h1>Centres d'intérêt</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="section">
        <ul>
            <li>Cinéma, lecture, théâtre et informatique</li>
            <li>Sports outdoors : kayak, VTT, randonnée pédestre et à ski</li>
            <li>Bricolage et construction</li>
            <li>Voyages</li>
            <li>Impression numérique</li>
            <li>IOT (objets connectés, domotique)</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Afficher le carrousel d'images


