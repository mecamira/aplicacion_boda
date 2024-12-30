import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px

import streamlit as st
import pandas as pd
import plotly.express as px

# Usuarios y contraseñas
USERS = {
    "admin": {"password": "gus2024", "role": "Administrador"},
    "invitado": {"password": "invitado", "role": "Invitado"},
}

# Estado de la sesión para login
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.role = None

def login_user(username, password):
    """Verifica credenciales y actualiza el estado de la sesión."""
    if username in USERS and USERS[username]["password"] == password:
        st.session_state.login = True
        st.session_state.role = USERS[username]["role"]
        st.success(f"Bienvenido, {username} ({st.session_state.role})")
    else:
        st.error("Usuario o contraseña incorrectos")

def logout():
    """Cierra la sesión."""
    st.session_state.login = False
    st.session_state.role = None

# Interfaz de login
if not st.session_state.login:
    st.title("🔒 Login")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        login_user(username, password)
else:
    # Mostrar contenido según el rol
    st.sidebar.title("📂 Opciones")
    st.sidebar.button("Cerrar sesión", on_click=logout)

    if st.session_state.role == "Administrador":
        # Contenido para el administrador
        st.title("👩‍💼 Panel de Administración")
        st.write("Contenido privado solo para el Administrador.")

        # Ejemplo: Gestión de gastos
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_gastos = pd.read_excel(excel_url, sheet_name="GASTOS")
        st.markdown("### Gestión de Gastos")
        st.dataframe(data_gastos)

        # Gráfico de gastos
        fig = px.bar(
            data_gastos,
            x="Concepto",
            y=["Prevision", "Gasto Real"],
            title="Gastos Previstos vs Reales",
            barmode="group",
        )
        st.plotly_chart(fig)

    elif st.session_state.role == "Invitado":
        # Contenido para el invitado
        st.title("🎉 Bienvenidos a la Boda")
        st.write("Contenido público para los invitados.")

        # Ejemplo: Lista de invitados
        excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
        data_inv = pd.read_excel(excel_url, sheet_name="INVITADOS")
        st.markdown("### Lista de Invitados Confirmados")
        st.dataframe(data_inv[data_inv["Confirma"] == "Confirmado"])


# Cargar datos desde el Excel
excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
data_inv = pd.read_excel(excel_url, sheet_name="INVITADOS")
data_gastos = pd.read_excel(excel_url, sheet_name="GASTOS")
data_restaurantes = pd.read_excel(excel_url, sheet_name="RESTAURANTES")

# Configuración de la barra de navegación
with st.sidebar:
    page = option_menu(
        "Navegación",
        ["Inicio", "Invitados", "Gastos", "Restaurantes"],
        icons=["house", "people", "wallet", "map"],
        menu_icon="cast",
        default_index=0,
    )

# Página de inicio
if page == "Inicio":
    st.title("🎉 Bienvenidos a la Aplicación de la Boda 💍")
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
    st.image("https://via.placeholder.com/800x400?text=Bienvenidos+a+la+Boda", use_container_width=True)


# Página de invitados
elif page == "Invitados":
    st.title("📋 Gestión de Invitados")
    data_inv['Estado'] = data_inv['Confirma'].fillna('Pendiente').replace('', 'Pendiente')

    # Resumen
    confirmados = len(data_inv[data_inv['Estado'] == 'Confirmado'])
    pendientes = len(data_inv[data_inv['Estado'] == 'Pendiente'])
    st.metric("Total invitados", len(data_inv))
    st.metric("Confirmados", confirmados)
    st.metric("Pendientes", pendientes)

    # Mostrar la tabla completa
    st.dataframe(data_inv)

    # Filtro interactivo
    filtro_estado = st.selectbox("Filtrar por estado", ["Todos", "Confirmado", "Pendiente"])
    if filtro_estado != "Todos":
        st.dataframe(data_inv[data_inv['Estado'] == filtro_estado])

# Página de gastos
elif page == "Gastos":
    st.title("💰 Gestión de Gastos")
    st.dataframe(data_gastos)

    # Gráfico de barras de gastos
    st.markdown("### Comparativa de Previsión vs Gasto Real")
    fig = px.bar(
        data_gastos,
        x="Concepto",
        y=["Prevision", "Gasto Real"],
        title="Gastos Previstos vs Reales",
        barmode="group",
    )
    st.plotly_chart(fig)

# Página de restaurantes
elif page == "Restaurantes":
    st.title("🍴 Restaurantes")
    st.dataframe(data_restaurantes)

    # Mapa interactivo o información detallada
    st.markdown("### Opciones de restaurantes cercanas a Oviedo")
    st.write("Selecciona un restaurante para más detalles en futuras versiones.")
