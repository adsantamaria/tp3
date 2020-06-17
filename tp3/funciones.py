import numpy as np
import scipy

def get_transformada(x_t):
    X_w = scipy.fft.fft(x_t)
    return X_w

def funcion_seno(t_inicial, t_final, amplitud, frecuencia, phi_0, precision):
    cantidad_muestras = obtener_cantidad_de_muestras(precision, t_final, t_inicial)
    eje_t = np.linspace(t_inicial, t_final, cantidad_muestras, endpoint=False)
    seno = []
    for k in range(len(eje_t)):
        seno.append(amplitud * np.sin(2 * np.pi * frecuencia * eje_t[k] + phi_0))
    return eje_t, np.array(seno)

def obtener_cantidad_de_muestras(precision, t_final, t_inicial):
    cantidad_muestras = (t_final - t_inicial) * precision
    return cantidad_muestras

def obtener_amplitud(X_w):
    return np.abs(X_w)[0:int(len(X_w) / 2)] / (len(X_w) / 2)