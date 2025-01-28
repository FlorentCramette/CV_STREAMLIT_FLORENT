import streamlit as st
import os

# Configuration de la page
st.set_page_config(page_title="Centres d'intérêt", page_icon="🌍")

# Charger le CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(os.path.join("assets", "style.css"))

st.markdown("<h1>Centres d'intérêt</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="section">
        <ul>
            <li>Cinéma, lecture, théâtre et informatique</li>
            <li>Sports outdoors : kayak, VTT, randonnée pédestre et à ski</li>
            <li>Bricolage et construction</li>
            <li>Voyages</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Afficher le carrousel d'images
image_folder = os.path.join("assets", "images_caroussel")
if os.path.exists(image_folder):
    images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    if "current_image" not in st.session_state:
        st.session_state.current_image = 0

    current_image = st.session_state.current_image
    st.image(images[current_image], use_container_width=True, caption=f"Image {current_image + 1}/{len(images)}")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("⬅️ Précédent"):
            st.session_state.current_image = (current_image - 1) % len(images)
    with col3:
        if st.button("➡️ Suivant"):
            st.session_state.current_image = (current_image + 1) % len(images)
else:
    st.error("Le dossier d'images n'existe pas.")
