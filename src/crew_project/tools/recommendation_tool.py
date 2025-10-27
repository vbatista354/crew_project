from crewai_tools import BaseTool
import pandas as pd 

class RecommendationTool(BaseTool):
    name: str= "Recommendation Tool"
    description: str= "Genera recomendaciones de optimizacion de gasto basadas en estadisticas de transacciones "

    def _run(self,file_path:str) -> dict:
        try:
            df = pd.read_csv(file_path)
            total_por_categoria = df.groupby('categoria') ['monto'].sum()
            max_monto = df['monto'].max()
            avg_monto = df['monto'].mean()
            recommendations = []

            #Recomendacion 1 : categoria con mayor gasto 
            max_categoria = total_por_categoria.idxmax()
            max_gasto = total_por_categoria.max()
            if max_gasto > avg_monto * 1.5:
                recommendations.append(
                    f"Reducir gastos en {max_categoria} (total: {max_gasto}€), que excede significativamente el promedio de transacciones ({avg_monto: .2f}€)."
                )

            #Recomendacion 2 : Transacciones altas 
            high_transactions = df[df['monto'] > 150]
            if not high_transactions.empty:
                recommendations.append(
                    f"Revisar transacciones altas (>150€): {len(high_transactions)} detectadas."
                )

            #Recomendacion 3 : Presupuesto 
            recommendations.append(
                "Establecer un presupuesto mensual para categorias con gastos elevados."
            )

            return {
                "status": "success",
                "data": recommendations
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }        

