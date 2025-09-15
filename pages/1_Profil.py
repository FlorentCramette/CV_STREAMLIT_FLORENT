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

# Bloc unique profil avec accents corrigés et première phrase centrée
st.markdown(
    """
    <div class="section" style="text-align: left;">
        <h2 style='text-align: center;'>À propos de moi</h2>
        <p style='text-align: center;'><strong>Consultant technico-fonctionnel & Data Analyst</strong></p>
        <p>Passionné par la donnée et la transformation digitale, j’accompagne les entreprises dans l’optimisation de leurs processus grâce à l’ERP Odoo et à l’analyse de données.</p>
        <p>Mon parcours mêle expertise métier, esprit d’analyse et sens du service. Découvrez mon expérience de consultant, mes compétences en BI et mon goût pour l’automatisation et la valorisation de l’information.</p>
        <p>Envie d’un profil hybride, à la fois orienté métier et technique ? Échangeons !</p>
        <div style="margin-top: 30px; display: flex; flex-direction: column; align-items: center;">
            <a href="https://github.com/FlorentCramette" target="_blank" style="margin-bottom: 18px;">
                <img src="https://img.shields.io/badge/GitHub-Profil-blue?logo=github" alt="GitHub">
            </a>
            <a href="https://www.linkedin.com/in/florentcramette/" target="_blank" style="margin-bottom: 18px;">
                <img src="https://img.shields.io/badge/LinkedIn-Florent%20Cramette-blue?logo=linkedin" alt="LinkedIn">
            </a>
            <span style="font-size: 1.1em; color: #fff; margin-bottom: 10px;">
                <strong>Email :</strong> <a href="mailto:florent.cramette@gmail.com" style="color: #c56409;">florent.cramette@gmail.com</a>
            </span>
            <span style="font-size: 1.1em; color: #fff;">
                <strong>Téléphone :</strong> +33 (0)6 21 52 41 40
            </span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)



