from crewai import Task

def create_analyze_task(agent, csv_file):
    return Task(
        description=f"""
        Realiza un análisis avanzado de las transacciones en el archivo CSV ubicado en {csv_file}.
        El análisis debe incluir:
        - maximo: el monto más alto de una transacción (en euros).
        - minimo: el monto más bajo de una transacción (en euros).
        - mediana: la mediana de los montos de las transacciones (en euros).
        - desviacion_estandar: la desviación estándar de los montos (en euros, redondeada a 2 decimales).
        - transaccion_mas_cara: un diccionario con el ID y monto de la transacción más cara.
        - alertas: una lista de diccionarios con las transacciones que superan los 150€ (con ID y monto).
        - tendencias: un diccionario con el total gastado por categoría (en euros).
        Usa las herramientas CsvTool y StatsTool para procesar los datos.
        Asegúrate de que la salida sea una cadena JSON válida.
        """,
        agent=agent,
        expected_output="Una cadena JSON serializada que contiene el análisis avanzado con las claves 'maximo', 'minimo', 'mediana', 'desviacion_estandar', 'transaccion_mas_cara', 'alertas' y 'tendencias'.",
        output_parser=None  # El agente maneja la salida directamente
    )