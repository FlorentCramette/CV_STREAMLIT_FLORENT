
import streamlit as st# Expérience actuelle chez Easi-Soft
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
)figure la page (doit être la première commande)
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

# Expérience actuelle chez Easi-Soft
st.markdown(
    """
    <div class="section">
        <h3>Consultant technico-fonctionnel Odoo</h3>
        <p><strong>Entreprise :</strong> Easi-Soft</p>
        <p><strong>Période :</strong> Mars 2025 - Octobre 2025 (CDD)</p>
        <ul>
            <li>Accompagnement des clients dans la mise en place et l’optimisation de la solution ERP Odoo.</li>
            <li>Analyse des besoins métiers et rédaction des cahiers des charges fonctionnels.</li>
            <li>Paramétrage, formation des utilisateurs et support technique.</li>
            <li>Interface entre les équipes techniques et les utilisateurs finaux.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Liste des expériences professionnelles précédentes
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

st.markdown(
    """
    <div class="section">
        <h3>Responsable d'un parc accrobatique en hauteur</h3>
        <p><strong>Entreprise :</strong> France Aventures</p>
        <p><strong>Période :</strong> Avril 2006 - Septembre 2007</p>
        <ul>
            <li>Management et formation des opérateurs du parc.</li>
            <li>Gestion opérationnelle d'un centre de profit, avec suivi des objectifs.</li>
            <li>Analyse des performances commerciales via Power BI et Excel.</li>
            <li>Construction et maintenance du parc et suivi des registres de sécurité.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="section">
        <h3>Responsable des activités</h3>
        <p><strong>Entreprise :</strong> UCPA</p>
        <p><strong>Période :</strong> 1993 - Septembre 2005</p>
        <ul>
            <li>Management des équipes de moniteurs.</li>
            <li>Gestion opérationnelle du matériel et des sites de pratique, avec suivi des objectifs.</li>
            <li>Elaboration des plannings d'activités interne et externe.</li>
            <li>Création de nouveaux produits de randonnées itinérantes en kayak.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
