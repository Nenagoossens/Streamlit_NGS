import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pagina-instellingen (optioneel)
st.set_page_config(page_title="Schoenen Verkoop Dashboard", layout="centered")

# Titel
st.title("Exclusieve Schoenen Verkoop Dashboard")

# CSV inladen
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Toon de data in de app (optioneel)
st.subheader("Data Voorbeeld")
st.dataframe(df.head())

# Eerste visual: Verkoop per merk
st.subheader("Visual 1: Totale Verkoop per Merk")
if 'merk' in df.columns and 'verkoop' in df.columns:
    verkoop_per_merk = df.groupby('verk')['verkoop'].sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(data=verkoop_per_merk, x='merk', y='verkoop', ax=ax1)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    st.pyplot(fig1)
else:
    st.warning("Kolommen 'merk' en/of 'verkoop' niet gevonden in je data.")

# Tweede visual: Verkooplocaties op een scatterplot (voorbeeld)
st.subheader("Visual 2: Verkooplocaties")
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    st.map(df[['Latitude', 'Longitude']])
else:
    st.warning("Kolommen 'Latitude' en 'Longitude' niet gevonden voor kaartvisualisatie.")
