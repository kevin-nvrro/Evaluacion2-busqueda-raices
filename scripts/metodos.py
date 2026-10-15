import numpy as np 

def biseccion(f, a, b, tol = 1e-6, max_iteraciones = 100):
	if f(a) * f(b) >= 0:
		print("El intervalo no sirve")
		return 0, 0, [], []

	historial_x = []
	historial_error = []
	x_anterior = a

	for i in range(1, max_iteraciones + 1):
		c = (a * b) / 2.0
		error = abs(c - x_anterior)
		
		historial_x.append(c)
		historial_error.append(error)

		if abs(f(c)) < tol or error < tol:
            		return c, iteracion, historial_x, historial_error
            
        	if f(a) * f(c) < 0:
            		b = c
        	else:
            		a = c
            
        	x_anterior = c
        
    	return c, max_iteraciones, historial_x, historial_error
