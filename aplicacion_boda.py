import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from auth import login_user, logout

# Estado inicial
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.role = None

# Configuración del menú principal
menu_items = ["Inicio"]
if st.session_state.login and st.session_state.role == "Administrador":
    menu_items.extend(["Invitados", "Gastos", "Restaurantes"])

if st.session_state.login:
    menu_items.append("Cerrar sesión")  # Añadimos la opción de cerrar sesión al menú

# Barra de navegación
with st.sidebar:
    page = option_menu(
        "Navegación",
        menu_items if st.session_state.login else ["Inicio", "Login"],
        icons=["house", "people", "wallet", "map", "key", "box-arrow-right"],
        menu_icon="cast",
        default_index=0,
    )

# Página de login
if page == "Login":
    login_user()

# Página de inicio (siempre visible)
elif page == "Inicio":
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

# Página de invitados (Solo accesible por administradores)
elif page == "Invitados" and st.session_state.login and st.session_state.role == "Administrador":
    st.title("📋 Gestión de Invitados")
    excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
    data_inv = pd.read_excel(excel_url, sheet_name="INVITADOS")
    data_inv['Estado'] = data_inv['Confirma'].fillna('Pendiente').replace('', 'Pendiente')

    confirmados = len(data_inv[data_inv['Estado'] == 'Confirmado'])
    pendientes = len(data_inv[data_inv['Estado'] == 'Pendiente'])
    st.metric("Total invitados", len(data_inv))
    st.metric("Confirmados", confirmados)
    st.metric("Pendientes", pendientes)
    st.dataframe(data_inv)

# Página de gastos (Solo accesible por administradores)
elif page == "Gastos" and st.session_state.login and st.session_state.role == "Administrador":
    st.title("💰 Gestión de Gastos")
    excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
    data_gastos = pd.read_excel(excel_url, sheet_name="GASTOS")
    st.dataframe(data_gastos)

# Página de restaurantes (Solo accesible por administradores)
elif page == "Restaurantes" and st.session_state.login and st.session_state.role == "Administrador":
    st.title("🍴 Restaurantes")
    excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
    data_restaurantes = pd.read_excel(excel_url, sheet_name="RESTAURANTES")
    st.dataframe(data_restaurantes)

# Página de cerrar sesión
elif page == "Cerrar sesión" and st.session_state.login:
    logout()
    st.experimental_rerun()  # Forzamos la recarga para limpiar la sesión

# Redirigir si intenta acceder sin login
elif not st.session_state.login and page != "Inicio":
    st.warning("🔒 Debes iniciar sesión para acceder a esta sección.")
