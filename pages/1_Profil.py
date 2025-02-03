import streamlit as st
import os

# Configure la page
st.set_page_config(
    page_title="À propos de moi",
    layout="wide",
    page_icon="👤")

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
        <p>
            <strong>Sportif dans l'âme et passionné par l’analyse de données,</strong> je transforme l’information brute en leviers stratégiques. 
            Après une carrière dans le sport et le retail, j’ai choisi de me spécialiser en data pour allier vision métier et expertise technique.<p>
            <p>Compétent en BI (Power BI, Tableau, SQL) et Python, j’aime extraire des insights clés, automatiser des processus 
            et créer des modèles prédictifs. Curieux et orienté impact, je cherche un premier poste en Data Analyse ou une alternance en Data/IA Engineering.
        <p>    
            <p>Envie d’en savoir plus ? Échangeons ! 🚀<p>
        </p>
        
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

# Vérifier si le fichier CV existe
cv_path = os.path.join("assets", "CV_Florent_Cramette_Data_2025.pdf")

if os.path.exists(cv_path):
    with open(cv_path, "rb") as file:
        cv_bytes = file.read()

    # Centrer le bouton avec un div en HTML/CSS
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.download_button(
        label="📄 Télécharger mon CV",
        data=cv_bytes,
        file_name="CV_Florent_Cramette.pdf",
        mime="application/pdf"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
else:
    st.error("Le fichier CV_Florent_Cramette_Data_2025.pdf est introuvable. Vérifiez son emplacement.")
