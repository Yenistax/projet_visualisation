import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("Sécurité routière, tous touchés, tous concernés, tous responsables")
st.divider()

#if "df" not in st.session_state:
    #st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

#st.header("Choose a datapoint color")
#color = st.color_picker("Color", "#FF0000")
#st.divider()
#st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

jours_de_fete = ["1", "14", "24"]
mois_de_fete = ["1", "7", "12"]

@st.cache_data
def load_data():
    return pd.read_csv("./csv/tri/df_final.csv", low_memory=False, sep=",", encoding="utf-8")
df = load_data()

@st.cache_data
def afficher_df():
    return df.head()

st.write(afficher_df())

@st.cache_data
def afficher_chart():
    return st.bar_chart(df["jour"])

st.write("test of day")
for i in jours_de_fete:
    if df["jour"] == i:
        st.write(afficher_chart())

st.write("test of month")
for i in mois_de_fete:
    if df["mois"] == i:
        st.write(afficher_chart())
