import streamlit as st
import pandas as pd

# Load and clean data
@st.cache_data
def load_data():
    data = pd.read_csv("google_play_store_dataset.csv")
    return data

data = load_data()

# Convert 'Size' and 'Installs' columns to numeric values for sorting
def clean_data(df):
    df['Size'] = df['Size'].replace('Varies with device', None)
    df['Size'] = df['Size'].str.replace('M', 'e6').str.replace('k', 'e3').astype(float)
    df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(float)
    df['Price'] = df['Price'].str.replace('$', '').astype(float)
    return df

data = clean_data(data)

# Title and introductory information
st.title("Google Play Store Apps Explorer")
st.markdown("Descubre información detallada del conjunto de datos de Google Play Store. Filtra apps por categoría, ordena por tamaño, precio, y descargas para explorar tendencias y métricas de rendimiento.")

# Sidebar - Filter and Sort Options
st.sidebar.header("Opciones de Filtro y Orden")
category = st.sidebar.selectbox("Elige una categoría", options=data['Category'].unique())
sort_by = st.sidebar.selectbox("Ordenar por", options=['Size', 'Price', 'Installs'])
sort_order = st.sidebar.radio("Orden", options=['Descendente', 'Ascendente'])

# Filter by category and sort
filtered_data = data[data['Category'] == category]
sorted_data = filtered_data.sort_values(by=sort_by, ascending=(sort_order == 'Ascendente'))

# Main Section with Sorted Data
st.subheader(f"Aplicaciones en la categoría: {category}")
st.write(f"Ordenado por {sort_by} en orden {sort_order.lower()}.")
st.dataframe(sorted_data[['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price']])

# Interactive Buttons for Insights
st.sidebar.header("Explora los Insights")
if st.sidebar.button("Análisis de Peso de la App"):
    st.subheader("Análisis de Peso de la App")
    st.markdown("""
    - **Pesadas**: Juegos y aplicaciones multimedia suelen ser las de mayor tamaño.
    - **Medianas**: Aplicaciones de productividad y redes sociales equilibran características y tamaño.
    - **Livianas**: Aplicaciones de utilidad priorizan un impacto mínimo en el almacenamiento.
    """)

if st.sidebar.button("Exploración de Rango de Precios"):
    st.subheader("Exploración de Rango de Precios")
    st.markdown("""
    - **Aplicaciones Premium**: Herramientas profesionales de alta gama con precios elevados.
    - **Gama Media**: Aplicaciones de calidad que equilibran características y asequibilidad.
    - **Aplicaciones Gratuitas**: La mayoría de las aplicaciones, a menudo monetizadas a través de anuncios.
    """)

if st.sidebar.button("Tendencias de Descargas"):
    st.subheader("Tendencias de Descargas")
    st.markdown("""
    - **Top**: Redes sociales y utilidades esenciales lideran las descargas.
    - **Estrellas Emergentes**: Aplicaciones innovadoras que ganan popularidad rápidamente.
    - **Crecimiento Sostenido**: Crecimiento constante en mercados de nicho.
    """)

