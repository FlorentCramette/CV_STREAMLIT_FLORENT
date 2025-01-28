import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mes Compétences", page_icon="💼")

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

# Contenu principal
st.markdown("<h1>Mes Compétences</h1>", unsafe_allow_html=True)

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
    "Analyse et structuration des données",
    "Nettoyage et transformation des données",
    "SQL, Python (Pandas, NumPy, Scikit-learn...)",
    "Power BI, Tableau (visualisation des données)",
    "Streamlit, Django (présentation web)"
    "Excel, VBA (TOSA niveau avancé)",
    "Modélisation et machine learning",
    
]

# Affichage en deux colonnes
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("💡 Soft Skills")
    st.markdown(
        "<ul class='skills-list'>" +
        "".join([f"<li>{skill}</li>" for skill in soft_skills]) +
        "</ul>",
        unsafe_allow_html=True,
    )

with col2:
    st.subheader("🔧 Hard Skills")
    st.markdown(
        "<ul class='skills-list'>" +
        "".join([f"<li>{skill}</li>" for skill in hard_skills]) +
        "</ul>",
        unsafe_allow_html=True,
    )

