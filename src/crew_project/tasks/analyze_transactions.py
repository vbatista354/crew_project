from crewai import Task

def create_analyze_task(agent, file_path):
    return Task(
        description=f"""Usa la herramienta CSV Data Processor para leer el archivo en: {file_path}.
        Realiza análisis estadístico avanzado:
        1. Monto máximo y mínimo
        2. Transacción más cara (ID y monto)
        3. Alertas: transacciones > 150€
        4. Tendencias por categoría
        5. Recomendaciones de optimización de gasto""",
        agent=agent,
        tools=[agent.tools[0]],  # Usa CsvTool
        expected_output="Reporte de análisis con estadísticas, alertas y recomendaciones en formato legible"
    )