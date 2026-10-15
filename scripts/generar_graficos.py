import numpy as np
import matplotlib.pyplot as plt
import funciones
import metodos

# funciones a graficar
lista_graficos = [
    ("polinomica_simple", funciones.f_poli, 1.0, 2.0),
    ("polinomica_doble", funciones.f_doble, 0.0, 4.0), 
    ("logaritmica", funciones.f_log, 1.0, 4.0),
    ("exponencial", funciones.f_exp, -1.0, 2.0),
    ("trigonometrica", funciones.f_trig, -1.0, 2.0),
    ("mixta", funciones.f_mixta, 0.1, 2.0)
]

print("generando graficos")

for nombre, f, a, b in lista_graficos:
    x_vals = np.linspace(a, b, 200)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=f"Funcion {nombre}", color="blue")
    
    plt.axhline(0, color="black", linewidth=1.2, linestyle="--")
    
    if nombre == "polinomica_doble":
        raiz, it, _, _ = metodos.newton_raphson_mejorado(funciones.f_doble, funciones.df_doble, funciones.d2f_doble, 1.0)
    else:
        raiz, it, _, _ = metodos.biseccion(f, a, b)
        
    # si se ecnuentra una raiz se marca con un punto rojo
    if it > 0 and raiz != 0:
        plt.scatter([raiz], [0], color="red", zorder=5, label=f"Raiz en x={raiz:.4f}")

    plt.title(f"Grafico de funcion: {nombre}")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.legend()
    plt.grid(True)
    
    plt.savefig(f"assets/{nombre}_funcion.png")
    plt.close()

print("Graficos de funciones generados")
