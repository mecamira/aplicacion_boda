import streamlit as st
from utils.helpers import cargar_datos

def run():
    st.title("🍴 Restaurantes")
    data_restaurantes = cargar_datos("RESTAURANTES")

    # Mostrar la tabla completa
    st.dataframe(data_restaurantes)

    # Información adicional o futura funcionalidad
    st.markdown("### Opciones de restaurantes cercanas a Oviedo")
    st.write("Selecciona un restaurante para más detalles en futuras versiones.")
