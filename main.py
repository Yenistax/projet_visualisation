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
    st.write(st.bar_chart(df["sexe"]))

#compter le nombre d'hommme qui ont eu un accident

st.write((df["sexe"] == "Masculin").sum())
st.write((df["sexe"] == "Féminin").sum())

st.write(((df["grav"] == "Tué") & (df["sexe"] == "Masculin")).sum())
st.write(((df["grav"] == "Tué") & (df["sexe"] == "Féminin")).sum())

data = []