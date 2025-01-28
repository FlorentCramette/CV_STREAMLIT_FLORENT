import streamlit as st
import os

# Configure la page
st.set_page_config(page_title="À propos de moi", page_icon="👤")

# Fonction pour charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Charger le CSS
load_css(os.path.join("assets", "style.css"))

# Contenu de la page
st.markdown("<h1>À propos de moi</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="section">
        <p><strong>Passionné par l’analyse de données, fort d’une expertise en gestion et retail.</strong></p>
        <p>Après une carrière enrichissante dans le management sportif et le secteur retail, où j'ai occupé des postes 
        à responsabilité (approvisionnement, gestion des équipes et opérations commerciales), j’ai opéré une transition 
        vers les métiers de la data.</p>
        <p>Grâce à une formation solide et des compétences en <strong>BI (Power BI, Tableau, SQL)</strong> et <strong>Python</strong>, 
        je mets à profit mon <strong>sens de l'analyse</strong> et ma <strong>capacité à résoudre des problèmes</strong> pour accompagner 
        les entreprises dans la prise de décisions stratégiques.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Liens GitHub et LinkedIn centrés
st.markdown(
    """
    <div class="center section">
        <a href="https://github.com/FlorentCramette" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-Profil-blue?logo=github" alt="GitHub">
        </a>
        <a href="https://www.linkedin.com/in/florentcramette/" target="_blank" style="margin-left: 20px;">
            <img src="https://img.shields.io/badge/LinkedIn-Florent%20Cramette-blue?logo=linkedin" alt="LinkedIn">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Coordonnées centrées
st.markdown(
    """
    <div class="center">
        <p><strong>Email :</strong> <a href="mailto:florent.cramette@gmail.com">florent.cramette@gmail.com</a></p>
        <p><strong>Téléphone :</strong> +33 (0)6 21 52 41 40</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Bouton centré pour télécharger le CV
with open(os.path.join("assets", "CV_florent_cramette_data_analyste_2025.pdf"), "rb") as pdf_file:
    st.markdown(
        """
        <div class="center">
            <a href="assets/CV_florent_cramette_data_analyste_2025.pdf" download="CV_Florent_Cramette.pdf" class="blue-button">
                📄 Télécharger mon CV
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
