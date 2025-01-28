import streamlit as st
import os

# Configure la page
st.set_page_config(
    page_title="CV en ligne - Florent Cramette",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Fonction pour charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Charger le CSS
load_css(os.path.join("assets", "style.css"))

# Contenu principal
st.markdown("<h1>Bienvenue sur mon CV interactif</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="section center">
        <p>Explorez mon parcours professionnel, mes compétences, mes expériences, mes formations, 
        et mes centres d'intérêt à travers les différentes sections accessibles via le menu latéral.</p>
        <p>Admis en formation Data IA engineer, je suis à la recherche d'une entreprise pour signer un contrat de professionalisation. L'alternance se déroule sur 15 mois, à raison de trois semains en entreprise et une semaine à l'école.<p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Afficher une image
st.image(os.path.join("assets", "board_nom.JPG"), caption="Florent Cramette", use_container_width=True)

# Ajouter un bouton centré pour télécharger le programme de l'alternance
with open(os.path.join("assets", "Programme_Data_IA_Engineer.pdf"), "rb") as file:
    st.markdown(
        """
        <div class="center">
            <a href="assets/Programme_Data_IA_Engineer.pdf" download="Programme_Data_IA_Engineer.pdf" class="blue-button">
                📄 Télécharger le programme de l'alternance
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
