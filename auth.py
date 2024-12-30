import streamlit as st

def run():
    """Pantalla de login."""
    st.title("🔒 Login")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        if username == "admin" and password == "gus2024":
            st.session_state.logged_in = True
            st.session_state.role = "admin"
            st.success("Inicio de sesión exitoso. ¡Bienvenido!")
            st.experimental_rerun()  # Recarga la app para reflejar el estado
        else:
            st.error("Usuario o contraseña incorrectos.")

def logout():
    """Cierra la sesión del usuario."""
    st.session_state.logged_in = False
    st.session_state.role = None
    st.info("Has cerrado sesión correctamente.")
