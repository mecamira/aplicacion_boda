import streamlit as st
from ..utils.helpers import cargar_datos


def run():
    st.title("📋 Gestión de Invitados")
    data_inv = cargar_datos("INVITADOS")
    data_inv['Estado'] = data_inv['Confirma'].fillna('Pendiente').replace('', 'Pendiente')

    # Resumen
    confirmados = len(data_inv[data_inv['Estado'] == 'Confirmado'])
    pendientes = len(data_inv[data_inv['Estado'] == 'Pendiente'])
    st.metric("Total invitados", len(data_inv))
    st.metric("Confirmados", confirmados)
    st.metric("Pendientes", pendientes)

    # Mostrar la tabla completa
    st.dataframe(data_inv)

    # Filtro interactivo
    filtro_estado = st.selectbox("Filtrar por estado", ["Todos", "Confirmado", "Pendiente"])
    if filtro_estado != "Todos":
        st.dataframe(data_inv[data_inv['Estado'] == filtro_estado])
