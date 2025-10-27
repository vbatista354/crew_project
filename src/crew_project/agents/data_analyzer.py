from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from tools.csv_tool import CsvTool
from tools.stats_tool import StatsTool

load_dotenv()

def create_data_analyzer():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )
    return Agent(
        role="Analista de datos Financieros",
        goal="Realizar análisis avanzados de datos financieros, incluyendo estadísticas y tendencias",
        backstory="Eres un experto en análisis de datos financieros, especializado en identificar patrones y generar insights a partir de transacciones.",
        verbose=True,
        llm=llm,
        tools=[CsvTool(), StatsTool()]
    )