import csv
import matplotlib.pyplot as plt

etiquetas = []
iteraciones = []

with open("data/resumen_convergencia.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        nombre = f"{fila['Funcion']}\n({fila['Metodo']})"
        etiquetas.append(nombre)
        iteraciones.append(int(fila['Iteraciones']))

plt.figure(figsize=(14, 6))
plt.bar(etiquetas, iteraciones, color='steelblue', edgecolor='black')

plt.title("Resumen de Iteraciones por Metodo y Funcion")
plt.ylabel("Numero de Iteraciones")
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("assets/resumen_iteraciones_barras.png")
print("Grafico de barras generado exitosamente con matplotlib.")
