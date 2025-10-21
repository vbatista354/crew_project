from crewai import Task

def create_report_task(agent, data):
    return Task(
        description=f"Analiza los datos financieros proporcionados : {data}. Genera un reporte en formato JSON con los campos: total_transacciones, promedio_transaciones y categorias_mas_frecuentes.",
        agent=agent,
        expected_output= "Un objeto JSON con el reporte financiero."
    )