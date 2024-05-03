import streamlit as st
import pandas as pd
import os 
import plotly.express as px

st.set_page_config(page_title="Notes Python 1LM", page_icon=":bar_chart:")
csv_file_path = st.secrets['csv_file_path']

#csv_file_path ='notes.csv'
# Chargement du fichier CSV en nettoyant les espaces dans la colonne Email
df = pd.read_csv(csv_file_path, delimiter=",", converters={"Email": lambda x: x.strip()})

# Titre de l'application
st.title("NOTES DS et TP PYTHON")
st.header("1LM A.U 2023-2024")
# Champ de saisie pour l'email de l'étudiant
email = st.text_input("Saisissez votre email")
def categorize_notes(note):
    if note < 10:
        return "Insuffisant (<10)"
    elif 10 <= note < 12:
        return "Passable (10-12)"
<<<<<<< HEAD
    elif 12 <= note < 14:
        return "Bien (12-14)"
=======
    elif 12<= note < 14:
        return "Assez Bien(12-14)"
>>>>>>> afc25d77b1b966d519fdf7746ce655ac23e9ed2d
    elif 14 <= note < 16:
        return "Bien (14-16)"
    else:
        return "Très bien (>16)"
df["TP"] = pd.to_numeric(df["TP"], errors='coerce').fillna(0)
df["DS"] = pd.to_numeric(df["DS"], errors='coerce').fillna(0)
df["Catégorie de notes DS"] = df["DS"].apply(categorize_notes)
df["Catégorie de notes TP"] = df["TP"].apply(categorize_notes)

# Vérification si l'email existe dans le fichier CSV
if email:
    if email in df["Email"].values:
        # Récupération des informations de l'étudiant correspondant à l'email
        etudiant = df[df["Email"] == email]
        nom = etudiant["Name"].values[0]
        groupe = etudiant["GROUP"].values[0]
        noteDS = etudiant["DS"].values[0]
        noteTP = etudiant["TP"].values[0]
        # Création d'un dictionnaire contenant les informations de l'étudiant
        etudiant_info = {
                        "Nom": nom,
                        "Groupe": groupe,
                        "DS": noteDS,
                        "TP": noteTP
                    }
        res = pd.DataFrame.from_dict(etudiant_info, orient='index', columns=['Résultats'])
        res['Résultats'] = res['Résultats'].astype(str)
        # Affichage des informations de l'étudiant dans un tableau
        st.subheader("Résultats de l'étudiant")
        a,b,c = st.columns(3)
        with b:
            st.write(res, unsafe_allow_html=True)
    else:
        st.error("Email non trouvé")



# Calculer les statistiques des notes pour le pie chart
stats_notesDS = df["Catégorie de notes DS"].value_counts()
stats_notesTP = df["Catégorie de notes TP"].value_counts()

<<<<<<< HEAD

# Créer le pie chart avec Plotly en spécifiant la taille
col1,_,col2 = st.columns(3)
figds = px.pie(values=stats_notesDS, names=stats_notesDS.index, title="Statistiques des notes DS", width=350, height=350)
figtp = px.pie(values=stats_notesTP, names=stats_notesTP.index, title="Statistiques des notes TP", width=350, height=350)
col1.plotly_chart(figtp)
col2.plotly_chart(figds)
=======
# Créer le pie chart avec Plotly
fig = px.pie(values=stats_notes, names=stats_notes.index, title="Statistiques des notes")
st.plotly_chart(fig)
>>>>>>> afc25d77b1b966d519fdf7746ce655ac23e9ed2d
