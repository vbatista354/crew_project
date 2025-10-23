import pandas as pd 
import matplotlib.pyplot as plt 

def generate_category_plot(csv_file): 
    df = pd.read_csv(csv_file)  #leer csv 
    totals = df.groupby("categoria") ["monto"].sum()
    plt.figure(figsize=(8,6))
    totals.plot(kind='bar', color=['#1f77b4', '#ff7f0e'])
    plt.title('Totales por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Monto Total (€)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    output_path = csv_file.replace('.csv', '_plot.png') #guardar grafico 
    plt.savefig(output_path)
    plt.close()
    return output_path
