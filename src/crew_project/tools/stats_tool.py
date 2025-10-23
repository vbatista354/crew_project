from crewai_tools import BaseTool
import pandas as pd 
import numpy as np

class StatsTool(BaseTool):
    name : str= "Statical Analysis Tool"
    description : str= "Herrramienta para calcular estadisticas vanzadas (mediana, desviacion estandar ) de un archivo CSV"

    def _run(self,file_path: str) -> dict:
        try:
            df = pd.read_csv(file_path)
            stats = {
                "mediana_monto": float(df["monto"].median()),
                "desviacion_estandar_monto": float(df["monto"].std()),
                "total_por_categoria": df.groupby("categoria") ["monto"].sum().to_dict
            }
            return {
                "status": "success",
                "data": stats
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }