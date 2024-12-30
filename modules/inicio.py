import streamlit as st
from PIL import Image
from datetime import datetime
import pandas as pd
import os

# Aplicar estilo personalizado con fondo
def add_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("assets/eucalyptus_background.png");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def run():
    # Aplicar fondo
    add_background()

    # Encabezado Principal
    st.title("¡Estás invitado a nuestra boda! 💍")

    # Foto e introducción
    try:
        imagen_principal = Image.open("assets/Foto_principal.jpeg")
        st.image(imagen_principal, use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen principal. Asegúrate de que 'assets/Foto_principal.jpeg' exista.")

    st.markdown(
        """
        Esta aplicación está diseñada para ayudarte a disfrutar cada momento de nuestro día especial.
        Explora la información del evento, confirma tu asistencia y comparte tus sugerencias. 🌸
        """
    )

    # Cuenta Atrás
    fecha_boda = datetime(2026, 6, 13, 12, 0, 0)  # Fecha corregida
    dias_restantes = (fecha_boda - datetime.now()).days
    st.subheader(f"¡Faltan {dias_restantes} días para el gran día!")

    # Información del Evento
    st.header("Detalles del Evento")

    # Ceremonia
    st.write("**Ceremonia:**")
    st.write("- **Lugar:** Iglesia San Pedro de los Arcos, Oviedo.")
    st.write("- [Ver en Google Maps](https://www.google.com/maps/place/Iglesia+de+San+Pedro+de+los+Arcos/@43.3672191,-5.8628094,1660m/data=!3m2!1e3!4b1!4m6!3m5!1s0xd368d023a71211f:0x17b0a2a66f4e2e75!8m2!3d43.3672153!4d-5.8579385!16s%2Fg%2F12lnh3l3y?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D)")
    try:
        imagen_iglesia = Image.open("assets/iglesia_san_pedro.jpg")
        st.image(imagen_iglesia, width=400)
    except FileNotFoundError:
        st.error("No se encontró la imagen de la iglesia. Asegúrate de que 'assets/iglesia_san_pedro.jpg' exista.")

    # Banquete
    st.write("**Banquete:**")
    st.write("- **Lugar:** Hotel Reconquista, Oviedo.")
    st.write("- [Ver en Google Maps](https://www.google.com/maps/place/Eurostars+Hotel+de+La+Reconquista/@43.3630968,-5.8564535,830m/data=!3m1!1e3!4m9!3m8!1s0xd368cfd2a506959:0x5204d03f5e4695a3!5m2!4m1!1i2!8m2!3d43.3630929!4d-5.8538786!16s%2Fg%2F11b77b3hsw?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D)")
    try:
        imagen_hotel = Image.open("assets/hotel_reconquista.jpg")
        st.image(imagen_hotel, width=400)
    except FileNotFoundError:
        st.error("No se encontró la imagen del hotel. Asegúrate de que 'assets/hotel_reconquista.jpg' exista.")

    # Confirmación de Asistencia
    st.header("Confirmación de Asistencia")
    with st.expander("Confirmar Asistencia"):
        with st.form(key='confirmacion_asistencia'):
            nombre = st.text_input("Nombre Completo")
            asistencia = st.radio("¿Asistirás al evento?", ("Sí", "No"))
            alergias = st.text_area("Alergias o Preferencias Alimenticias")
            submit_confirmacion = st.form_submit_button("Enviar Confirmación", disabled=True)
            if submit_confirmacion:
                st.info("Por ahora, este formulario está bloqueado.")

    # Mensajes y Sugerencias
    st.header("Mensajes y Sugerencias")
    with st.expander("Enviar Mensaje o Sugerencia"):
        with st.form(key='mensajes_sugerencias'):
            nombre_mensaje = st.text_input("Tu Nombre")
            mensaje = st.text_area("Escribe tu mensaje o sugerencia")
            submit_mensaje = st.form_submit_button("Enviar Mensaje", disabled=True)
            if submit_mensaje:
                st.info("Por ahora, este formulario está bloqueado.")

if __name__ == "__main__":
    run()
