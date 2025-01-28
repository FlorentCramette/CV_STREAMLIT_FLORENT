import streamlit as st
import os

# Configure la page (doit être la première commande)
st.set_page_config(
    page_title="Compétences",
    page_icon="💡",
)

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(os.path.join("assets", "style.css"))

# Contenu de la page
st.markdown("<h1>Compétences</h1>", unsafe_allow_html=True)

# Liste des compétences
st.markdown(
    """
    <div class="section">
        <ul>
            <li><strong>Analyse, exploitation et structuration des données :</strong> Compétence clé pour transformer des données brutes en insights exploitables.</li>
            <li><strong>Présentation et diffusion des résultats :</strong> Communication claire et visuelle via des outils BI (Power BI, Tableau).</li>
            <li><strong>Langages techniques :</strong> SQL, Python, DAX pour l’analyse avancée et l’automatisation.</li>
            <li><strong>Maîtrise des outils :</strong> Power BI, Tableau, Excel (TOSA niveau avancé), VBA.</li>
            <li><strong>Rigueur et précision :</strong> Focus sur les détails et la qualité des données.</li>
            <li><strong>Prise d’initiatives :</strong> Force de proposition dans des contextes variés.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
