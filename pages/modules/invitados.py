import streamlit as st
import pandas as pd

def mostrar_invitados():
    """Gestión de la página de invitados."""
    st.title("📋 Gestión de Invitados")
    excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
    data_inv = pd.read_excel(excel_url, sheet_name="INVITADOS")
    
    data_inv['Estado'] = data_inv['Confirma'].fillna('Pendiente').replace('', 'Pendiente')
    confirmados = len(data_inv[data_inv['Estado'] == 'Confirmado'])
    pendientes = len(data_inv[data_inv['Estado'] == 'Pendiente'])
    
    st.metric("Total invitados", len(data_inv))
    st.metric("Confirmados", confirmados)
    st.metric("Pendientes", pendientes)
    
    # Mostrar tabla
    st.dataframe(data_inv)
