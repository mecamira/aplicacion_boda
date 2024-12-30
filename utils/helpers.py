import pandas as pd

def cargar_datos(sheet_name):
    """Carga datos de una hoja específica del Excel."""
    excel_url = "https://docs.google.com/spreadsheets/d/1TjlHkjPvyxZrTy2YR2eUWjHIkSS0fcWg/export?format=xlsx"
    return pd.read_excel(excel_url, sheet_name=sheet_name)
