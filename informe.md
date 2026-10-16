# Laboratorio 2: La raíz que se esconde
**Análisis de convergencia de métodos de búsqueda de raíces**

## preguntas de convergencia

**1. ¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?**
Bueno, al realizar la ejecución de todos los métodos se puede observar que el método Newton-Raphson fue el que tuvo menos iteraciones para converger en las funciones con raices simples.
Esto se debe a su orden de convergencia cuadrática, ya que la cantidad de decimales correctos de la estimación se duplica en cada iteración, acercándose al cero muy rápido.
Aunque, en el caso de la función polinómica con raíz doble, el método más rápido en converger fue Newton-Raphson mejorado, y esto porque es la mejor para estos casos ya que utiliza la segunda derivada.

**2. ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?**
los métodos se agrupan de la siguiente forma:
*   **Convergencia lineal:** Bisección, falsa posición, y punto fijo
*   **Convergencia superlineal:** Secante (1,618)
*   **Convergencia cuaddrática:** Newton-Raphson y Newton-Raphson mejorado
Bueno, esto se puede observar en nuestro gráfico con escala logaritmica, donde la convergencia lineal se ve como una bajada recta y suave. Y la cuadrática, se cae en picada de forma casi vertical, confimando que aplasta el error mucho más rápido.

**3. ¿Qué métodos requieren un intervalo con cambio de signo y cuáles son?**
los métodos que sí requieren un cambio de signo son los cerrados como la bisección y falsa posición, en cambio los métodos abiertos como el punto fijo, secante y las dos versiones de Newton, no requieren un cambio de signo sino que usan estimaciones iniciales.



