# pages/inicio.py
import streamlit as st

def mostrar_inicio():
    """Página principal de la aplicación."""
    st.title("🎉 Inicio - Bienvenidos a la Aplicación de la Boda 💍")
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
    st.image("https://via.placeholder.com/800x400?text=Inicio+-+Bienvenidos+a+la+Boda", use_container_width=True)

