import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit instellingen
st.set_page_config(page_title="Schoenen Verkoop Dashboard", layout="wide")

# Titel
st.title("📊 Exclusieve Schoenen Verkoop Dashboard")

# CSV inladen
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Kolomnamen opschonen
df.columns = df.columns.str.strip().str.lower()

# Kolomnamen tonen (optioneel, handig voor debug)
st.sidebar.subheader("📌 Kolomnamen in de dataset:")
st.sidebar.write(df.columns.tolist())

# Check op benodigde kolommen
vereiste_kolommen = ['order-id', 'land', 'product_naam']
if all(kol in df.columns for kol in vereiste_kolommen):

    # Aantal orders per land
    st.subheader("🌍 Aantal orders per land")
    orders_per_land = df.groupby('land')['order-id'].nunique().reset_index()
    orders_per_land = orders_per_land.sort_values('order-id', ascending=False)

    fig1, ax1 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=orders_per_land, x='land', y='order-id', ax=ax1)
    ax1.set_xlabel("Land")
    ax1.set_ylabel("Aantal unieke orders")
    ax1.set_title("Aantal orders per land")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig1)

    # Aantal orders per producttype
    st.subheader("👟 Aantal orders per type product")
    orders_per_product = df.groupby('product_naam')['order-id'].nunique().reset_index()
    orders_per_product = orders_per_product.sort_values('order-id', ascending=False)

    fig2, ax2 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=orders_per_product, x='product_naam', y='order-id', ax=ax2)
    ax2.set_xlabel("Productnaam")
    ax2.set_ylabel("Aantal unieke orders")
    ax2.set_title("Aantal orders per producttype")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig2)

else:
    st.error(f"❌ De vereiste kolommen ontbreken. Zorg dat de CSV minimaal de volgende kolommen bevat: {vereiste_kolommen}")
