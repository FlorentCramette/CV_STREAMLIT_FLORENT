import streamlit as st
import os

# Configure la page (doit être la première commande)
st.set_page_config(
    page_title="Expériences professionnelles",
    page_icon="📈",
)

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(os.path.join("assets", "style.css"))

# Contenu de la page
st.markdown("<h1>Expériences professionnelles</h1>", unsafe_allow_html=True)

# Liste des expériences professionnelles
st.markdown(
    """
    <div class="section">
        <h3>Responsable des achats</h3>
        <p><strong>Entreprise :</strong> L’Équipeur</p>
        <p><strong>Période :</strong> Janvier 2022 - Août 2023</p>
        <ul>
            <li>Approvisionnement, négociations, sélection et élaboration des gammes.</li>
            <li>Gestion des stocks et aide aux décisions commerciales.</li>
            <li>Partenariats avec les fournisseurs pour des actions commerciales.</li>
            <li>Élaboration des KPIs sur Excel pour optimiser les performances.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
        <h3>Responsable de rayon / magasin</h3>
        <p><strong>Entreprise :</strong> Au vieux campeur / Intersport / Ekosport</p>
        <p><strong>Période :</strong> 2007 - Décembre 2021</p>
        <ul>
            <li>Management des équipes de vente et formation des conseillers.</li>
            <li>Gestion opérationnelle d'un centre de profit, avec suivi des objectifs.</li>
            <li>Analyse des performances commerciales via Power BI et Excel.</li>
            <li>Optimisation des processus internes pour améliorer les résultats.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
