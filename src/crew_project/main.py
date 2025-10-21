from agents.report_generator import create_report_generator
from agents.data_analyzer import create_data_analyzer
from tasks.generate_report import create_report_task
from tasks.analyze_transactions import create_analyze_task
from crewai import Crew
import pandas as pd

# Cargar datos de ejemplo desde un CSV 
sample_data = pd.read_csv("C:/Users/Victor/crew_project/data/sample_transactions.csv").to_dict(orient="records")

#Configurar agentes y tareas 
report_agent = create_report_generator()
analyzer_agent = create_data_analyzer()
report_task = create_report_task(report_agent, sample_data)
analyze_task = create_analyze_task(analyzer_agent,sample_data)

#Crear y ejecutar el Crew 
crew = Crew(agents=[report_agent, analyzer_agent], tasks=[report_task, analyze_task], verbose=True)
result = crew.kickoff()

print(result)