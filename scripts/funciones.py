import numpy as np

# función polinómica de raíz simple [x^3 - x - 2]
def f_poli(x):
    return x**3 - x - 2

def df_poli(x):
    return 3 * x**2 - 1

def d2f_poli(x):
    return 6 * x

# funcion polinomica de raíz doble [(x - 2)^2]
def f_doble(x):
    return (x - 2)**2

def df_doble(x):
    return 2 * (x - 2)

def d2f_doble(x):
    return 2

# funcion logaritmica [ln(x) + x - 4]
def f_log(x):
    return np.log(x) + x - 4

def df_log(x):
    return (1 / x) + 1

def d2f_log(x):
    return -1 / (x**2)

# funcion exponencial [e^(-x) - x]
def f_exp(x):
    return np.exp(-x) - x

def df_exp(x):
    return -np.exp(-x) - 1

def d2f_exp(x):
    return np.exp(-x)

# función trigonometrica [cos(x) - x]
def f_trig(x):
    return np.cos(x) - x

def df_trig(x):
    return -np.sin(x) - 1

def d2f_trig(x):
    return -np.cos(x)

# funcion Mixta [raiz(x) - cos(x)]
def f_mixta(x):
    return np.sqrt(x) - np.cos(x)

def df_mixta(x):
    return 1 / (2 * np.sqrt(x)) + np.sin(x)

def d2f_mixta(x):
    return -1 / (4 * x**(1.5)) + np.cos(x)
