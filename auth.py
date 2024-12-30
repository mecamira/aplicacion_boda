import streamlit as st

# Usuarios y contraseñas
USERS = {
    "admin": {"password": "gus2024", "role": "Administrador"},
}

def login_user():
    """Muestra el formulario de login y actualiza el estado de sesión."""
    if "login" not in st.session_state:
        st.session_state.login = False
        st.session_state.role = None

    # Si no está logeado, mostrar el formulario de login
    if not st.session_state.login:
        with st.form("login_form"):
            st.write("🔒 **Identificarse**")
            username = st.text_input("Usuario", key="username_input")
            password = st.text_input("Contraseña", type="password", key="password_input")
            login_clicked = st.form_submit_button("Iniciar sesión")

            if login_clicked:
                if username in USERS and USERS[username]["password"] == password:
                    st.session_state.login = True
                    st.session_state.role = USERS[username]["role"]
                    st.experimental_set_query_params(logged_in="1")
                    st.success(f"Bienvenido, {username} ({st.session_state.role})")
                else:
                    st.error("Usuario o contraseña incorrectos")

def logout():
    """Cierra la sesión del usuario."""
    st.session_state.login = False
    st.session_state.role = None
    st.experimental_set_query_params(logged_in="0")
    st.info("Sesión cerrada con éxito")
