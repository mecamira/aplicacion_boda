import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Boda de Alejandro y [Nombre de tu pareja]",
    layout="wide"
)

def run():
    # Cargar la imagen subida
    try:
        imagen_principal = Image.open("assets/Foto_principal.jpeg")
    except FileNotFoundError:
        st.error("La imagen no se encuentra en la ruta especificada. Asegúrate de que 'assets/Foto_principal.jpeg' exista.")

    # Mostrar el banner con la imagen principal
    if 'imagen_principal' in locals():
        st.image(imagen_principal, use_column_width=True)

    # Sección de bienvenida
    st.markdown(
        """
        <style>
            .titulo {
                font-size: 3rem;
                font-weight: bold;
                color: #5A189A;
                text-align: center;
                margin-top: 20px;
            }
            .subtitulo {
                font-size: 1.5rem;
                text-align: center;
                margin-top: 10px;
                color: #5A189A;
            }
        </style>
        <div class="titulo">¡Bienvenidos a Nuestra Boda!</div>
        <div class="subtitulo">Organiza y disfruta cada detalle de este día tan especial 💍</div>
        """,
        unsafe_allow_html=True
    )

    # Dividir la pantalla en columnas
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            """
            ### ¿Qué puedes hacer aquí?
            - **Gestionar invitados**: Confirma asistencias, verifica alérgenos y detalles.
            - **Control de gastos**: Visualiza el presupuesto y gastos reales.
            - **Explora restaurantes**: Elige el lugar perfecto para celebrar.

            ---

            ¡Todo en un solo lugar para que este día sea inolvidable! 🎊
            """
        )

    # Accesos rápidos
    st.markdown(
        """
        <style>
            .boton {
                display: inline-block;
                padding: 15px 25px;
                font-size: 16px;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
                outline: none;
                color: #fff;
                background-color: #5A189A;
                border: none;
                border-radius: 15px;
                box-shadow: 0 9px #999;
                margin: 10px;
            }

            .boton:hover {background-color: #7B2CBF}

            .boton:active {
                background-color: #7B2CBF;
                box-shadow: 0 5px #666;
                transform: translateY(4px);
            }

            .botones {
                text-align: center;
                margin-top: 30px;
            }
        </style>
        <div class="botones">
            <a href="#" class="boton">Gestión de Invitados</a>
            <a href="#" class="boton">Gestión de Gastos</a>
            <a href="#" class="boton">Explorar Restaurantes</a>
        </div>
        """,
        unsafe_allow_html=True
    )
