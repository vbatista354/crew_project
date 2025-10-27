from crewai import Task

def create_recommendations_task(agent, csv_file):
    return Task(
        description=f"""
        Analiza el archivo CSV en la ruta {csv_file} y genera una lista de recomendaciones financieras personalizadas para optimizar los gastos.
        Las recomendaciones deben ser claras, concisas y basadas en patrones identificados en las transacciones (por ejemplo, categorías con gastos altos, transacciones inusuales).
        Usa la herramienta RecommendationTool para generar las recomendaciones.
        La salida debe ser una lista de cadenas, donde cada cadena es una recomendación completa y comprensible.
        Ejemplo de formato: ["Reducir gastos en categoría X (total: Y€).", "Revisar transacciones altas (>Z€)."]
        Asegúrate de que la salida sea una lista de cadenas directamente utilizable.
        """,
        agent=agent,
        expected_output="Una lista de cadenas con recomendaciones financieras personalizadas basadas en el análisis de las transacciones."
    )