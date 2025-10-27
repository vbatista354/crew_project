from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import json
from tools.csv_tool import CsvTool

load_dotenv()

def create_report_generator():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )
    def custom_output_parser(output):
        print(f"DEBUG: Ejecutando custom_output_parser en Generador de Reportes")
        print(f"DEBUG: Raw output from Generador de Reportes = {output}")
        print(f"DEBUG: Type of output = {type(output)}")
        if isinstance(output, dict):
            return json.dumps(output, ensure_ascii=False)
        elif isinstance(output, str):
            try:
                parsed = json.loads(output)
                return json.dumps(parsed, ensure_ascii=False)
            except json.JSONDecodeError:
                print(f"DEBUG: Output no es una cadena JSON válida: {output}")
                return json.dumps({
                    "total_transacciones": 0,
                    "promedio_transaccion": 0.0,
                    "categorias_mas_frecuentes": []
                }, ensure_ascii=False)
        else:
            print(f"DEBUG: Output inesperado: {output}")
            return json.dumps({
                "total_transacciones": 0,
                "promedio_transaccion": 0.0,
                "categorias_mas_frecuentes": []
            }, ensure_ascii=False)

    return Agent(
        role="Generador de Reportes",
        goal="Crear reportes financieros claros y estructurados a partir de datos de transacciones en formato JSON serializado",
        backstory="Eres un analista financiero experto que trabaja para un banco español como BBVA. Tu tarea es generar reportes en formato JSON basados en datos de transacciones, asegurándote de que la salida sea una cadena JSON válida.",
        verbose=True,
        llm=llm,
        tools=[CsvTool()],
        output_parser=custom_output_parser
    )
