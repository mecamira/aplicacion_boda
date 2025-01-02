import streamlit as st

def get_users():
    """Obtiene los usuarios y contraseñas desde los secretos."""
    return st.secrets["USERS"]

def login_user():
    """Gestiona el formulario de login y actualiza el estado de la sesión."""
    if "login" not in st.session_state:
        st.session_state.login = False
        st.session_state.role = None
        st.session_state.username = None  # Identifica al usuario logueado

    # Si ya está logueado, no mostrar el formulario de login
    if st.session_state.login:
        return True

    # Leer los usuarios desde los secretos
    users = get_users()

    # Formulario de login
    st.title("🔒 Login")
    username = st.text_input("Usuario", key="username_input")
    password = st.text_input("Contraseña", type="password", key="password_input")

    if st.button("Iniciar sesión"):
        if username in users and users[username]["password"] == password:
            st.session_state.login = True
            st.session_state.role = users[username]["role"]
            st.session_state.username = username
        else:
            st.error("Usuario o contraseña incorrectos")
    return st.session_state.login

def get_role():
    """Devuelve el rol del usuario logueado."""
    return st.session_state.get("role", None)

def logout():
    """Cierra la sesión del usuario."""
    st.session_state.login = False
    st.session_state.role = None
    st.session_state.username = None
