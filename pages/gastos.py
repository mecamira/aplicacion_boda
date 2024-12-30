import streamlit as st
import pandas as pd
import plotly.express as px

def mostrar_gastos():
    """Gestión de la página de gastos."""
    st.title("💰 Gestión de Gastos")
    excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
    data_gastos = pd.read_excel(excel_url, sheet_name="GASTOS")
    
    # Mostrar datos
    st.dataframe(data_gastos)
    
    # Gráfico de barras
    st.markdown("### Comparativa de Previsión vs Gasto Real")
    fig = px.bar(
        data_gastos,
        x="Concepto",
        y=["Prevision", "Gasto Real"],
        title="Gastos Previstos vs Reales",
        barmode="group",
    )
    st.plotly_chart(fig)
