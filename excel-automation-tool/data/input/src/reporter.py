import pandas as pd

def generate_report(df, summary, output_path):
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Datos Limpios", index=False)

        resumen_df = pd.DataFrame({
            "Cliente": summary["total_por_cliente"].index,
            "Total": summary["total_por_cliente"].values
        })

        resumen_df.to_excel(writer, sheet_name="Resumen", index=False)
