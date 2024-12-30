import streamlit as st
from auth import login_user, logout
from pages.inicio import mostrar_inicio
from pages.invitados import mostrar_invitados
from pages.gastos import mostrar_gastos
from pages.restaurantes import mostrar_restaurantes

# Inicializar el estado de sesión
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.role = None

# Configurar las páginas visibles según el estado de sesión
menu_items = ["Inicio"]  # La página "Inicio" siempre será visible
if st.session_state.login and st.session_state.role == "Administrador":
    menu_items.extend(["Invitados", "Gastos", "Restaurantes", "Cerrar sesión"])

if not st.session_state.login:
    menu_items.append("Login")

# Barra de navegación
with st.sidebar:
    page = st.radio("Navegación", menu_items)

# Controlar navegación entre páginas
if page == "Inicio":
    mostrar_inicio()
elif page == "Login":
    login_user()
elif page == "Invitados" and st.session_state.login and st.session_state.role == "Administrador":
    mostrar_invitados()
elif page == "Gastos" and st.session_state.login and st.session_state.role == "Administrador":
    mostrar_gastos()
elif page == "Restaurantes" and st.session_state.login and st.session_state.role == "Administrador":
    mostrar_restaurantes()
elif page == "Cerrar sesión":
    logout()
    st.session_state.login = False
    st.session_state.role = None
    st.sidebar.empty()
    st.success("Has cerrado sesión correctamente.")

