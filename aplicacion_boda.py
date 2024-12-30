import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from auth import login_user, get_role

# Verificar si el usuario está logueado
if login_user():
    role = get_role()

    # Configuración de la barra de navegación
    with st.sidebar:
        page = option_menu(
            "Navegación",
            ["Inicio", "Invitados", "Gastos", "Restaurantes"],
            icons=["house", "people", "wallet", "map"],
            menu_icon="cast",
            default_index=0,
        )

    # Página de inicio
    if page == "Inicio":
        st.title("🎉 Bienvenidos a la Aplicación de la Boda 💍")
        st.markdown(
            """
            Esta aplicación ha sido creada para gestionar de manera eficiente todos los detalles de nuestra boda. 
            Explora las diferentes secciones para:
            - **Gestión de invitados**: Confirmar asistencia, verificar alérgenos y regalos.
            - **Gastos**: Analizar y controlar el presupuesto.
            - **Restaurantes**: Evaluar opciones de lugares para la celebración.
            
            ¡Esperamos que disfrutes esta experiencia tanto como nosotros al prepararla! 🎊
            """
        )
        st.image("https://via.placeholder.com/800x400?text=Bienvenidos+a+la+Boda", use_container_width=True)

    # Página de invitados (Solo para Invitados y Administradores)
    elif page == "Invitados" and role in ["Administrador"]:
        st.title("📋 Gestión de Invitados")
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_inv = pd.read_excel(excel_url, sheet_name="INVITADOS")
        data_inv['Estado'] = data_inv['Confirma'].fillna('Pendiente').replace('', 'Pendiente')

        # Mostrar métricas y tabla
        st.metric("Total invitados", len(data_inv))
        st.metric("Confirmados", len(data_inv[data_inv['Estado'] == 'Confirmado']))
        st.dataframe(data_inv)

    # Página de gastos (Solo para Administradores)
    elif page == "Gastos" and role == "Administrador":
        st.title("💰 Gestión de Gastos")
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_gastos = pd.read_excel(excel_url, sheet_name="GASTOS")
        st.dataframe(data_gastos)

        # Gráfico
        fig = px.bar(data_gastos, x="Concepto", y=["Prevision", "Gasto Real"], barmode="group")
        st.plotly_chart(fig)

    # Página de restaurantes (Solo para Administradores)
    elif page == "Restaurantes" and role == "Administrador":
        st.title("🍴 Restaurantes")
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_restaurantes = pd.read_excel(excel_url, sheet_name="RESTAURANTES")
        st.dataframe(data_restaurantes)
    else:
        st.warning("No tienes acceso a esta página.")
