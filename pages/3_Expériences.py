import streamlit as st
import os

# Configure la page (doit être la première commande)
st.set_page_config(
    page_title="Expériences professionnelles",
    page_icon="📈",
    layout="wide",
)

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(os.path.join("assets", "style.css"))

# Contenu de la page
st.markdown("<h1>Expériences professionnelles</h1>", unsafe_allow_html=True)

# Expérience actuelle chez Easi Soft
st.markdown(
    """
    <div class="section">
        <h3>Consultant technico-fonctionnel Odoo</h3>
        <p><strong>Entreprise :</strong> Easi Soft</p>
        <p><strong>Période :</strong> 2025</p>
        <ul>
            <li>Amélioration de la qualité des données et reporting (SQL, Power BI)</li>
            <li>Développement et paramétrage de solutions sur mesure (multi-sociétés)</li>
            <li>Formation utilisateurs, rédaction de documentation et spécifications fonctionnelles</li>
            <li>Support à la direction dans ses décisions grâce à des analyses chiffrées</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# L'Équipeur - Responsable achats
st.markdown(
    """
    <div class="section">
        <h3>Responsable achats & approvisionnement</h3>
        <p><strong>Entreprise :</strong> L'Équipeur</p>
        <p><strong>Période :</strong> 2022 - 2023</p>
        <ul>
            <li>Mise en place de reportings Odoo + SQL pour le suivi des marges, stocks et achats</li>
            <li>Analyse de performance commerciale pour guider les décisions stratégiques</li>
            <li>Négociation fournisseurs et optimisation des flux logistiques</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Ekosport - Responsable de magasin
st.markdown(
    """
    <div class="section">
        <h3>Responsable de magasin</h3>
        <p><strong>Entreprise :</strong> Ekosport</p>
        <p><strong>Période :</strong> 2021 - 2022</p>
        <ul>
            <li>Pilotage d'un centre de profit via indicateurs de performance (CA, marge, panier moyen)</li>
            <li>Mise en place d'actions commerciales orientées données</li>
            <li>Formation et management d'équipe</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# INTERSPORT France - Responsable univers
st.markdown(
    """
    <div class="section">
        <h3>Responsable univers</h3>
        <p><strong>Entreprise :</strong> INTERSPORT France</p>
        <p><strong>Période :</strong> 2018 - 2020</p>
        <ul>
            <li>Suivi des KPI retail (CA, marge, rotation stock)</li>
            <li>Gestion des stocks et optimisation des linéaires</li>
            <li>Déploiement d'opérations commerciales locales et nationales</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Expériences antérieures groupées
st.markdown(
    """
    <div class="section">
        <h3>Expériences antérieures</h3>
        <p><strong>Période :</strong> 1994 - 2018</p>
        <ul>
            <li><strong>Création et gestion d'entreprise</strong> (Val de Saône Canoë)</li>
            <li><strong>Encadrement et pilotage d'équipes</strong> (Au Vieux Campeur, France Aventures, UCPA)</li>
            <li><strong>Développement commercial et gestion opérationnelle</strong> avec suivi de données (CA, fréquentation, rentabilité)</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)