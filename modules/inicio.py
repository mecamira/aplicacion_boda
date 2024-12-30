import streamlit as st
from PIL import Image
from datetime import datetime
import pandas as pd
import os

def run():
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
    st.write("**Fecha y Hora:** 13 de junio, 12:00 PM")
    st.write("**Ceremonia:**")
    st.write("- **Lugar:** Iglesia San Pedro de los Arcos, Oviedo.")
    st.write("- [Ver en Google Maps](https://www.google.com/maps/place/Iglesia+de+San+Pedro+de+los+Arcos)")
    try:
        imagen_iglesia = Image.open("assets/iglesia_san_pedro.jpg")
        st.image(imagen_iglesia, use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen de la iglesia. Asegúrate de que 'assets/iglesia_san_pedro.jpg' exista.")
    try:
        imagen_hotel = Image.open("assets/hotel_reconquista.jpg")
        st.image(imagen_hotel, use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen del hotel. Asegúrate de que 'assets/hotel_reconquista.jpg' exista.")
    st.write("**Banquete:**")
    st.write("- **Lugar:** Hotel Reconquista, Oviedo (pendiente de confirmación).")

    # Confirmación de Asistencia
    st.header("Confirmación de Asistencia")
    st.warning("Este formulario aún no está disponible.")
    with st.form(key='confirmacion_asistencia'):
        nombre = st.text_input("Nombre Completo")
        asistencia = st.radio("¿Asistirás al evento?", ("Sí", "No"))
        alergias = st.text_area("Alergias o Preferencias Alimenticias")
        submit_confirmacion = st.form_submit_button("Enviar Confirmación")
        if submit_confirmacion:
            st.info("Por ahora, este formulario está bloqueado.")

    # Mensajes y Sugerencias
    st.header("Mensajes y Sugerencias")
    st.warning("Este formulario aún no está disponible.")
    with st.form(key='mensajes_sugerencias'):
        nombre_mensaje = st.text_input("Tu Nombre")
        mensaje = st.text_area("Escribe tu mensaje o sugerencia")
        submit_mensaje = st.form_submit_button("Enviar Mensaje")
        if submit_mensaje:
            st.info("Por ahora, este formulario está bloqueado.")

if __name__ == "__main__":
    run()
