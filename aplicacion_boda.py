import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from auth import login_user, logout

# Estado inicial
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.role = None

# Configuración de la barra de navegación
menu_items = ["Inicio"]
if st.session_state.login and st.session_state.role == "Administrador":
    menu_items.extend(["Invitados", "Gastos", "Restaurantes"])

with st.sidebar:
    page = option_menu(
        "Navegación",
        menu_items,
        icons=["house", "people", "wallet", "map"],
        menu_icon="cast",
        default_index=0,
    )

# Botón de login/logout en la parte superior
with st.container():
    st.markdown("---")
    if st.session_state.login:
        st.button("Cerrar sesión", on_click=logout)
    else:
        st.button("Identificarse", on_click=login_user)
    st.markdown("---")

# Página de inicio (Visible por todos)
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

# Página de invitados (Solo accesible por administradores)
elif page == "Invitados":
    if st.session_state.login and st.session_state.role == "Administrador":
        st.title("📋 Gestión de Invitados")
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_inv = pd.read_excel(excel_url, sheet_name="INVITADOS")
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
    else:
        st.warning("🔒 Acceso denegado. Solo administradores pueden ver esta página.")

# Página de gastos (Solo accesible por administradores)
elif page == "Gastos":
    if st.session_state.login and st.session_state.role == "Administrador":
        st.title("💰 Gestión de Gastos")
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_gastos = pd.read_excel(excel_url, sheet_name="GASTOS")
        st.dataframe(data_gastos)
    else:
        st.warning("🔒 Acceso denegado. Solo administradores pueden ver esta página.")

# Página de restaurantes (Solo accesible por administradores)
elif page == "Restaurantes":
    if st.session_state.login and st.session_state.role == "Administrador":
        st.title("🍴 Restaurantes")
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_restaurantes = pd.read_excel(excel_url, sheet_name="RESTAURANTES")
        st.dataframe(data_restaurantes)
    else:
        st.warning("🔒 Acceso denegado. Solo administradores pueden ver esta página.")
