import numpy as np
import csv
import funciones

lista_funciones = [
    ("polinomica_simple", funciones.f_poli, 1, 2),
    ("polinomica_doble", funciones.f_doble, 1, 3),
    ("logaritmica", funciones.f_log, 2, 3),
    ("exponencial", funciones.f_exp, 0, 1),
    ("trigonometrica", funciones.f_trig, 0, 1),
    ("mixta", funciones.f_mixta, 0.1, 1)
]

print("Generando archivos CSV con los puntos (x, f(x))")

# aqui se recorrera una por una las funciones de la lista
for nombre, f, a, b in lista_funciones:
    valores_x = np.linspace(a, b, 100)
    
    # ruta donde se guardaran
    ruta_archivo = f"data/{nombre}.csv"
    
    with open(ruta_archivo, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["x", "f(x)"])

        for x in valores_x:
            escritor.writerow([x, f(x)])
            
    print(f"archivo {ruta_archivo} creado")
