import streamlit as st
from PIL import Image, ImageEnhance
from datetime import datetime
import os
from io import BytesIO
import base64

def prepare_background():
    """
    Carga y suaviza la imagen de fondo, guardándola temporalmente.
    """
    image_path = "assets/eucalyptus_background.jpg"
    background = Image.open(image_path)

    enhancer = ImageEnhance.Brightness(background)
    softened_background = enhancer.enhance(1.1)

    softened_path = "assets/softened_eucalyptus_background.jpg"
    softened_background.save(softened_path)
    return softened_path

def add_custom_styles(background_path):
    """
    Inyecta el fondo + estilos mínimos en la app,
    sin forzar fuentes ni tamaños, salvo en el background y contenedores.
    """
    with open(background_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

        /* Fondo de la aplicación */
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover;
            background-attachment: fixed;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center; 
            color: #000000;
        }}

        /* Separador decorativo */
        .separador {{
            width: 100%;
            height: 2px;
            background-color: #8B4513;
            margin: 1rem 0;
        }}

        /* Imágenes circulares */
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
    # 1. Preparar e inyectar fondo
    softened_background_path = prepare_background()
    add_custom_styles(softened_background_path)

    # 2. Encabezado principal
    st.write("N & A")
    st.write("13 de junio de 2026")
    st.title("¡Bienvenidos a nuestra boda! 💍")

    # 3. Imagen principal (si existe)
    try:
        imagen_principal = Image.open("assets/Foto_principal.jpeg")
        st.image(imagen_principal, use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen principal ('assets/Foto_principal.jpeg').")

    # ==================== BLOQUE 1: Introducción ====================
    st.markdown(
        """
        <div style="
            font-size: 24px; 
            font-family: 'Dancing Script', cursive; 
            color: #000000; 
            text-align: center;
        ">
            ¡Que sí! ¡Que nos casamos! Estamos muy felices de compartir con vosotros 
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

    # ==================== BLOQUE 2: Cuenta atrás ====================
    fecha_boda = datetime(2026, 6, 13, 12, 0, 0)
    dias_restantes = (fecha_boda - datetime.now()).days

    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="
            font-size: 2em; 
            font-family: 'Dancing Script', cursive; 
            color: #8B4513; 
            text-align: center; 
            font-weight: bold;
        ">
            ¡Faltan <span style="font-size: 1.3em;">{dias_restantes}</span> días para el gran día!
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)

    # ==================== Detalles del evento ====================
    st.header("Detalles del Evento")  # Esto usa h2 de Streamlit

    # ------ BLOQUE 3: Ceremonia ------
    st.markdown(
        """
        <div style="
            font-size: 26px; 
            font-family: 'Dancing Script', cursive; 
            color: #000000; 
            text-align: center;
        ">
            <strong>⛪ Ceremonia:</strong><br>
            <strong>Lugar:</strong> Iglesia San Pedro de los Arcos, Oviedo.
            <br>
            <a href="https://www.google.com/maps/place/Iglesia+de+San+Pedro+de+los+Arcos/@43.3672191,-5.8628094,1660m/data=!3m2!1e3!4b1!4m6!3m5!1s0xd368d023a71211f:0x17b0a2a66f4e2e75!8m2!3d43.3672153!4d-5.8579385!16s%2Fg%2F12lnh3l3y?entry=ttu" 
               target="_blank" style="color: #8B4513;">
               Ver en Google Maps
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

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
        st.error("No se encontró la imagen de la iglesia ('assets/iglesia_san_pedro.jpg').")

    # ------ BLOQUE 4: Banquete ------
    st.markdown(
        """
        <div style="
            font-size: 26px; 
            font-family: 'Dancing Script', cursive; 
            color: #000000; 
            text-align: center;
        ">
            <strong>🏰 Banquete:</strong><br>
            <strong>Lugar:</strong> Hotel Reconquista, Oviedo.
            <br>
            <a href="https://www.google.com/maps/place/Eurostars+Hotel+de+La+Reconquista/@43.3630968,-5.8564535,830m/data=!3m1!1e3!4m9!3m8!1s0xd368cfd2a506959:0x5204d03f5e4695a3!5m2!4m1!1i2!8m2!3d43.3630929!4d-5.8538786!16s%2Fg%2F11b77b3hsw?entry=ttu" 
               target="_blank" style="color: #8B4513;">
               Ver en Google Maps
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

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
        st.error("No se encontró la imagen del hotel ('assets/hotel_reconquista.jpg').")

    # ==================== Confirmación de Asistencia ====================
    st.header("Confirmación de Asistencia")
    with st.expander("Confirmar Asistencia"):
        with st.form(key='confirmacion_asistencia'):
            nombre = st.text_input("Nombre Completo")
            asistencia = st.radio("¿Asistirás al evento?", ("Sí", "No"))
            alergias = st.text_area("Alergias o Preferencias Alimenticias")
            submit_confirmacion = st.form_submit_button("Enviar Confirmación", disabled=True)
            if submit_confirmacion:
                st.info("Por ahora, este formulario está bloqueado.")

    # ==================== Mensajes y Sugerencias ====================
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
