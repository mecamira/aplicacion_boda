import streamlit as st
from PIL import Image, ImageEnhance
from datetime import datetime
import os
from io import BytesIO
import base64

# 1. Función para suavizar la imagen de fondo
def prepare_background():
    image_path = "assets/eucalyptus_background.jpg"
    background = Image.open(image_path)

    # Ajustar brillo para que quede suave
    enhancer = ImageEnhance.Brightness(background)
    softened_background = enhancer.enhance(1.1)

    # Guardar la imagen modificada
    softened_path = "assets/softened_eucalyptus_background.jpg"
    softened_background.save(softened_path)
    return softened_path

# 2. Función para inyectar CSS global (fuente, color, fondo, etc.)
def add_custom_styles(background_path):
    # Convertir imagen de fondo a base64
    with open(background_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()

    # Inyectar estilos
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

        /* Fondo + tipografía y color base */
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover;
            background-attachment: fixed;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
            /* Tipografía y color base para toda la app */
            font-family: 'Dancing Script', cursive;
            color: #000000; 
        }}

        /* Opcional: puedes dejar h1, h2 con tamaño grande si quieres destacar títulos */
        h1 {{
            font-family: 'Dancing Script', cursive;
            font-size: 64px;
            color: #000000;
        }}
        h2 {{
            font-family: 'Dancing Script', cursive;
            font-size: 48px;
            color: #000000;
        }}

        /* No forzamos tamaño en p, label ni .stMarkdown para que no entren en conflicto
           y así cada bloque puede usar su propio inline style si lo desea. */
        p, label, .stMarkdown {{
            font-family: 'Dancing Script', cursive;
            color: #000000;
        }}

        /* Inputs de texto / radio / etc., con la misma fuente y color */
        .stTextInput > div > div > input,
        .stTextArea > div > textarea,
        .stRadio > div {{
            font-family: 'Dancing Script', cursive;
            color: #000000;
        }}

        /* Botones */
        .stButton > button {{
            background-color: #5A9;
            color: white;
            border-radius: 8px;
            border: none;
            font-family: 'Dancing Script', cursive;
            font-size: 20px; /* Ajusta si quieres */
        }}
        .stButton > button:disabled {{
            background-color: #ccc;
            color: #666;
            font-family: 'Dancing Script', cursive;
        }}

        /* Expander */
        .stExpander {{
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            color: #000000;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            font-family: 'Dancing Script', cursive;
        }}

        /* Separador decorativo */
        .separador {{
            width: 100%;
            height: 2px;
            background-color: #8B4513;
            margin: 1rem 0;
        }}

        /* Imágenes circulares (iglesia, hotel, etc.) */
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

# 3. Función principal de la página
def run():
    # Preparar el fondo suavizado
    softened_background_path = prepare_background()
    # Inyectar estilos globales
    add_custom_styles(softened_background_path)

    # Encabezado principal (texto fijo)
    st.write("N & A")                      # Hereda estilo base (Dancing Script, color #000)
    st.write("13 de junio de 2026")        # Lo mismo
    st.title("¡Bienvenidos a nuestra boda! 💍")  # Usa h1 con font-size 64px

    # Foto principal
    try:
        imagen_principal = Image.open("assets/Foto_principal.jpeg")
        st.image(imagen_principal, use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen principal en 'assets/Foto_principal.jpeg'.")

    # BLOQUE 1: Introducción
    # - Aquí, en vez de inline styles, dejamos que herede la fuente y color base.
    # - Si quieres un tamaño concreto, lo pones: style="font-size: 24px;" por ejemplo.
    st.markdown(
        """
        <div style="font-size: 24px; text-align: center;">
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

    # Cuenta atrás
    fecha_boda = datetime(2026, 6, 13, 12, 0, 0)
    dias_restantes = (fecha_boda - datetime.now()).days

    # Separador decorativo
    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)

    # BLOQUE 2: Cuenta atrás (ejemplo de estilo inline distinto)
    st.markdown(
        f"""
        <div style="color: #8B4513; font-size: 2em; font-weight: bold; text-align: center;">
            ¡Faltan <span style="font-size: 2em;">{dias_restantes}</span> días para el gran día!
        </div>
        """,
        unsafe_allow_html=True
    )

    # Otro separador
    st.markdown('<div class="separador"></div>', unsafe_allow_html=True)

    # Información del evento
    st.header("Detalles del Evento")  # Usa h2 con font-size 48px

    # BLOQUE 3: Ceremonia
    st.markdown(
        """
        <div style="font-size: 26px; text-align: center;">
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
    # Imagen iglesia
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
        st.error("No se encontró la imagen de la iglesia. Verifica 'assets/iglesia_san_pedro.jpg'.")

    # BLOQUE 4: Banquete
    st.markdown(
        """
        <div style="font-size: 26px; text-align: center;">
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
    # Imagen hotel
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
        st.error("No se encontró la imagen del hotel. Verifica 'assets/hotel_reconquista.jpg'.")

    # Confirmación de asistencia
    st.header("Confirmación de Asistencia")
    with st.expander("Confirmar Asistencia"):
        with st.form(key='confirmacion_asistencia'):
            nombre = st.text_input("Nombre Completo")
            asistencia = st.radio("¿Asistirás al evento?", ("Sí", "No"))
            alergias = st.text_area("Alergias o Preferencias Alimenticias")
            submit_confirmacion = st.form_submit_button("Enviar Confirmación", disabled=True)
            if submit_confirmacion:
                st.info("Por ahora, este formulario está bloqueado.")

    # Mensajes y sugerencias
    st.header("Mensajes y Sugerencias")
    with st.expander("Enviar Mensaje o Sugerencia"):
        with st.form(key='mensajes_sugerencias'):
            nombre_mensaje = st.text_input("Tu Nombre")
            mensaje = st.text_area("Escribe tu mensaje o sugerencia")
            submit_mensaje = st.form_submit_button("Enviar Mensaje", disabled=True)
            if submit_mensaje:
                st.info("Por ahora, este formulario está bloqueado.")

# Llamada principal (si se ejecuta este script directamente)
if __name__ == "__main__":
    run()
