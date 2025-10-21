from crewai import Task

def create_analyze_task(agent,data):
    return Task(
        description= f"""Realiza analisis estadistico avanzado de estas transacciones:
        {data}.
        
        Calcula y reporta:
        1. Monto maximo y minimo
        2. Transaccion mas cara (ID y monto)
        3. Alertas: transacciones > 150€
        4. Tendencias por categoria
        5. Recomendaciones de optimizacion de gasto""",
        agent= agent,
        expected_output= "Reporte de analisis con estadisticas, alertas y recomendaciones en formato legible"
    )