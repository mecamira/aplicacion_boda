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
        return True

    # Formulario de login
    with st.form("login_form"):
        st.title("🔒 Login")
        username = st.text_input("Usuario", key="username_input")
        password = st.text_input("Contraseña", type="password", key="password_input")
        submit_button = st.form_submit_button("Iniciar sesión")

        if submit_button:
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.login = True
                st.session_state.role = USERS[username]["role"]
                st.session_state.username = username
                st.success(f"Bienvenido, {username} ({st.session_state.role})")
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
