import streamlit as st
import pandas as pd


csv_file_path = "1lm.csv"
# Chargement du fichier CSV en nettoyant les espaces dans la colonne Email
df = pd.read_csv(csv_file_path, delimiter=";", converters={"Email": lambda x: x.strip()})

# Titre de l'application
st.title("NOTES DE DS PYTHON 1LM A.U 2023-2024")

# Champ de saisie pour l'email de l'étudiant
email = st.text_input("Saisissez votre email")

# Vérification si l'email existe dans le fichier CSV
if email:
    if email in df["Email"].values:
        # Récupération des informations de l'étudiant correspondant à l'email
        etudiant = df[df["Email"] == email]
        nom = etudiant["Name"].values[0]
        groupe = etudiant["GROUP"].values[0]
        note = etudiant["Note"].values[0]
        
        # Affichage des informations de l'étudiant
        st.success(f"Nom de l'étudiant : {nom}")
        st.success(f"Groupe de l'étudiant : {groupe}")
        st.success(f"La note de l'étudiant est : {note}")
    else:
        st.error("Email non trouvé")