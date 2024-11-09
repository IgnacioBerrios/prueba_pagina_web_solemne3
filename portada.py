import streamlit as st
import pandas as pd

# Load and clean data
@st.cache_data
def load_data():
    data = pd.read_csv("google_play_store_dataset.csv")
    return data

def clean_data(df):
    # Reemplazar valores no numéricos en 'Size'
    df['Size'] = df['Size'].replace('Varies with device', None)
    # Eliminar espacios y reemplazar 'M' y 'k' con potencias de 10
    df['Size'] = df['Size'].str.replace('M', 'e6', regex=False).str.replace('k', 'e3', regex=False)
    # Convertir a float, manejando errores
    df['Size'] = pd.to_numeric(df['Size'], errors='coerce')
    
    # Convertir 'Installs' a valores numéricos eliminando '+' y ','
    df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(float)
    
    # Convertir 'Price' a valores numéricos eliminando '$'
    df['Price'] = df['Price'].str.replace('$', '').astype(float)
    
    return df

# Cargar y limpiar los datos
data = load_data()
data = clean_data(data)

# Título e información introductoria
st.title("Google Play Store Apps Explorer")
st.markdown("Descubre información detallada del conjunto de datos de Google Play Store. Filtra apps por categoría, ordena por tamaño, precio, y descargas para explorar tendencias y métricas de rendimiento.")

# Sidebar - Opciones de filtro y ordenación
st.sidebar.header("Opciones de Filtro y Orden")
category = st.sidebar.selectbox("Elige una categoría", options=data['Category'].unique())
sort_by = st.sidebar.selectbox("Ordenar por", options=['Size', 'Price', 'Installs'])
sort_order = st.sidebar.radio("Orden", options=['Descendente', 'Ascendente'])

# Filtrar por categoría y ordenar
filtered_data = data[data['Category'] == category]
sorted_data = filtered_data.sort_values(by=sort_by, ascending=(sort_order == 'Ascendente'))

# Mostrar datos ordenados
st.subheader(f"Aplicaciones en la categoría: {category}")
st.write(f"Ordenado por {sort_by} en orden {sort_order.lower()}.")
st.dataframe(sorted_data[['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price']])

# Botones interactivos para insights
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

