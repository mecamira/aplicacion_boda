import streamlit as st
from PIL import Image, ImageEnhance
from datetime import datetime
import pandas as pd
import os
from io import BytesIO
import base64

# Suavizar la imagen de fondo
def prepare_background():
    image_path = "assets/eucalyptus_background.jpg"
    background = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(background)
    softened_background = enhancer.enhance(1.1)
    softened_path = "assets/softened_eucalyptus_background.jpg"
    softened_background.save(softened_path)
    return softened_path

# Aplicar estilo personalizado con fondo y textos
def add_custom_styles(background_path):
    with open(background_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover;
            background-attachment: fixed;
            font-family: 'Dancing Script', cursive;
        }}
        h1 {{
            color: #000000 !important;
            font-size: 64px;
        }}
        h2 {{
            color: #000000 !important;
            font-size: 48px;
        }}
        .normal-text {{
            font-size: 15px;
            color: #000000;
            text-align: center;
        }}
        .circular-image {{
            display: block;
            margin: 0 auto;
            border-radius: 50%;
            width: 350px;
            height: 350px;
            object-fit: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def run():
    softened_background_path = prepare_background()
    add_custom_styles(softened_background_path)

    # Encabezado Principal
    st.write("N & A")
    st.write("13 de junio de 2026")
    st.title("¡Bienvenidos a nuestra boda! 💍")

    # Foto e introducción
    try:
        imagen_principal = Image.open("assets/Foto_principal.jpeg")
        st.image(imagen_principal, use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen principal. Asegúrate de que 'assets/Foto_principal.jpeg' exista.")

    # Texto de introducción
    st.markdown(
        f"""
        <div class="normal-text">
            ¡Que sí! ¡Que nos casamos! Estamos muy felices de compartir con vosotros cada momento de nuestro día especial. Por eso estamos preparando una boda que será para recordar.
            <br><br>
            Mientras llega el gran día, hemos creado esta app con varias secciones para que estés al día de todo.
            <br><br>
            Una cosa importante. En la sección de Confirmar Asistencia puedes confirmar si asistirás o no, además de compartirnos cualquier mensaje o sugerencia. Confírmanos lo antes posible, por favor, que así organizarlo todo nos será mucho más fácil.
            <br><br>
            Nos vemos pronto 🌸
            <br><br>
            Noemi y Alejandro
        </div>
        """,
        unsafe_allow_html=True
    )

    # Cuenta Atrás
    fecha_boda = datetime(2026, 6, 13, 12, 0, 0)
    dias_restantes = (fecha_boda - datetime.now()).days

    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="color: #8B4513; font-size: 24px; font-weight: bold; text-align: center;">
            ¡Faltan <span style="font-size: 32px;">{dias_restantes}</span> días para el gran día!
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)

    # Información del Evento
    st.header("Detalles del Evento")
    st.markdown(
        f"""
        <div class="normal-text">
            <b>⛪ Ceremonia:</b> Iglesia San Pedro de los Arcos, Oviedo.
            <br>
            <a href="https://www.google.com/maps/place/Iglesia+de+San+Pedro+de+los+Arcos/" target="_blank">Ver en Google Maps</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    try:
        imagen_iglesia = Image.open("assets/iglesia_san_pedro.jpg")
        buffered = BytesIO()
        imagen_iglesia.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(f"""<img src="data:image/jpeg;base64,{img_str}" class="circular-image">""", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen de la iglesia.")

    st.markdown(
        f"""
        <div class="normal-text">
            <b>🏰 Banquete:</b> Hotel Reconquista, Oviedo.
            <br>
            <a href="https://www.google.com/maps/place/Eurostars+Hotel+de+La+Reconquista/" target="_blank">Ver en Google Maps</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    try:
        imagen_hotel = Image.open("assets/hotel_reconquista.jpg")
        buffered = BytesIO()
        imagen_hotel.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(f"""<img src="data:image/jpeg;base64,{img_str}" class="circular-image">""", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen del hotel.")

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
