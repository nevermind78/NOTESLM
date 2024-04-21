import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt
csv_file_path = st.secrets["csv_file_path"]
# Chargement du fichier CSV en nettoyant les espaces dans la colonne Email
df = pd.read_csv(csv_file_path, delimiter=";", converters={"Email": lambda x: x.strip()})

# Titre de l'application
st.title("NOTES DE DS PYTHON")
st.header("1LM A.U 2023-2024")
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

def categorize_notes(note):
    if note < 10:
        return "Insuffisant (<10)"
    elif 10 <= note < 12:
        return "Passable (10-12)"
    elif 14 <= note < 16:
        return "Bien (14-16)"
    else:
        return "Très bien (>16)"


df["Catégorie de notes"] = df["Note"].apply(categorize_notes)

# Afficher les statistiques des notes sous forme de pie charts
st.write("Statistiques des notes :")
fig, ax = plt.subplots()
ax.pie(df["Catégorie de notes"].value_counts(), labels=df["Catégorie de notes"].value_counts().index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)