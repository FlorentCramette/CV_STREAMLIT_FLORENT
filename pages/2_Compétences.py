import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Mes Compétences",
    page_icon="💼")

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

# Forcer la largeur maximale de la page à 1400px (sûr)
st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 1400px !important;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenu principal
st.markdown("<h1>Mes Compétences</h1>", unsafe_allow_html=True)

# Bouton de téléchargement du CV et lien démo
col1, col2 = st.columns(2)
with col1:
    with open("assets/CV_Florent_Cramette_Data_Final.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Télécharger mon CV",
            data=pdf_file,
            file_name="CV_Florent_Cramette_Data_Final.pdf",
            mime="application/pdf"
        )
with col2:
    st.markdown(
        """
        <a href="https://retailgeodatacase-jjdsfxbvgmdwn3n4yzh6pg.streamlit.app/" target="_blank" style="
            display: inline-block;
            background-color: #c56409;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            margin-bottom: 10px;
        ">🌍 Démo Retail GeoData Case</a>
        """,
        unsafe_allow_html=True
    )

# Organisation des compétences
soft_skills = [
    "Curieux et autodidacte",
    "Capacité d'adaptation",
    "Leadership bienveillant",
    "Prise d'initiative",
    "Force de proposition",
    "Collaboration et travail en équipe",
    "Rigueur et organisation",
]

hard_skills = [
    "Extract, Transform, Load (ETL)",
    "Nettoyage et transformation des données",
    "SQL, Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)",
    "Power BI, Tableau (visualisation des données)",
    "Streamlit, Django (présentation web)",
    "Excel, VBA (TOSA niveau avancé)",
    "Machine Learning (régression, classification)",
    "Bases de données relationnelles (PostgreSQL, MySQL)",
    "Git, GitHub (gestion de versions)",
    # Compétences Odoo
    "Odoo : paramétrage fonctionnel des modules (ventes, achats, stocks, CRM, facturation...)",
    "Odoo : analyse des besoins métiers et rédaction de cahiers des charges",
    "Odoo : formation et accompagnement des utilisateurs",
    "Odoo : support, tests et recette fonctionnelle",
    "Odoo : gestion de projets d'implémentation ERP",
]

# Affichage des listes l'une sous l'autre, pleine largeur
st.markdown(
    """
    <div style='width: 100%; max-width: 1200px; margin: 0 auto 2rem auto;'>
        <h3>💡 Soft Skills</h3>
        <ul class='skills-list'>
            {soft}
        </ul>
    </div>
    <div style='width: 100%; max-width: 1200px; margin: 0 auto 2rem auto;'>
        <h3>🔧 Hard Skills</h3>
        <ul class='skills-list'>
            {hard}
        </ul>
    </div>
    """.format(
        soft="".join([f"<li>{skill}</li>" for skill in soft_skills]),
        hard="".join([f"<li>{skill}</li>" for skill in hard_skills])
    ), unsafe_allow_html=True)

