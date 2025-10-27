from crewai import Task

def create_report_task(agent, csv_file):
    return Task(
        description=f"""
        Analiza el archivo CSV en la ruta {csv_file} y genera un reporte financiero básico en formato JSON serializado.
        El reporte debe incluir:
        - total_transacciones: número total de transacciones.
        - promedio_transaccion: promedio de los montos de las transacciones (en euros, redondeado a 2 decimales).
        - categorias_mas_frecuentes: lista de diccionarios con las categorías más frecuentes y su conteo (por ejemplo, [{{"categoria": "Alimentacion", "conteo": 2}}, ...]).
        Usa la herramienta CsvTool para leer el archivo CSV.
        Asegúrate de que la salida sea una cadena JSON válida.
        """,
        agent=agent,
        expected_output="Una cadena JSON serializada que contiene el reporte financiero básico con las claves 'total_transacciones', 'promedio_transaccion' y 'categorias_mas_frecuentes'."
    )