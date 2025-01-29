import streamlit as st
import os

# Configure la page (doit être la première commande)
st.set_page_config(
    page_title="Formations",
    page_icon="🎓",
)

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(os.path.join("assets", "style.css"))

# Contenu de la page
st.markdown("<h1>Formations</h1>", unsafe_allow_html=True)

# Liste des formations avec logos
st.markdown(
    """
    <div class="section">
        <ul>
            <li>
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google Logo" style="width:50px; vertical-align:middle; margin-right:10px;">
                <strong>Career Certificate - Data Analyste</strong> (septembre - décembre 2024)
            </li>
            <li>
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google Logo" style="width:50px; vertical-align:middle; margin-right:10px;">
                <strong>Career Certificate - Chef de projet IT</strong> (septembre - décembre 2024)
            </li>
            <li>
                <img src="https://avatars.githubusercontent.com/u/8874047" alt="Wild Code School Logo" style="width:50px; vertical-align:middle; margin-right:10px;">
                <strong>Certification Data Analyste RNCP 6</strong> - Wild Code School Lyon (février - août 2024)
            </li>
            <li>
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Claude_Bernard_University_Lyon_1_%28logo%29.svg/225px-Claude_Bernard_University_Lyon_1_%28logo%29.svg.png" alt="Université Claude Bernard Lyon 1 Logo" style="width:50px; vertical-align:middle; margin-right:10px;">
                <strong>DEUST Activités de Pleine Nature et BEES 1 Canoë-kayak</strong> (2001-2003) - Université Claude Bernard Lyon 1
            </li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
