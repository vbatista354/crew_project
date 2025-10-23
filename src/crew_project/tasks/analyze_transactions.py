from crewai import Task

def create_analyze_task(agent, file_path):
    return Task(
        description=f"""Usa la herramienta CSV Data Processor para leer los datos brutos del archivo en: {file_path}.
        Usa la herramienta Statistical Analysis Tool para calcular estadísticas avanzadas (mediana, desviación estándar, totales por categoría).
        NO delegues tareas a otros agentes. Realiza el análisis completo:
        1. Monto máximo, mínimo (usa CSV Data Processor para obtener los datos brutos)
        2. Transacción más cara (ID y monto, usa CSV Data Processor)
        3. Alertas: transacciones > 150€ (usa CSV Data Processor)
        4. Tendencias por categoría (usa totales por categoría de Statistical Analysis Tool)
        5. Recomendaciones de optimización de gasto basadas en las estadísticas""",
        agent=agent,
        tools=[agent.tools[0], agent.tools[1]],  # Usa CsvTool y StatsTool
        expected_output="Reporte de análisis con estadísticas (máximo, mínimo, mediana, desviación estándar), alertas, tendencias (totales por categoría) y recomendaciones en formato legible"
    )