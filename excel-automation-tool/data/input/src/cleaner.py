def clean_data(df):
    df["Cliente"] = df["Cliente"].str.strip().str.title()
    df["Producto"] = df["Producto"].str.strip().str.upper()
    df["Fecha"] = df["Fecha"].dt.strftime("%Y-%m-%d")

    return df
