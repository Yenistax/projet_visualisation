import streamlit as st
import pandas as pd
import numpy as np



@st.cache_data
def load_data():
    return pd.read_csv("./csv/tri/df_final.csv", low_memory=False, sep=",", encoding="utf-8")
df = load_data()

# Conversion de la colonne de temps en format datetime si elle n'est pas déjà convertie
if 'hrmn' in df.columns:
    df['hrmn'] = pd.to_datetime(df['hrmn'], format='%H:%M:%S')

# Calcul des heures les plus communes
accidents_by_hour = df['hrmn'].dt.hour.value_counts().sort_index()
most_common_hours = accidents_by_hour.nlargest(5)  # Prend les 5 heures avec le plus d'accidents

# Affichage des heures les plus communes
st.title('Analyse des accidents')
st.write('Heures avec le plus d\'accidents:')
for hour, count in most_common_hours.items():
    st.write(f"{hour}:00 - {hour+1}:00 : {count} accidents")