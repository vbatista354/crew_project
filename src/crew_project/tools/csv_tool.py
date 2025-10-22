from crewai_tools import BaseTool
import pandas as pd 

class CsvTool(BaseTool):
    name : str = "CSV Data Processor"
    description : str = "Herramienta para leer y procesar datos desde un archivo CSV"

    def _run(self,file_path: str) -> dict:
        try:
            data= pd.read_csv(file_path).to_dict(orient="records")
            return {
                "status": "Success",
                "data": data
            }
        except Exception as e:
            return {
                "Status": "error",
                "message": str(e)
            }