import streamlit as st

# Usuarios y contraseñas
USERS = {
    "admin": {"password": "gus2024", "role": "Administrador"},
    "invitado": {"password": "invitado", "role": "Invitado"},
}

def login_user():
    """Muestra el formulario de login y gestiona el estado de la sesión."""
    if "login" not in st.session_state:
        st.session_state.login = False
        st.session_state.role = None

    if not st.session_state.login:
        st.title("🔒 Login")
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Iniciar sesión"):
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.login = True
                st.session_state.role = USERS[username]["role"]
                st.success(f"Bienvenido, {username} ({st.session_state.role})")
                st.experimental_rerun()  # Refresca la página automáticamente
            else:
                st.error("Usuario o contraseña incorrectos")
        return False
    else:
        st.sidebar.button("Cerrar sesión", on_click=logout)
        return True

def get_role():
    """Devuelve el rol del usuario logueado."""
    return st.session_state.get("role", None)

def logout():
    """Cierra la sesión del usuario."""
    st.session_state.login = False
    st.session_state.role = None
