import pandas as pd
import streamlit as st

# URL del Google Sheet en formato CSV
url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=csv"

# Título de la aplicación
st.title("Gestión de Invitados - Boda N&A 2026")

try:
    # Leer los datos desde la URL
    data = pd.read_csv(url)
    st.write(f"Datos cargados: {data.shape[0]} filas, {data.shape[1]} columnas")
    # Mostrar los datos en Streamlit
    st.dataframe(data)
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")
