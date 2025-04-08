import streamlit as st
import pandas as pd
import plotly.express as px

# Titel
st.title("Exclusieve Schoenen Verkoop Dashboard")

# Data inladen
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Toon een stukje van de data
st.subheader("Voorbeeld van de data")
st.dataframe(df.head())

# Visual 1: Top 10 best verkochte schoenen
st.subheader("Top 10 best verkochte schoenen")
top_schoenen = df['schoen_naam'].value_counts().nlargest(10).reset_index()
top_schoenen.columns = ['schoen_naam', 'aantal_verkocht']

fig1 = px.bar(top_schoenen, x='schoen_naam', y='aantal_verkocht', 
              labels={'schoen_naam': 'Schoen', 'aantal_verkocht': 'Aantal verkocht'},
              title='Top 10 best verkochte schoenen')
st.plotly_chart(fig1)

# Visual 2: Verkooplocaties op kaart
st.subheader("Verkooplocaties")
# Zorg dat er kolommen zijn voor latitude en longitude
if 'latitude' in df.columns and 'longitude' in df.columns:
    st.map(df[['latitude', 'longitude']])
else:
    st.warning("De dataset bevat geen locatiegegevens (latitude & longitude).")

