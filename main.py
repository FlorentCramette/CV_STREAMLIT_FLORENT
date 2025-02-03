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

# Contenu principal
st.markdown("<h1>Bienvenue sur mon CV interactif</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="section center">
        <p>A la recherche d'une première expérience en tant que Data Analyste, ou d'une alternance pour devenir Data IA Engineer, explorez mon parcours à travers les différentes sections accessibles via le menu latéral.</p>
        <p>Admis en formation Data IA engineer, je suis à la recherche d'une entreprise pour signer un contrat de professionalisation. 
        L'alternance débute en mars 2025 et se déroule sur 15 mois, à raison de trois semaines en entreprise et une semaine à l'école.<p>
        <p>Si vous souhaitez combiner l'énergie du junior à la sagesse du sénior: je suis là!<p>
     </div>
    """,
    unsafe_allow_html=True,
)

# Ajouter un bouton de téléchargement pour le PDF
pdf_path = os.path.join("assets", "Programme_Data_IA_Engineer.pdf")

# Vérifier si le fichier existe
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_bytes = file.read()

    st.download_button(
        label="📄 Télécharger le programme de l'alternance",
        data=pdf_bytes,
        file_name="Programme_Data_IA_Engineer.pdf",
        mime="application/pdf"
    )
else:
    st.error("Le fichier Programme_Data_IA_Engineer.pdf est introuvable. Vérifiez le chemin.")


# Afficher une image
st.image(os.path.join("assets", "board_nom.JPG"), caption="Florent Cramette", use_container_width=True)


