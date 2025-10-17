from agents.report_generator import create_report_generator
from task.generate_report import create_report_task
from crewai import Crew
import pandas as pd 

#cargar datos desde el csv 
sample_data = pd.read_csv("data/sample_transaccions.csv").to_dict(orient="records")

#Agente y tarea 
report_agent = create_report_generator()
report_task = create_report_task(report_agent, sample_data)

#crear y ejectuar crew 
crew = Crew(agents=[report_agent], tasks=[report_task], verbose=2)
result = crew.kickoff()

print(result)
