from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

def create_data_analyzer():
    llm = ChatOpenAI(
        model= os.getenv("MODEL"),
        api_key= os.getenv("OPENAI_API_KEY")
    )
    return Agent(
        role= "Analista de datos Financieros",
        goal= "Realizar analisis estadistico avanzado de transacciones y detectar patrones/anomalias",
        backstory= "Eres un data scientist especializado en analisis financiero para bancos. Identificas tendencias, anomalias y oportunidades de optimizacion en los patrones de gasto.",
        verbose=True,
        llm= llm
    )