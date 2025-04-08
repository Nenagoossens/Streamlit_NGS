import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Laad de CSV-bestand
df = pd.read_csv('exclusieve_schoenen_verkoop_met_locatie.csv')

# Verander de kolomnaam 'verkoop_datum' naar 'aankoopdatum'
df['aankoopdatum'] = pd.to_datetime(df['aankoopdatum'])

# Maak de tabs
tab1, tab2 = st.tabs(["Verkopen per Maand", "Verkopen per Land"])

# Tab 1 - Verkopen per maand
with tab1:
    # Groepeer de data per maand
    df['maand'] = df['aankoopdatum'].dt.to_period('M')
    maand_verkopen = df.groupby('maand')['prijs'].sum()

    # Plot de maandelijkse verkopen
    plt.figure(figsize=(10, 6))
    maand_verkopen.plot(kind='bar', color='skyblue')
    plt.title('Verkopen per Maand')
    plt.xlabel('Maand')
    plt.ylabel('Prijs (€)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Tab 2 - Verkopen per land
with tab2:
    # Groepeer de data per land
    land_verkopen = df.groupby('land')['prijs'].sum()

    # Plot de verkopen per land
    plt.figure(figsize=(10, 6))
    land_verkopen.plot(kind='bar', color='green')
    plt.title('Verkopen per Land')
    plt.xlabel('Land')
    plt.ylabel('Prijs (€)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

