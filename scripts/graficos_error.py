import matplotlib.pyplot as plt
import funciones
import metodos

print("generando grafico de convergencia de errores")

a = 1.0
b = 2.0
x0 = 2.0

# solo necesitamos el cuarto argumento
_, _, _, err_bis = metodos.biseccion(funciones.f_poli, a, b)
_, _, _, err_fp = metodos.falsa_posicion(funciones.f_poli, a, b)
_, _, _, err_sec = metodos.secante(funciones.f_poli, a, b)
_, _, _, err_nr = metodos.newton_raphson(funciones.f_poli, funciones.df_poli, x0)

plt.figure(figsize=(8, 5))

# se dibujan las lineas solo si el método logró avanzar
if len(err_bis) > 0: 
    plt.plot(range(1, len(err_bis) + 1), err_bis, marker='o', label="Biseccion")
if len(err_fp) > 0: 
    plt.plot(range(1, len(err_fp) + 1), err_fp, marker='s', label="Falsa Posicion")
if len(err_sec) > 0: 
    plt.plot(range(1, len(err_sec) + 1), err_sec, marker='^', label="Secante")
if len(err_nr) > 0: 
    plt.plot(range(1, len(err_nr) + 1), err_nr, marker='d', label="Newton-Raphson")

plt.yscale('log')

plt.title("Convergencia: Error vs Iteracion (Escala Log)")
plt.xlabel("Numero de Iteracion")
plt.ylabel("Error Absoluto (log)")
plt.legend()
plt.grid(True, which="both", linestyle="--")

plt.savefig("assets/convergencia_errores.png")
plt.close()

print("Grafico de errores guardado")
