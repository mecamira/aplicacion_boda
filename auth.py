import streamlit as st

# Usuarios y contraseñas
USERS = {
    "admin": {"password": "gus2024", "role": "Administrador"},
    "invitado": {"password": "invitado", "role": "Invitado"},
}

def login_user():
    """Gestiona el formulario de login y actualiza el estado de la sesión."""
    if "login" not in st.session_state:
        st.session_state.login = False
        st.session_state.role = None
        st.session_state.username = None  # Identifica al usuario logueado

    # Si ya está logueado, no mostrar el formulario de login
    if st.session_state.login:
        st.sidebar.button("Cerrar sesión", on_click=logout)
        return True

    # Formulario de login
    st.title("🔒 Login")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Verificar credenciales al hacer clic
    if st.button("Iniciar sesión"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.login = True
            st.session_state.role = USERS[username]["role"]
            st.session_state.username = username
            st.success(f"Bienvenido, {username} ({st.session_state.role})")
            return True
        else:
            st.error("Usuario o contraseña incorrectos")
    return False

def get_role():
    """Devuelve el rol del usuario logueado."""
    return st.session_state.get("role", None)

def logout():
    """Cierra la sesión del usuario."""
    st.session_state.login = False
    st.session_state.role = None
    st.session_state.username = None
