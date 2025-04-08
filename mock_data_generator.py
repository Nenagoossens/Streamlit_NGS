import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pagina-instellingen
st.set_page_config(page_title="Schoenen Verkoop Dashboard", layout="centered")

# Titel
st.title("Exclusieve Schoenen Verkoop Dashboard")

# Data inladen
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Toon een voorbeeld van de data
st.subheader("Voorbeeld van de data")
st.dataframe(df.head())

# Visual 1: Aantal orders per land
st.subheader("Aantal orders per land")
if 'order-id' in df.columns and 'land' in df.columns:
    orders_per_land = df.groupby('land')['order-id'].nunique().reset_index()
    orders_per_land = orders_per_land.sort_values('order-id', ascending=False)
    
    fig1, ax1 = plt.subplots()
    sns.barplot(data=orders_per_land, x='land', y='order-id', ax=ax1)
    ax1.set_xlabel("Land")
    ax1.set_ylabel("Aantal unieke orders")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    st.pyplot(fig1)
else:
    st.warning("Kolommen 'order-id' en/of 'land' niet gevonden in de dataset.")

# Visual 2: Aantal orders per producttype
st.subheader("Aantal orders per producttype")
if 'order-id' in df.columns and 'product_naam' in df.columns:
    orders_per_product = df.groupby('product_naam')['order-id'].nunique().reset_index()
    orders_per_product = orders_per_product.sort_values('order-id', ascending=False)

    fig2, ax2 = plt.subplots()
    sns.barplot(data=orders_per_product, x='product_naam', y='order-id', ax=ax2)
    ax2.set_xlabel("Productnaam")
    ax2.set_ylabel("Aantal unieke orders")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha="right")
    st.pyplot(fig2)
else:
    st.warning("Kolommen 'order-id' en/of 'product_naam' niet gevonden in de dataset.")
