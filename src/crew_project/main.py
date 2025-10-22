from agents.report_generator import create_report_generator
from agents.data_analyzer import create_data_analyzer
from tasks.generate_report import create_report_task
from tasks.analyze_transactions import create_analyze_task
from tools.csv_tool import CsvTool
from crewai import Crew

# Ruta absoluta al CSV
csv_file = "C:/Users/Victor/crew_project/data/sample_transactions.csv"

# Configurar agentes y herramientas
csv_tool = CsvTool()
report_agent = create_report_generator()
analyzer_agent = create_data_analyzer()

# Asignar herramienta a los agentes
report_agent.tools = [csv_tool]
analyzer_agent.tools = [csv_tool]

# Configurar tareas con la ruta del CSV
report_task = create_report_task(report_agent, csv_file)
analyze_task = create_analyze_task(analyzer_agent, csv_file)

# Crear y ejecutar el Crew
crew = Crew(agents=[report_agent, analyzer_agent], tasks=[report_task, analyze_task], verbose=True)
result = crew.kickoff()

print(result)