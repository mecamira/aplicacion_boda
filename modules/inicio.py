import streamlit as st
from PIL import Image, ImageEnhance
from datetime import datetime
import pandas as pd
import os
from io import BytesIO
import base64

st.write("VERSIÓN: PRUEBA DE HOY")


# Suavizar la imagen de fondo
def prepare_background():
    # Cargar la imagen
    image_path = "assets/eucalyptus_background.jpg"
    background = Image.open(image_path)

    # Reducir la opacidad
    enhancer = ImageEnhance.Brightness(background)
    softened_background = enhancer.enhance(1.1)
    
    # Guardar la imagen modificada
    softened_path = "assets/softened_eucalyptus_background.jpg"
    softened_background.save(softened_path)
    return softened_path

# Aplicar estilo personalizado con fondo y textos
def add_custom_styles(background_path):
    # Leer la imagen y convertirla a base64
    with open(background_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()

    # Aplicar el fondo y estilos con Google Fonts
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

        /* Fondo de la app con imagen y tipografía base */
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover;
            background-attachment: fixed;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
            font-family: 'Dancing Script', cursive;
        }}

        /* Encabezados, con un tamaño de letra definido */
        h1 {{
            color: #000000 !important;
            font-family: 'Dancing Script', cursive;
            font-size: 64px;
        }}
        h2 {{
            color: #000000 !important;
            font-family: 'Dancing Script', cursive;
            font-size: 48px;
        }}

        /* Eliminar tamaño forzado en p, label y .stMarkdown, manteniendo color y fuente */
        p, label, .stMarkdown {{
            color: #000000;
            font-family: 'Dancing Script', cursive;
            /* font-size: 24px;  <-- COMENTADO/ELIMINADO PARA NO INTERFERIR */
        }}

        /* Inputs de texto */
        .stTextInput > div > div > input {{
            background-color: white;
            border: 1px solid #ccc;
            color: #000000;
            font-family: 'Dancing Script', cursive;
        }}
        .stTextArea > div > textarea {{
            background-color: white;
            border: 1px solid #ccc;
            color: #000000;
            font-family: 'Dancing Script', cursive;
        }}
        .stRadio > div {{
            color: #000000;
            font-family: 'Dancing Script', cursive;
        }}

        /* Botones */
        .stButton > button {{
            background-color: #5A9;
            color: white;
            border-radius: 8px;
            border: none;
            font-family: 'Dancing Script', cursive;
            font-size: 20px;
        }}
        .stButton > button:disabled {{
            background-color: #ccc;
            color: #666;
            font-family: 'Dancing Script', cursive;
        }}

        /* Expander - Quitado el font-size forzado */
        .stExpander {{
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            color: #000000;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            font-family: 'Dancing Script', cursive;
            /* font-size: 24px;  <-- COMENTADO/ELIMINADO PARA EVITAR CONFLICTOS */
        }}

        .separador {{
            width: 100%;
            height: 2px;
            background-color: #8B4513;
            margin: 8px 0;
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
    # Preparar el fondo suavizado
    softened_background_path = prepare_background()

    # Aplicar fondo y estilos personalizados
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

    # BLOQUE 1: Introducción
    st.markdown(
        f"""
        <div style="font-size: 50px; /* Estilo particular de este bloque */
                    font-family: 'Dancing Script', cursive; 
                    color: #000000; text-align: center;">
            ¡Qu sí! ¡Que nos casamos! Estamos muy felices de compartir con vosotros 
            cada momento de nuestro día especial. Por eso estamos preparando una boda 
            que será para recordar.
            <br><br>
            Mientras llega el gran día, hemos creado esta app con varias secciones 
            para que estés al día de todo.
            <br><br>
            Una cosa importante. En la sección de Confirmar Asistencia puedes confirmar 
            si asistirás o no, además de compartirnos cualquier mensaje o sugerencia. 
            Confírmanos lo antes posible, por favor, que así organizarlo todo nos será mucho más fácil.
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

    # Separador superior
    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)

    # BLOQUE 2: Cuenta atrás con estilo individual
    st.markdown(
        f"""
        <div style="color: #8B4513; font-size: 2em; font-weight: bold; text-align: center;">
            ¡Faltan <span style="font-size: 2em;">{dias_restantes}</span> días para el gran día!
        </div>
        """,
        unsafe_allow_html=True
    )

    # Separador inferior
    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)

    # Información del Evento
    st.header("Detalles del Evento")

    # BLOQUE 3: Ceremonia (con estilo propio)
    st.markdown(
        """
        <div style="font-size: 24px; color: #000000; text-align: center;">
            <strong>⛪ Ceremonia:</strong><br>
            <strong>Lugar:</strong> Iglesia San Pedro de los Arcos, Oviedo.
            <br>
            <a href="https://www.google.com/maps/place/Iglesia+de+San+Pedro+de+los+Arcos/@43.3672191,-5.8628094,1660m/data=!3m2!1e3!4b1!4m6!3m5!1s0xd368d023a71211f:0x17b0a2a66f4e2e75!8m2!3d43.3672153!4d-5.8579385!16s%2Fg%2F12lnh3l3y?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D" 
               target="_blank" style="color: #8B4513;">
               Ver en Google Maps
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Imagen de la Iglesia
    try:
        imagen_iglesia = Image.open("assets/iglesia_san_pedro.jpg")
        buffered = BytesIO()
        imagen_iglesia.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(
            f"""
            <img src="data:image/jpeg;base64,{img_str}" class="circular-image">
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("No se encontró la imagen de la iglesia. Asegúrate de que 'assets/iglesia_san_pedro.jpg' exista.")

    # BLOQUE 4: Banquete (con estilo propio)
    st.markdown(
        """
        <div style="font-size: 24px; color: #000000; text-align: center;">
            <strong>🏰 Banquete:</strong><br>
            <strong>Lugar:</strong> Hotel Reconquista, Oviedo.
            <br>
            <a href="https://www.google.com/maps/place/Eurostars+Hotel+de+La+Reconquista/@43.3630968,-5.8564535,830m/data=!3m1!1e3!4m9!3m8!1s0xd368cfd2a506959:0x5204d03f5e4695a3!5m2!4m1!1i2!8m2!3d43.3630929!4d-5.8538786!16s%2Fg%2F11b77b3hsw?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D" 
               target="_blank" style="color: #8B4513;">
               Ver en Google Maps
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Imagen del Hotel
    try:
        imagen_hotel = Image.open("assets/hotel_reconquista.jpg")
        buffered = BytesIO()
        imagen_hotel.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(
            f"""
            <img src="data:image/jpeg;base64,{img_str}" class="circular-image">
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("No se encontró la imagen del hotel. Asegúrate de que 'assets/hotel_reconquista.jpg' exista.")

    # Confirmación de Asistencia (form en un expander)
    st.header("Confirmación de Asistencia")
    with st.expander("Confirmar Asistencia"):
        with st.form(key='confirmacion_asistencia'):
            nombre = st.text_input("Nombre Completo")
            asistencia = st.radio("¿Asistirás al evento?", ("Sí", "No"))
            alergias = st.text_area("Alergias o Preferencias Alimenticias")
            submit_confirmacion = st.form_submit_button("Enviar Confirmación", disabled=True)
            if submit_confirmacion:
                st.info("Por ahora, este formulario está bloqueado.")

    # Mensajes y Sugerencias (form en otro expander)
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
