import matplotlib.pyplot as plt
import funciones
import metodos

print("Generando graficos de convergencia de errores")

#aqui esta la lista con todas las funciones, derivadas y sus intervalos
lista_pruebas = [
    ("polinomica_simple", funciones.f_poli, funciones.df_poli, funciones.d2f_poli, 1.0, 2.0),
    ("polinomica_doble", funciones.f_doble, funciones.df_doble, funciones.d2f_doble, 1.0, 3.0),
    ("logaritmica", funciones.f_log, funciones.df_log, funciones.d2f_log, 2.0, 3.0),
    ("exponencial", funciones.f_exp, funciones.df_exp, funciones.d2f_exp, 0.0, 1.0),
    ("trigonometrica", funciones.f_trig, funciones.df_trig, funciones.d2f_trig, 0.0, 1.0),
    ("mixta", funciones.f_mixta, funciones.df_mixta, funciones.d2f_mixta, 0.1, 1.0)
]

for nombre, f, df, d2f, a, b in lista_pruebas:
    plt.figure(figsize=(8, 5))

    _, _, _, err_bis = metodos.biseccion(f, a, b)
    _, _, _, err_fp = metodos.falsa_posicion(f, a, b)
    
    # aqui hacemos la adaptación para punto fijo
    def g(x): return f(x) + x
    _, it_pf, _, err_pf = metodos.punto_fijo(g, b)
    
    _, _, _, err_sec = metodos.secante(f, a, b)
    _, _, _, err_nr = metodos.newton_raphson(f, df, b)
    _, _, _, err_nrm = metodos.newton_raphson_mejorado(f, df, d2f, b)

    # aquí solo dibujamos la línea si el método funcionó y devolvió errores
    if len(err_bis) > 0: plt.plot(range(1, len(err_bis) + 1), err_bis, marker='o', label="Biseccion")
    if len(err_fp) > 0: plt.plot(range(1, len(err_fp) + 1), err_fp, marker='s', label="Falsa Posicion")
    if it_pf > 0 and len(err_pf) > 0 and err_pf[-1] < 100: 
        plt.plot(range(1, len(err_pf) + 1), err_pf, marker='x', label="Punto Fijo")
    if len(err_sec) > 0: plt.plot(range(1, len(err_sec) + 1), err_sec, marker='^', label="Secante")
    if len(err_nr) > 0: plt.plot(range(1, len(err_nr) + 1), err_nr, marker='d', label="Newton-Raphson")
    if len(err_nrm) > 0: plt.plot(range(1, len(err_nrm) + 1), err_nrm, marker='*', label="Newton Mejorado")

    plt.yscale('log')
    plt.title(f"Convergencia: Error vs Iteracion - {nombre}")
    plt.xlabel("Numero de Iteracion")
    plt.ylabel("Error Absoluto (log)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--")

    plt.savefig(f"assets/{nombre}_convergencia_errores.png")
    plt.close()

print("Graficos de errores actualizados y guardados")
