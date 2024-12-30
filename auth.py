import streamlit as st

# Usuarios y contraseñas
USERS = {
    "admin": {"password": "gus2024", "role": "Administrador"},
}

def login_user():
    """Gestión del login de usuarios."""
    st.title("🔒 Login")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.login = True
            st.session_state.role = USERS[username]["role"]
            st.success(f"Bienvenido, {username} ({st.session_state.role})")
        else:
            st.error("Usuario o contraseña incorrectos.")

def logout():
    """Gestión del cierre de sesión."""
    st.session_state.login = False
    st.session_state.role = None
    st.sidebar.empty()
    st.success("Has cerrado sesión correctamente.")
