import streamlit as st
from PIL import Image, ImageEnhance
from datetime import datetime
import os
from io import BytesIO
import base64

def prepare_background():
    image_path = "assets/eucalyptus_background.jpg"
    background = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(background)
    softened_background = enhancer.enhance(1.1)
    softened_path = "assets/softened_eucalyptus_background.jpg"
    softened_background.save(softened_path)
    return softened_path

def add_custom_styles(background_path):
    with open(background_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

        /* Fondo + tipografía y color base para la app */
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
            color: #000000;
        }}

        /* Fuerza a que h1 y h2 también tengan Dancing Script y color negro */
        h1 {{
            font-family: 'Dancing Script', cursive !important;
            font-size: 64px !important;
            color: #000000 !important;
            /* Si quieres forzar estilo "italics" añade:
               font-style: italic !important;
            */
        }}
        h2 {{
            font-family: 'Dancing Script', cursive !important;
            font-size: 48px !important;
            color: #000000 !important;
        }}

        /* El resto (p, label, .stMarkdown) solo fuerza tipografía y color, sin tamaño */
        p, label, .stMarkdown {{
            font-family: 'Dancing Script', cursive;
            color: #000000;
        }}

        /* Inputs de texto / radio */
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
            font-size: 20px;
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
    # Inyectamos fondo y estilos
    softened_background_path = prepare_background()
    add_custom_styles(softened_background_path)

    # Encabezado principal
    st.write("N & A")  # Hereda Dancing Script + color #000
    st.write("13 de junio de 2026")  
    st.title("¡Bienvenidos a nuestra boda! 💍")  # <h1> con Dancing Script

    # Imagen principal
    try:
        imagen_principal = Image.open("assets/Foto_principal.jpeg")
        st.image(imagen_principal, use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen principal ('assets/Foto_principal.jpeg').")

    # BLOQUE 1: Introducción
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

    # BLOQUE 2: Cuenta atrás
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

    # Detalles del evento
    st.header("Detalles del Evento")  # <h2> con Dancing Script

    # Ceremonia
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
            <a href="https://www.google.com/maps/place/Iglesia+de+San+Pedro+de+los+Arcos/@43.3672192,-5.8605134,1660m/data=!3m2!1e3!4b1!4m6!3m5!1s0xd368d023a71211f:0x17b0a2a66f4e2e75!8m2!3d43.3672153!4d-5.8579385!16s%2Fg%2F12lnh3l3y?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D" 
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
        st.error("No se encontró la imagen de la iglesia.")

    # Banquete
    st.markdown(
        """
        <div style="
            font-size: 26px; 
            font-family: 'Dancing Script', cursive; 
            color: #000000; 
            text-align: center;
        ">
            <strong>🏰 Banquete:</strong><br>
            <strong>Lugar:</strong> Palacio de Villabona, Llanera.
            <br>
            <a href="https://www.google.es/maps/place/Palacio+de+Villabona/@43.4622896,-5.8373044,17z/data=!3m1!4b1!4m6!3m5!1s0xd368f3a9c000001:0x95b6e22a5d2bb121!8m2!3d43.4622858!4d-5.8324335!16s%2Fg%2F1218f4ry?hl=es&entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D" 
               target="_blank" style="color: #8B4513;">
               Ver en Google Maps
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    try:
        imagen_hotel = Image.open("assets/palacio_viallabona.jpg")
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
        st.error("No se encontró la imagen del hotel.")

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
