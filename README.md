# Laboratorio 2: Búsqueda de Raíces

Este proyecto implementa y compara distintos métodos numéricos para encontrar raíces de funciones (Bisección, Falsa Posición, Punto Fijo, Secante, Newton-Raphson y Newton Mejorado).

## Estructura del Proyecto
* `scripts/metodos.py`: Contiene la lógica matemática de los 6 algoritmos con control de errores.
* `scripts/funciones.py`: Define las 6 funciones de prueba y sus derivadas.
* `scripts/generar_resumen.py`: Script principal que pone a prueba los métodos y genera los datos.
* `scripts/generar_graficos.py`: Dibuja las funciones y marca las raíces encontradas.
* `scripts/graficos_error.py`: Genera los gráficos de convergencia (error vs iteración) en escala logarítmica.
* `data/`: Contiene los archivos CSV con los resultados numéricos.
* `assets/`: Contiene los gráficos PNG generados.
* `informe.md`: Análisis técnico y respuestas a las preguntas de convergencia.

## Entorno y Ejecución (Docker)
Este proyecto utiliza un ambiente controlado mediante Docker, por lo que no es necesario instalar dependencias de Python localmente (como matplotlib o numpy).

Para reproducir los resultados, ejecuta los siguientes comandos en la terminal desde la raíz del proyecto:

1. **Generar los datos CSV:**
   `sudo docker run --rm -v $(pwd):/app busqueda-raices python scripts/generar_resumen.py`

2. **Generar los gráficos de las funciones:**
   `sudo docker run --rm -v $(pwd):/app busqueda-raices python scripts/generar_graficos.py`

3. **Generar los gráficos de convergencia (error vs iteración):**
   `sudo docker run --rm -v $(pwd):/app busqueda-raices python scripts/graficos_error.py`
