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
        <p>
            <strong>Passionné par l’analyse de données</strong> et animé par une volonté constante de transformer les informations brutes en 
            leviers décisionnels, je possède une expertise solide en gestion et dans le secteur retail. Mon parcours m’a permis de développer 
            une vision stratégique et opérationnelle des métiers, tout en acquérant une compréhension fine des enjeux business.
        </p>
        <p>
            Après une carrière enrichissante dans le <strong>management sportif</strong> et le <strong>retail</strong>, où j’ai occupé des postes 
            à responsabilité tels que l’approvisionnement, la gestion d’équipes, et la mise en œuvre d’actions commerciales, 
            j’ai choisi de me spécialiser dans les métiers de la data. Cette transition s’appuie sur une <strong>solide formation</strong> 
            et un développement constant de mes compétences techniques.
        </p>
        <p>
            Aujourd’hui, je mets à profit mes compétences en <strong>BI (Power BI, Tableau, SQL)</strong> et <strong>Python</strong>, 
            ainsi que mon goût pour la modélisation avancée, pour accompagner les entreprises dans leurs prises de décisions stratégiques. 
            J’aime particulièrement :
        </p>
        <ul>
            <li><strong>Analyser et traiter des données complexes</strong> pour en extraire des insights clairs et exploitables ;</li>
            <li><strong>Automatiser et optimiser des processus</strong> via des solutions déployables en production ;</li>
            <li><strong>Faire parler les chiffres</strong> à travers des visualisations impactantes ;</li>
            <li><strong>Prédire des tendances</strong> grâce à des modèles d’analyse prédictive et des approches machine learning.</li>
        </ul>
        <p>
            La mise en production de solutions robustes et le suivi de leur impact sur la performance des entreprises 
            sont pour moi des étapes clés. En combinant mes compétences techniques, ma curiosité, et mon expérience métier, 
            je suis convaincu de pouvoir apporter une <strong>valeur ajoutée durable</strong> et adaptée aux besoins spécifiques des organisations.
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
