# Laboratorio 2: La raíz que se esconde
**Análisis de convergencia de métodos de búsqueda de raíces**

## preguntas de convergencia

**1. ¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?**

Bueno, al realizar la ejecución de todos los métodos se puede observar que el método Newton-Raphson fue el que tuvo menos iteraciones para converger en las funciones con raíces simples.
Esto se debe a su orden de convergencia cuadrática, ya que la cantidad de decimales correctos de la estimación se duplica en cada iteración, acercándose al cero muy rápido.
Aunque, en el caso de la función polinómica con raíz doble, el método más rápido en converger fue Newton-Raphson mejorado, y esto porque es la mejor para estos casos ya que utiliza la segunda derivada.

**2. ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?**

Los métodos se agrupan de la siguiente forma:
*   **Convergencia lineal:** Bisección, falsa posición y punto fijo
*   **Convergencia superlineal:** Secante (1,618)
*   **Convergencia cuaddrática:** Newton-Raphson y Newton-Raphson mejorado
  
Bueno, esto se puede observar en nuestro gráfico con escala logarítmica, donde la convergencia lineal se ve como una bajada recta y suave. Y la cuadrática, se cae en picada de forma casi vertical, confimando que aplasta el error mucho más rápido.

**3. ¿Qué métodos requieren un intervalo con cambio de signo y cuáles son?**

Los métodos que sí requieren un cambio de signo son los cerrados como la bisección y falsa posición, en cambio los métodos abiertos como el punto fijo, secante y las dos versiones de Newton, no requieren un cambio de signo sino que usan estimaciones iniciales.

**4. En la función que toca el eje x (raiz doble): ¿Qué métodos fallan o no aplican y cuál se comporta mejor?¿Por qué?**

Los métodos que fallan son los cerrados, o sea bisección y falsa posición ya que la curva solo toca el eje X sin cruzarlo, por lo que no hay cambio de signo. Newton-Raphson funciona, pero se vuelve muy lento. El único que es eficiente es el Newton-Raphson mejorado, ya que usa la segunda derivada para mantener la velocidad cuadrática.

**5. ¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?**

Los métodos cerrados que tienen el intervalo inicial, dicen que mientras más estrecho este sea, menos iteraciones tomará llegar a la raíz. Sin embargo, si el intervalo se elige mal y no envuelve un cambio de signo, el método ni siquiera puede empezar a converger.
En cambio los métodos abiertos con estimación inicial, mientras más cercana esté de la raíz más rápido sera la convergencia. En cambio, si la estimación es lejana o cae en una zona donde la curva es horizontal, el método diverge.

**6. ¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?**

Bueno, para robustez y seguridad recomendaría la bisección ya que aunque sea lento, garantiza encontrar la raíz si esta existe en el intervalo. Ahora para máxima velocidad, me iría por Newton-Raphson, por su gran rapidez cuadrática. Luego para funciones con raíces múltiples sin duda Newton-Raphson mejorado, ya que es la única opción viable. Y finalmente si quieres un equilibrio, recomendaría el método de la secante, ya que es casi tan rápido como Newton, pero más robusto en su uso práctico al no exigir el cálculo de derivadas analíticas.

## Conclusión

En conclusión, viendo los gráficos, la Bisección es la mejor opción en cuanto a robustez para ir a la segura, pero Newton gana por lejos en velocidad. Eso sí, darle a un buen intervalo o punto inicial es clave, porque si nos alejamos mucho, aumenta la cantidad de iteraciones o el método simplemente explota (como pasó con el Punto fijo). Por último, la raíz doble me demostró que "tener raíz" (tocar el eje X) no es lo mismo que "cambiar de signo" (cruzarlo), por eso ahí los métodos cerrados fallaron y el único que salvó la situación fue el Newton Mejorado.
