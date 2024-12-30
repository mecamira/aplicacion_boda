import streamlit as st
import plotly.express as px
from utils.helpers import cargar_datos

def run():
    st.title("💰 Gestión de Gastos")
    data_gastos = cargar_datos("GASTOS")

    # Mostrar la tabla completa
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
