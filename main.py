import streamlit as st
from auth import login_user, logout
from pages.inicio import mostrar_inicio
from pages.invitados import mostrar_invitados
from pages.gastos import mostrar_gastos
from pages.restaurantes import mostrar_restaurantes

if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.role = None

menu_items = ["Inicio"]
if st.session_state.login and st.session_state.role == "Administrador":
    menu_items.extend(["Invitados", "Gastos", "Restaurantes"])
if st.session_state.login:
    menu_items.append("Cerrar sesión")

with st.sidebar:
    page = st.radio("Navegación", menu_items if st.session_state.login else ["Inicio", "Login"])

if page == "Login":
    login_user()
elif page == "Inicio":
    mostrar_inicio()
elif page == "Invitados" and st.session_state.login and st.session_state.role == "Administrador":
    mostrar_invitados()
elif page == "Gastos" and st.session_state.login and st.session_state.role == "Administrador":
    mostrar_gastos()
elif page == "Restaurantes" and st.session_state.login and st.session_state.role == "Administrador":
    mostrar_restaurantes()
elif page == "Cerrar sesión":
    logout()
