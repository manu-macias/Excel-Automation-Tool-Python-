import pandas as pd

REQUIRED_COLUMNS = ["Fecha", "Cliente", "Producto", "Cantidad", "Precio"]

def validate_data(file_path):
    df = pd.read_excel(file_path)
    errors = []

    # Validar columnas obligatorias
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            errors.append({"error": f"Columna faltante: {col}"})

    # Si faltan columnas críticas, cortar
    if errors:
        return None, pd.DataFrame(errors)

    # Convertir tipos
    df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce")
    df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")

    # Filas inválidas
    invalid_rows = df[df[["Cantidad", "Precio"]].isnull().any(axis=1)]

    if not invalid_rows.empty:
        for idx in invalid_rows.index:
            errors.append({"fila": idx + 2, "error": "Cantidad o Precio inválido"})

    return df.drop(invalid_rows.index), pd.DataFrame(errors)
