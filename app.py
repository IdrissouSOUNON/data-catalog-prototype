import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Catalogue Data Bénin", layout="wide")

st.title("📊 Catalogue National de Données Publiques")
st.markdown("Plateforme de consultation et d'exploration des données publiques")

with open("catalog.json", encoding="utf-8") as f:
    catalog = json.load(f)

# SIDEBAR
st.sidebar.header("📂 Navigation")

dataset_names = [d["title"] for d in catalog["datasets"]]
selected_dataset = st.sidebar.selectbox("Choisir un dataset", dataset_names)

dataset = next(d for d in catalog["datasets"] if d["title"] == selected_dataset)

df = pd.read_csv(f"data/{dataset['file']}")

# INFOS DATASET
st.subheader(dataset["title"])
st.info(dataset["description"])
st.caption(f"Source : {dataset.get('source', 'Non spécifiée')}")

# FILTRES
st.sidebar.header("🔎 Filtres")

if "ville" in df.columns:
    villes = st.sidebar.multiselect("Ville", df["ville"].unique())
    if villes:
        df = df[df["ville"].isin(villes)]

if "type" in df.columns:
    types = st.sidebar.multiselect("Type", df["type"].unique())
    if types:
        df = df[df["type"].isin(types)]

# METRICS
st.markdown("### 📈 Aperçu des données")
col1, col2 = st.columns(2)
col1.metric("Nombre d'enregistrements", len(df))
col2.metric("Nombre de colonnes", len(df.columns))

# TABLE
st.dataframe(df, use_container_width=True)