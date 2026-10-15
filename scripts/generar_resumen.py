import csv
import metodos
import funciones

# el formato de como se cargan los datos es: Nombre, funcion, primera derivada, segunda derivada, inicio 'a', fin 'b')
lista_pruebas = [
    ("polinomica_simple", funciones.f_poli, funciones.df_poli, funciones.d2f_poli, 1.0, 2.0),
    ("polinomica_doble", funciones.f_doble, funciones.df_doble, funciones.d2f_doble, 1.0, 3.0),
    ("logaritmica", funciones.f_log, funciones.df_log, funciones.d2f_log, 2.0, 3.0),
    ("exponencial", funciones.f_exp, funciones.df_exp, funciones.d2f_exp, 0.0, 1.0),
    ("trigonometrica", funciones.f_trig, funciones.df_trig, funciones.d2f_trig, 0.0, 1.0),
    ("mixta", funciones.f_mixta, funciones.df_mixta, funciones.d2f_mixta, 0.1, 1.0)
]

print("poniendo a prueba los metodos")

# ahora abrimos  el archivo CSV 
with open("data/resumen_convergencia.csv", mode="w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Funcion", "Metodo", "Raiz", "Iteraciones", "Error"])

    for nombre, f, df, d2f, a, b in lista_pruebas:
        
        #  aqui es la prueba de Bisección
        raiz, it, _, hist_err = metodos.biseccion(f, a, b)
        if it > 0:
            error_final = hist_err[-1] if len(hist_err) > 0 else 0
            escritor.writerow([nombre, "Biseccion", raiz, it, error_final])

        # aqui es la prueba de Falsa Posición
        raiz, it, _, hist_err = metodos.falsa_posicion(f, a, b)
        if it > 0:
            error_final = hist_err[-1] if len(hist_err) > 0 else 0
            escritor.writerow([nombre, "Falsa Posicion", raiz, it, error_final])

        # aqui es la prueba de Punto Fijo
        def g(x): return f(x) + x
        raiz, it, _, hist_err = metodos.punto_fijo(g, a)
        if it > 0:
            error_final = hist_err[-1] if len(hist_err) > 0 else 0
            escritor.writerow([nombre, "Punto Fijo", raiz, it, error_final])

        # aqui es la prueba de Secante
        raiz, it, _, hist_err = metodos.secante(f, a, b)
        if it > 0:
            error_final = hist_err[-1] if len(hist_err) > 0 else 0
            escritor.writerow([nombre, "Secante", raiz, it, error_final])

        # aqui es la prueba de Newton-Raphson
        raiz, it, _, hist_err = metodos.newton_raphson(f, df, b)
        if it > 0:
            error_final = hist_err[-1] if len(hist_err) > 0 else 0
            escritor.writerow([nombre, "Newton-Raphson", raiz, it, error_final])

        # aqui es la prueba de Newton-Raphson Mejorado
        raiz, it, _, hist_err = metodos.newton_raphson_mejorado(f, df, d2f, b)
        if it > 0:
            error_final = hist_err[-1] if len(hist_err) > 0 else 0
            escritor.writerow([nombre, "Newton Mejorado", raiz, it, error_final])

print("archivo data/resumen_convergencia.csv creado")
