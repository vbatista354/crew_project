**Proyecto de Análisis Financiero con CrewAI**

Descripción
-----------
Este proyecto utiliza `crewai` y `langchain` para analizar transacciones financieras desde un archivo CSV (`sample_transactions.csv`) y generar reportes automatizados para aplicaciones bancarias. Incluye tres agentes inteligentes:
- **Generador de Reportes**: Crea un reporte básico con el total de transacciones, promedio de montos y categorías más frecuentes.
- **Analista de Datos Financieros**: Realiza un análisis avanzado (máximo, mínimo, mediana, desviación estándar, transacción más cara, alertas para transacciones >150€, tendencias por categoría).
- **Especialista en Recomendaciones Financieras**: Genera recomendaciones para optimizar gastos basadas en patrones de transacciones.

Salidas:
- `final_report.json`: Reporte consolidado en formato JSON.
- `final_report.txt`: Reporte consolidado en formato de texto.
- `sample_transactions_plot.png`: Gráfico de barras de gastos por categoría.

Requisitos
----------
- Python 3.10+
- Dependencias (instalar con `pip install -r requirements.txt`):
  crewai==0.51.1
  crewai-tools==0.12.1
  chromadb==0.4.24
  pypdf==4.3.1
  tiktoken==0.7.0
  langchain==0.2.17
  langchain-openai==0.1.25
  pydantic==2.12.3
  matplotlib==3.8.4
  pandas==2.3.3
  numpy==2.3.3
  openpyxl==3.1.5
  python-dotenv==1.1.1

Instalación
-----------
1. Clona el repositorio:
   git clone https://github.com/vbatista354/crew_project.git
   cd crew_project
2. Crea un entorno virtual e instala las dependencias:
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # En Windows
   pip install -r requirements.txt
3. Crea un archivo `.env` en la raíz del proyecto con:
   OPENAI_API_KEY=tu_clave_aqui
   MODEL=gpt-4o-mini

Ejecución
---------
1. Asegúrate de que `data/sample_transactions.csv` esté presente con el formato:
   id,monto,categoria
   1,100,Alimentacion
   2,50,Transporte
   3,200,Alimentacion
2. Ejecuta el script principal:
   python src\crew_project\main.py
3. Salidas generadas:
   - data/reports/final_report.json
   - data/reports/final_report.txt
   - data/sample_transactions_plot.png


Ejemplos de Salidas
-------------------
final_report.json
{
    "reporte_basico": {
        "total_transacciones": 3,
        "promedio_transaccion": 116.67,
        "categorias_mas_frecuentes": [
            {"categoria": "Alimentacion", "conteo": 2},
            {"categoria": "Transporte", "conteo": 1}
        ]
    },
    "analisis_avanzado": {
        "maximo": 200,
        "minimo": 50,
        "mediana": 100.0,
        "desviacion_estandar": 76.38,
        "transaccion_mas_cara": {"id": 3, "monto": 200},
        "alertas": [{"id": 3, "monto": 200}],
        "tendencias": {"Alimentacion": 300, "Transporte": 50}
    },
    "recomendaciones": [
        "Reducir gastos en Alimentacion (total: 300€), que excede significativamente el promedio de transacciones ( 116.67€).",
        "Revisar transacciones altas (>150€): 1 detectadas.",
        "Establecer un presupuesto mensual para categorias con gastos elevados."
    ]
}

final_report.txt
=== Reporte Financiero Consolidado ===

1. Reporte Básico:
- Total Transacciones: 3
- Promedio Transacción: 116.67€
- Categorías Más Frecuentes:
  - Alimentacion: 2
  - Transporte: 1

2. Análisis Avanzado:
- Monto Máximo: 200€
- Monto Mínimo: 50€
- Mediana: 100.0€
- Desviación Estándar: 76.38€
- Transacción Más Cara: ID 3, 200€
- Alertas (>150€):
  - ID 3: 200€
- Tendencias por Categoría:
  - Alimentacion: 300€
  - Transporte: 50€

3. Recomendaciones:
  1. Reducir gastos en Alimentacion (total: 300€), que excede significativamente el promedio de transacciones ( 116.67€).
  2. Revisar transacciones altas (>150€): 1 detectadas.
  3. Establecer un presupuesto mensual para categorias con gastos elevados.

sample_transactions_plot.png
Gráfico de barras mostrando gastos por categoría:
- Alimentacion: 300€
- Transporte: 50€
(Ubicado en `data/sample_transactions_plot.png`.)

Notas
-----
- Advertencias de `Pydantic` y `pkg_resources` no afectan la ejecución con las versiones actuales.
- Para usar un CSV diferente, actualiza `data/sample_transactions.csv` y ejecuta `main.py`.

Autor
-----

Victor Batista Mañon

