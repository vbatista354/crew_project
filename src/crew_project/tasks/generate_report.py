from crewai import Task

def create_report_task(agent, data):
    return Task(
        description=f"""Analiza los datos financieros proporcionados: {data}.
        Genera un reporte en formato JSON con los campos:
        - total_transacciones (número total de transacciones)
        - promedio_transaccion (promedio del monto de transacciones)
        - categorias_mas_frecuentes (lista de las 3 categorías más frecuentes con sus conteos)""",
        agent=agent,
        expected_output="JSON válido con: total_transacciones (int), promedio_transaccion (float), categorias_mas_frecuentes (lista de {categoria: str, conteo: int})"
    )
