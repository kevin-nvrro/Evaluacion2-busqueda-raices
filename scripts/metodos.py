import numpy as np 

def biseccion(f, a, b, tol = 1e-6, max_iteraciones = 100):
    if f(a) * f(b) >= 0:
        print("El intervalo no sirve")
        return 0, 0, [], []

    historial_x = []
    historial_error = []
    x_anterior = a

    for i in range(1, max_iteraciones + 1):
        c = (a + b) / 2.0
        error = abs(c - x_anterior)
        
        historial_x.append(c)
        historial_error.append(error)

        if abs(f(c)) < tol or error < tol:
            return c, i, historial_x, historial_error
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
        x_anterior = c
        
    return c, max_iteraciones, historial_x, historial_error

def falsa_posicion(f, a, b, tol = 1e-6, max_iteraciones = 100):
    if f(a) * f(b) >= 0:
        print("El intervalo no sirve")
        return 0, 0, [], []
    
    historial_x = []
    historial_error = []
    x_anterior = a
    
    for i in range(1, max_iteraciones + 1):
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        error = abs(c - x_anterior)
        historial_x.append(c)
        historial_error.append(error)
        
        if abs(f(c)) < tol or error < tol:
            return c, i, historial_x, historial_error
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
        x_anterior = c
        
    return c, max_iteraciones, historial_x, historial_error

def punto_fijo(g, x0, tol=1e-6, max_iteraciones=100):
    historial_x = []
    historial_error = []
    x_anterior = x0
    
    for i in range(1, max_iteraciones + 1):
        if abs(x_anterior) > 100000:
            print("los numeros crecieron muy rápido, el metodo falló")
            return 0, 0, [], []
            
        x_actual = g(x_anterior)
        error = abs(x_actual - x_anterior)
        
        historial_x.append(x_actual)
        historial_error.append(error)
        
        if error < tol:
            return x_actual, i, historial_x, historial_error
            
        x_anterior = x_actual
        
    print("el método no alcanzó la tolerancia")
    return x_actual, max_iteraciones, historial_x, historial_error

def secante(f, x0, x1, tol=1e-6, max_iteraciones=100):
    historial_x = []
    historial_error = []
    
    for i in range(1, max_iteraciones + 1):
        if f(x1) - f(x0) == 0:
            print("cuidado con la division por 0")
            return 0, 0, [], []
            
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        error = abs(x2 - x1)
        
        historial_x.append(x2)
        historial_error.append(error)
        
        if abs(f(x2)) < tol or error < tol:
            return x2, i, historial_x, historial_error
            
        x0 = x1
        x1 = x2
        
    print("El metodo no alcanzo la tolerancia")
    return x1, max_iteraciones, historial_x, historial_error

def newton_raphson(f, df, x0, tol=1e-6, max_iteraciones=100):
    historial_x = []
    historial_error = []
    x_anterior = x0
    
    for i in range(1, max_iteraciones + 1):
        if df(x_anterior) == 0:
            print("la derivada es cero, el metodo falla aqui")
            return 0, 0, [], []
            
        x_actual = x_anterior - f(x_anterior) / df(x_anterior)
        
        error = abs(x_actual - x_anterior)
        
        historial_x.append(x_actual)
        historial_error.append(error)
        
        if abs(f(x_actual)) < tol or error < tol:
            return x_actual, i, historial_x, historial_error
            
        x_anterior = x_actual
        
    print("El metodo no alcanzo la tolerancia")
    return x_actual, max_iteraciones, historial_x, historial_error

def newton_raphson_mejorado(f, df, d2f, x0, tol=1e-6, max_iteraciones=100):
    historial_x = []
    historial_error = []
    x_anterior = x0
    
    for i in range(1, max_iteraciones + 1):
        fx = f(x_anterior)
        dfx = df(x_anterior)
        d2fx = d2f(x_anterior)
        
        denominador = (dfx * dfx) - (fx * d2fx)
        
        if denominador == 0:
            print("denominador dio cero, el metodo falla")
            return 0, 0, [], []
            
        x_actual = x_anterior - (fx * dfx) / denominador
        
        error = abs(x_actual - x_anterior)
        
        historial_x.append(x_actual)
        historial_error.append(error)
        
        if abs(fx) < tol or error < tol:
            return x_actual, i, historial_x, historial_error
            
        x_anterior = x_actual
        
    print("el metodo no alcanzo la tolerancia")
    return x_actual, max_iteraciones, historial_x, historial_error
