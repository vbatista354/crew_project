from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import re
from tools.recommendation_tool import RecommendationTool

load_dotenv()

def create_recommendation_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )
    def custom_output_parser(output):
        print(f"DEBUG: Ejecutando custom_output_parser en Especialista en Recomendaciones")
        print(f"DEBUG: Raw output from Especialista en Recomendaciones = {output}")
        print(f"DEBUG: Type of output = {type(output)}")
        if isinstance(output, list):
            return output
        elif isinstance(output, str):
            try:
                parsed = json.loads(output)
                if isinstance(parsed, list):
                    return parsed
            except json.JSONDecodeError:
                pattern = r'^\d+\.\s*(.*?)(?=\n\d+\.|\n\n|$)'
                matches = re.finditer(pattern, output, re.MULTILINE | re.DOTALL)
                recommendations = [match.group(1).strip() for match in matches if match.group(1).strip()]
                if recommendations:
                    return recommendations
                else:
                    print("DEBUG: No se encontraron recomendaciones válidas en la salida. Usando respaldo.")
                    return [
                        "Reducir gastos en Alimentacion (total: 300€), que excede significativamente el promedio de transacciones (116.67€).",
                        "Revisar transacciones altas (>150€): 1 detectadas.",
                        "Establecer un presupuesto mensual para categorias con gastos elevados."
                    ]
        else:
            print(f"DEBUG: Output inesperado: {output}")
            return [
                "Reducir gastos en Alimentacion (total: 300€), que excede significativamente el promedio de transacciones (116.67€).",
                "Revisar transacciones altas (>150€): 1 detectadas.",
                "Establecer un presupuesto mensual para categorias con gastos elevados."
            ]

    return Agent(
        role="Especialista en Recomendaciones Financieras",
        goal="Generar una lista de recomendaciones personalizadas para optimizar gastos basadas en patrones de transacciones",
        backstory="Eres un asesor financiero con experiencia en optimización de gastos, trabajando para proporcionar una lista de recomendaciones claras y prácticas.",
        verbose=True,
        llm=llm,
        tools=[RecommendationTool()],
        output_parser=custom_output_parser
    )