from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def create_report_generator():
    llm = ChatOpenAI(
        model=os.getenv("MODEL"),
        api_key=os.getenv("OPENAI_API_KEY")
    )
    return Agent(
        role="Generador de Reportes",
        goal="Crear reportes financieros claros y estructurados a partir de datos de transacciones",
        backstory="Eres un analista financiero experto que trabaja para un banco español como BBVA. Tu tarea es generar reportes en formato JSON basados en datos de transacciones.",
        verbose=True,
        llm=llm
    )