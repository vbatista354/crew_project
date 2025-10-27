import json
import os
from crewai import Crew
from agents.report_generator import create_report_generator
from agents.data_analyzer import create_data_analyzer
from agents.recommendation_agent import create_recommendation_agent
from tasks.generate_report import create_report_task
from tasks.analyze_transactions import create_analyze_task
from tasks.generate_recommendations import create_recommendations_task
from tools.csv_tool import CsvTool
from tools.stats_tool import StatsTool
from tools.recommendation_tool import RecommendationTool
from generate_plot import generate_category_plot
from generate_final_report import generate_final_report

# Rutas absolutas
CSV_FILE = "C:/Users/Victor/crew_project/data/sample_transactions.csv"
OUTPUT_DIR = "C:/Users/Victor/crew_project/data/reports"

def main():
    # Configurar agentes y herramientas
    csv_tool = CsvTool()
    stats_tool = StatsTool()
    recommendation_tool = RecommendationTool()
    
    report_agent = create_report_generator()
    analyzer_agent = create_data_analyzer()
    recommendation_agent = create_recommendation_agent()

    # Asignar herramientas a los agentes
    report_agent.tools = [csv_tool]
    analyzer_agent.tools = [csv_tool, stats_tool]
    recommendation_agent.tools = [recommendation_tool]

    # Configurar tareas
    report_task = create_report_task(report_agent, CSV_FILE)
    analyze_task = create_analyze_task(analyzer_agent, CSV_FILE)
    recommendations_task = create_recommendations_task(recommendation_agent, CSV_FILE)

    # Crear y ejecutar el Crew
    crew = Crew(
        agents=[report_agent, analyzer_agent, recommendation_agent],
        tasks=[report_task, analyze_task, recommendations_task],
        verbose=True
    )
    
    try:
        # Ejecutar las tareas
        result = crew.kickoff()
        
        # Depuración para desarrollo (se puede eliminar en producción)
        print(f"DEBUG: Full result = {result}")
        print(f"DEBUG: Type of result = {type(result)}")
        print(f"DEBUG: result.tasks_output = {result.tasks_output}")
        print(f"DEBUG: report_task output = {result.tasks_output[0].raw}")  # Reporte básico
        print(f"DEBUG: analyze_task output = {result.tasks_output[1].raw}")  # Análisis avanzado
        print(f"DEBUG: recommendations_task output = {result.tasks_output[2].raw}")  # Recomendaciones

        # Procesar la salida del reporte básico (result.tasks_output[0].raw)
        report_data = result.tasks_output[0].raw
        if isinstance(report_data, str):
            try:
                report_data = json.loads(report_data)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error: La salida del Generador de Reportes no es una cadena JSON válida: {report_data}") from e
        if not isinstance(report_data, dict) or 'total_transacciones' not in report_data:
            raise ValueError(f"Error: La salida del Generador de Reportes no tiene el formato esperado: {report_data}")

        # Procesar la salida del análisis avanzado (result.tasks_output[1].raw)
        analysis_data = result.tasks_output[1].raw
        if isinstance(analysis_data, str):
            try:
                # Eliminar marcas de código JSON si están presentes
                analysis_data = analysis_data.replace('```json\n', '').replace('\n```', '')
                analysis_data = json.loads(analysis_data)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error: La salida del Analista de Datos no es una cadena JSON válida: {analysis_data}") from e
        if not isinstance(analysis_data, dict) or 'maximo' not in analysis_data:
            raise ValueError(f"Error: La salida del Analista de Datos no tiene el formato esperado: {analysis_data}")

        # Procesar la salida de recomendaciones (result.tasks_output[2].raw)
        recommendations_data = result.tasks_output[2].raw
        if not isinstance(recommendations_data, list):
            if isinstance(recommendations_data, str):
                try:
                    recommendations_data = json.loads(recommendations_data)
                    if not isinstance(recommendations_data, list):
                        raise ValueError(f"Error: La salida de Recomendaciones no es una lista: {recommendations_data}")
                except json.JSONDecodeError:
                    # Intentar extraer recomendaciones si es texto plano
                    import re
                    pattern = r'^\d+\.\s*(.*?)(?=\n\d+\.|\n\n|$)'
                    matches = re.finditer(pattern, recommendations_data, re.MULTILINE | re.DOTALL)
                    recommendations_data = [match.group(1).strip() for match in matches if match.group(1).strip()]
                    if not recommendations_data:
                        raise ValueError(f"Error: No se pudieron extraer recomendaciones válidas: {recommendations_data}")
            else:
                raise ValueError(f"Error: La salida de Recomendaciones no es una lista ni una cadena válida: {recommendations_data}")

        # Generar gráfico
        plot_path = generate_category_plot(CSV_FILE)
        print(f"Gráfico generado y guardado en: {plot_path}")

        # Generar reporte final
        json_path, text_path = generate_final_report(report_data, analysis_data, recommendations_data, OUTPUT_DIR)
        print(f"Reporte final JSON guardado en: {json_path}")
        print(f"Reporte final de texto guardado en: {text_path}")

    except Exception as e:
        print(f"Error durante la ejecución del Crew: {str(e)}")
        raise

if __name__ == "__main__":
    main()