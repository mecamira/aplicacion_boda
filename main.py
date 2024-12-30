import streamlit as st
from utils.helpers import load_page
import auth  # Importa las funciones de autenticación

# Configuración de la página debe ser la primera instrucción
st.set_page_config(
    page_title="Boda de Alejandro y [Nombre de tu pareja]",
    layout="wide"
)

# Estado de sesión para el login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# Configuración del menú dinámico
if st.session_state.logged_in:
    menu_options = ["Inicio", "Invitados", "Gastos", "Restaurantes", "Cerrar sesión"]
else:
    menu_options = ["Inicio", "Login"]

# Renderizar el menú
selected_page = st.sidebar.radio("Navegación", menu_options)

# Lógica para las páginas
if selected_page == "Inicio":
    load_page("modules.inicio")

elif selected_page == "Login" and not st.session_state.logged_in:
    load_page("auth")  # Cambiamos "modules.login" por "auth"

elif selected_page == "Cerrar sesión" and st.session_state.logged_in:
    auth.logout()

elif st.session_state.logged_in:
    if selected_page == "Invitados" and st.session_state.role == "admin":
        load_page("modules.invitados")
    elif selected_page == "Gastos" and st.session_state.role == "admin":
        load_page("modules.gastos")
    elif selected_page == "Restaurantes" and st.session_state.role == "admin":
        load_page("modules.restaurantes")
