import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

# Configuration de la page
st.set_page_config(page_title="Projets - Analyse du Marché du Vin", layout="wide")

st.markdown(
    """
    <style>
        .block-container {
            max-width: 800px;  /* Ajuste cette valeur pour réduire la largeur */
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍷 Analyse du Marché du Vin et Prédiction de Prix")

## **1️⃣ Présentation de l'Étude**
st.write(
    "Dans le cadre de ma certification Data Analyst, j'ai réalisé une étude de marché "
    "pour estimer le prix d'une bouteille de vin sur le marché américain. L'étude comprend :"
)
st.markdown("- **Exploration et nettoyage des données** 🧹\n"
            "- **Visualisation des tendances** 📊\n"
            "- **Modélisation Machine Learning** 🤖\n"
            "- **Prédiction du prix d'un vin spécifique** 💰")

# Bouton pour télécharger le notebook Colab
with open("assets/Florent_CRAMETTE_Certification_Data_Analyst_Cas _Pratiques.ipynb", "rb") as f:
    st.download_button(
        label="📥 Télécharger le notebook Colab",
        data=f,
        file_name="Florent_CRAMETTE_Certification_Data_Analyst_Cas_Pratiques.ipynb",
        mime="application/octet-stream"
    )

## **2️⃣ Chargement et exploration des données**
@st.cache_data
def load_data():
    df = pd.read_csv("assets/df_wine_filled.csv")  # Mise à jour du chemin
    return df

df = load_data()

st.subheader("📌 Aperçu du Dataset")
st.write(df.head())

## **3️⃣ Nettoyage et amélioration des données**
st.subheader("🧹 Nettoyage des Données")
st.write("Avant d'entraîner notre modèle, nous avons procédé aux étapes suivantes :")
st.markdown("- Suppression des colonnes non pertinentes (ex: `taster_name`, `taster_twitter_handle`).\n"
            "- Remplissage des valeurs manquantes :\n"
            "  - Si la province est absente, elle est remplacée par `Inconnu`.\n"
            "  - Si le prix est manquant, suppression de la ligne (trop critique).\n"
            "- Encodage des variables catégoriques pour la modélisation.")

st.write("Voici les valeurs manquantes par colonne après nettoyage :")
st.write(df.isnull().sum())

# Suppression des valeurs nulles dans la colonne 'price'
df = df.dropna(subset=['price'])

# Affichage de la heatmap des valeurs nulles
with st.container():
    st.subheader("🗺️ Carte des Valeurs Manquantes")
    fig, ax = plt.subplots(figsize=(2, 1.5))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
    ax.set_title("Carte des Valeurs Manquantes")
    st.pyplot(fig)

st.write("📌 Aperçu des données après nettoyage :")
st.write(df.head())

## **4️⃣ Visualisation des données**
st.subheader("📊 Distribution des Prix du Vin")
with st.container():
    fig, ax = plt.subplots(figsize=(2, 1.5))
    sns.histplot(df['price'], bins=30, kde=True, ax=ax)
    ax.set_title("Répartition des prix des vins")
    st.pyplot(fig)

# Affichage du boxplot pour détecter les outliers
st.subheader("📌 Analyse des Prix et Outliers")
with st.container():
    fig, ax = plt.subplots(figsize=(2, 1.5))
    sns.boxplot(x=df['price'], ax=ax)
    ax.set_title("Boxplot des Prix des Vins")
    st.pyplot(fig)

st.write("💡 Les prix du vin présentent une forte variabilité, mais les valeurs élevées ne doivent pas être considérées comme des outliers.")
st.write("Il est courant d'avoir des bouteilles à prix très élevé en fonction de la région et de la rareté du vin.")

## **5️⃣ Modèle Machine Learning pour la prédiction du prix**
st.subheader("🤖 Modélisation et Prédiction du Prix")

# Encodage des variables catégoriques
features = ["points", "country", "province", "variety"]
label_encoders = {}
for col in ["country", "province", "variety"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df[features]
y = df["price"]

# Vérification et suppression des valeurs nulles restantes dans 'y'
y = y.dropna()
X = X.loc[y.index]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choix du modèle de ML
model_choice = st.radio("Sélectionnez un modèle de Machine Learning", ["Random Forest", "Gradient Boosting"])

if model_choice == "Random Forest":
    n_estimators = st.slider("Nombre d'arbres (n_estimators)", 10, 200, 50, 10)
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=42, n_jobs=-1)
else:
    learning_rate = st.slider("Taux d'apprentissage (learning_rate)", 0.01, 0.5, 0.1, 0.01)
    n_estimators = st.slider("Nombre d'arbres (n_estimators)", 10, 200, 50, 10)
    model = GradientBoostingRegressor(n_estimators=n_estimators, learning_rate=learning_rate, random_state=42)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
st.write(f"**Erreur moyenne absolue du modèle :** {mae:.2f} $")

## **6️⃣ Prédiction pour un vin spécifique**
st.subheader("💰 Prédiction du Prix pour le Domaine des Croix 2016 - Corton Grèves")
vin_exemple = pd.DataFrame({
    "points": [94],
    "country": [label_encoders["country"].transform(["France"])[0]],
    "province": [label_encoders["province"].transform(["Burgundy"])[0]],
    "variety": [label_encoders["variety"].transform(["Pinot Noir"])[0]],
})
prix_prevu = model.predict(vin_exemple)[0]
st.success(f"💲 Prix estimé sur le marché américain : {prix_prevu:.2f} $")

## **7️⃣ Conclusion et recommandations**
st.write(
    "L'analyse des tendances du marché et l'utilisation d'un modèle robuste de Machine Learning "
    "nous permettent d'obtenir une estimation fiable du prix des vins en fonction de leurs caractéristiques. "
    "L'ajout de paramètres personnalisables permet d'optimiser les performances du modèle."
)
