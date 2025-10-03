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
        <p style='text-align: center;'><strong>Data Analyst certifié</strong></p>
        <p>Data Analyst certifié, avec une expertise à la croisée de la donnée et du métier. Fort de 15+ ans d'expérience en retail, management et ERP (Odoo), j'ai acquis une compréhension approfondie des processus commerciaux et opérationnels.</p>
        <p>Aujourd'hui, je mets mes compétences en SQL, Python et Power BI au service de la valorisation des données, en transformant les flux bruts en insights actionnables pour soutenir la performance et la prise de décision.</p>
        <p>💡 Mon atout : associer vision métier (achats, stocks, ventes, logistique) et compétences techniques pour créer des solutions data pragmatiques et impactantes.</p>
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