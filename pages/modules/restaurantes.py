import streamlit as st
import pandas as pd

def mostrar_restaurantes():
    """Gestión de la página de restaurantes."""
    st.title("🍴 Restaurantes")
    excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
    data_restaurantes = pd.read_excel(excel_url, sheet_name="RESTAURANTES")
    
    # Mostrar datos
    st.dataframe(data_restaurantes)
    
    # Información adicional o mapa (en el futuro)
    st.markdown("### Opciones de restaurantes cercanas a Oviedo")
    st.write("Selecciona un restaurante para más detalles en futuras versiones.")
