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
if 'Merk' in df.columns and 'Verkoop' in df.columns:
    verkoop_per_merk = df.groupby('Merk')['Verkoop'].sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(data=verkoop_per_merk, x='Merk', y='Verkoop', ax=ax1)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    st.pyplot(fig1)
else:
    st.warning("Kolommen 'Merk' en/of 'Verkoop' niet gevonden in je data.")

# Tweede visual: Verkooplocaties op een scatterplot (voorbeeld)
st.subheader("Visual 2: Verkooplocaties")
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    st.map(df[['Latitude', 'Longitude']])
else:
    st.warning("Kolommen 'Latitude' en 'Longitude' niet gevonden voor kaartvisualisatie.")
