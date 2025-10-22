from crewai import Task

def create_report_task(agent, file_path):
    return Task(
        description=f"""Usa la herramienta CSV Data Processor para leer el archivo en: {file_path}.
        Genera un reporte en formato JSON con:
        - total_transacciones (número total de transacciones)
        - promedio_transaccion (promedio del monto de transacciones)
        - categorias_mas_frecuentes (lista de las 3 categorías más frecuentes con sus conteos)""",
        agent=agent,
        tools=[agent.tools[0]],  # Usa CsvTool
        expected_output="JSON válido con: total_transacciones (int), promedio_transaccion (float), categorias_mas_frecuentes (lista de {categoria: str, conteo: int})"
    )