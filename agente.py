
import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel

# Cargar variables desde .env
load_dotenv()  # lee .env en la carpeta del proyecto

# Obtener variables
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o-mini")

if not API_KEY:
    raise RuntimeError("No se encontró OPENAI_API_KEY. Añádela al .env o en la variable de entorno.")

# Asegurarnos de que la librería OpenAI vea la clave en el entorno
os.environ["OPENAI_API_KEY"] = API_KEY

# Importar las librerías que necesitan ya la variable de entorno
from langchain_openai import ChatOpenAI
from crewai import Agent, Crew, Task, Process

# Pydantic model (opcional) para validar salida JSON
class Blog(BaseModel):
    title: str
    content: str

# Crear el LLM usando la configuración del .env
llm = ChatOpenAI(model=MODEL)

# Definir el agente (pedimos explícitamente salida en JSON para facilitar parseo)
blog_agent = Agent(
    role="Music",
    goal="Search music content",
    backstory=(
        "You are a music expert who helps find information about classical musicians. "
        "Return the result as JSON: an array of objects with fields 'title' (musician) "
        "and 'content' (short description of their best song)."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Definir la tarea pidiendo JSON estructurado
task1 = Task(
    description=(
        "Give me 3 names of classical musicians and their best songs. "
        "Return a JSON array of up to 3 objects with keys: title, content."
    ),
    expected_output="json",  # informativo; la librería podría ignorarlo dependiendo de versión
    agent=blog_agent
)

# Construir y ejecutar el crew
crew = Crew(agents=[blog_agent], tasks=[task1], process=Process.sequential, verbose=True)
result = crew.kickoff()

# Mostrar resultado crudo
print("\n--- Resultado crudo del agente ---\n")
print(result)

# Intentar parsear como JSON y validar con Pydantic
print("\n--- Intentando parsear JSON ---\n")
try:
    # Si result es str, intentar json.loads, si ya es estructura, usarla
    data = json.loads(result) if isinstance(result, str) else result

    # Si es una lista de objetos
    if isinstance(data, list):
        for i, item in enumerate(data, 1):
            b = Blog.parse_obj(item)
            print(f"\n[{i}] Title: {b.title}\nContent: {b.content}")
    elif isinstance(data, dict):
        b = Blog.parse_obj(data)
        print(f"Title: {b.title}\nContent: {b.content}")
    else:
        print("El resultado no tiene estructura JSON esperada (lista/dict).")
except Exception as e:
    print("No se pudo parsear JSON automáticamente:", str(e))
    print("Revisa el resultado crudo arriba y ajusta la instrucción para forzar salida JSON.")

