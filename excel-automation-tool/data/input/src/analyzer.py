def analyze_data(df):
    df["Total"] = df["Cantidad"] * df["Precio"]

    summary = {
        "total_general": df["Total"].sum(),
        "total_por_cliente": df.groupby("Cliente")["Total"].sum()
    }

    return summary
