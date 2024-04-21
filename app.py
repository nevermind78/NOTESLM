import streamlit as st
import pandas as pd
import os 
import plotly.express as px

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
        if type(note)==str:
            st.warning("A : Abscent")

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

df["Note"] = pd.to_numeric(df["Note"], errors='coerce').fillna(0)
df["Catégorie de notes"] = df["Note"].apply(categorize_notes)


# Calculer les statistiques des notes pour le pie chart
stats_notes = df["Catégorie de notes"].value_counts()

# Créer le pie chart avec Plotly
fig = px.pie(values=stats_notes, names=stats_notes.index, title="Statistiques des notes")
st.plotly_chart(fig)