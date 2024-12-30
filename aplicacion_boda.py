import pandas as pd
import streamlit as st
import plotly.express as px

# URL del Google Sheet en formato CSV
url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=csv"

# Título de la aplicación
st.markdown("# Gestión de Invitados - Boda Noe y Alejandro 💍")
st.write("Bienvenidos a la aplicación para gestionar los invitados de la boda. Aquí podrás ver el estado de las confirmaciones, filtrar por categorías y visualizar gráficos interactivos.")

try:
    # Leer los datos desde la URL
    data = pd.read_csv(url)

    # Añadir columnas calculadas (por ejemplo: estado de confirmación)
    data['Estado'] = data['Confirma'].fillna('Pendiente').replace('', 'Pendiente')

    # Mostrar métricas principales
    confirmados = len(data[data['Estado'] == 'Confirmado'])
    pendientes = len(data[data['Estado'] == 'Pendiente'])
    total = len(data)

    st.markdown("## Resumen")
    st.metric("Total de invitados", total)
    st.metric("Confirmados", confirmados)
    st.metric("Pendientes", pendientes)

    # Filtro interactivo por estado
    st.markdown("## Filtrar invitados por estado")
    filtro_estado = st.selectbox("Selecciona el estado", ["Todos", "Confirmado", "Pendiente"])
    if filtro_estado != "Todos":
        data_filtrada = data[data['Estado'] == filtro_estado]
    else:
        data_filtrada = data

    st.dataframe(data_filtrada)

    # Gráfico interactivo
    st.markdown("## Visualización de confirmaciones")
    fig = px.bar(data, x="Estado", title="Confirmaciones por estado", color="Estado", text_auto=True)
    st.plotly_chart(fig)

except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

