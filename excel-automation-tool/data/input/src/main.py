import argparse
import logging
import os

from validator import validate_data
from cleaner import clean_data
from analyzer import analyze_data
from reporter import generate_report


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main(input_path, output_path):
    logging.info("Proceso iniciado")

    df, errors = validate_data(input_path)

    if df is None:
        print("❌ Error: el archivo tiene problemas de estructura")
        print(errors)
        errors.to_excel("errores.xlsx", index=False)
        logging.error("Errores de estructura")
        return

    if not errors.empty:
        print("⚠️ Se encontraron errores en los datos (ver errores.xlsx)")
        errors.to_excel("errores.xlsx", index=False)

    clean_df = clean_data(df)
    summary = analyze_data(clean_df)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_report(clean_df, summary, output_path)

    logging.info("Proceso finalizado correctamente")
    print(f"✅ Reporte generado correctamente en: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Excel Automation Tool")

    parser.add_argument(
        "--input",
        required=True,
        help="Ruta del archivo Excel de entrada"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Ruta del archivo Excel de salida"
    )

    args = parser.parse_args()
    main(args.input, args.output)
