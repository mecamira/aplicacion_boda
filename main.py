import streamlit as st
from streamlit_option_menu import option_menu

# Estado de sesión para el login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# Configuración del menú dinámico
if st.session_state.logged_in:
    menu_options = ["Inicio", "Invitados", "Gastos", "Restaurantes", "Cerrar sesión"]
    icons = ["house", "people", "wallet", "map", "box-arrow-right"]
else:
    menu_options = ["Inicio", "Login"]
    icons = ["house", "key"]

# Renderizar el menú
with st.sidebar:
    selected_page = option_menu(
        "Navegación",
        menu_options,
        icons=icons,
        menu_icon="menu-app-fill",
        default_index=0,
    )

# Lógica para las páginas
if selected_page == "Inicio":
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

elif selected_page == "Login" and not st.session_state.logged_in:
    st.title("🔒 Login")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username == "admin" and password == "gus2024":
            st.session_state.logged_in = True
            st.session_state.role = "admin"
            st.success("Inicio de sesión exitoso. ¡Bienvenido!")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos.")

elif selected_page == "Cerrar sesión" and st.session_state.logged_in:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.success("Has cerrado sesión correctamente.")
    st.experimental_rerun()

elif st.session_state.logged_in:
    if selected_page == "Invitados" and st.session_state.role == "admin":
        st.experimental_set_query_params(page="invitados")
    elif selected_page == "Gastos" and st.session_state.role == "admin":
        st.experimental_set_query_params(page="gastos")
    elif selected_page == "Restaurantes" and st.session_state.role == "admin":
        st.experimental_set_query_params(page="restaurantes")
