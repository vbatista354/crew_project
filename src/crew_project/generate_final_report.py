import json
import os

def generate_final_report(report_data, analysis_data, recommendations_data, output_dir):
    # Combinar resultados en un reporte JSON
    final_report = {
        "reporte_basico": report_data,
        "analisis_avanzado": analysis_data,
        "recomendaciones": recommendations_data
    }

    # Crear directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "final_report.json")

    # Guardar reporte JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_report, f, indent=4, ensure_ascii=False)

    # Generar reporte de texto legible
    try:
        text_report = (
            "=== Reporte Financiero Consolidado ===\n\n"
            f"1. Reporte Básico:\n"
            f"- Total Transacciones: {report_data.get('total_transacciones', 'N/A')}\n"
            f"- Promedio Transacción: {report_data.get('promedio_transaccion', 'N/A'):.2f}€\n"
            f"- Categorías Más Frecuentes:\n"
        )
        for cat in report_data.get('categorias_mas_frecuentes', []):
            text_report += f"  - {cat.get('categoria', 'N/A')}: {cat.get('conteo', 'N/A')}\n"
    except Exception as e:
        text_report = f"Error al generar el reporte básico: {str(e)}\n"

    text_report += (
        "\n2. Análisis Avanzado:\n"
        f"- Monto Máximo: {analysis_data.get('maximo', 'N/A')}€\n"
        f"- Monto Mínimo: {analysis_data.get('minimo', 'N/A')}€\n"
        f"- Mediana: {analysis_data.get('mediana', 'N/A')}€\n"
        f"- Desviación Estándar: {analysis_data.get('desviacion_estandar', 'N/A'):.2f}€\n"
        f"- Transacción Más Cara: ID {analysis_data.get('transaccion_mas_cara', {}).get('id', 'N/A')}, {analysis_data.get('transaccion_mas_cara', {}).get('monto', 'N/A')}€\n"
        f"- Alertas (>150€):\n"
    )
    for alerta in analysis_data.get('alertas', []):
        text_report += f"  - ID {alerta.get('id', 'N/A')}: {alerta.get('monto', 'N/A')}€\n"
    text_report += f"- Tendencias por Categoría:\n"
    for cat, total in analysis_data.get('tendencias', {}).items():
        text_report += f"  - {cat}: {total}€\n"

    text_report += "\n3. Recomendaciones:\n"
    for i, rec in enumerate(recommendations_data, 1):
        text_report += f"  {i}. {rec}\n"

    text_report_path = os.path.join(output_dir, "final_report.txt")
    with open(text_report_path, 'w', encoding='utf-8') as f:
        f.write(text_report)

    return output_path, text_report_path