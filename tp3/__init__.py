import numpy as np
from matplotlib import pyplot as plt
from tp3.funciones import funcion_seno
from tp3.funciones import get_transformada
from tp3.funciones import obtener_cantidad_de_muestras
from tp3.funciones import obtener_amplitud


limite_1 = -10
limite_2 = 10
duracion = limite_2 - limite_1
frecuencia_fundamental = 1
amplitud = 1
fase = 0
frecuencia_muestreo_señal_original = 500
frecuencia_muestreo = 20

#genero las señales seno
eje_tiempo, eje_amplitud = funcion_seno(limite_1, limite_2, amplitud, frecuencia_fundamental,  fase, frecuencia_muestreo_señal_original)
eje_tiempo2, eje_amplitud2 = funcion_seno(limite_1, limite_2, amplitud, frecuencia_fundamental, fase, frecuencia_muestreo)

#genero las transformadas
transformada = get_transformada(eje_amplitud)
transformada2 = get_transformada(eje_amplitud2)

#calculo el modulo de la transformada (tomo la mitad porque el seno es espejada)
modulo_transformada = np.abs(transformada)[0:int(len(transformada)/2)]/(len(transformada)/2)
modulo_transformada2 = np.abs(transformada2)[0:int(len(transformada2)/2)]/(len(transformada2)/2)

#calculo y creo el eje de las frecuencias.
eje_frecuencias = np.linspace(0, frecuencia_muestreo_señal_original, duracion*frecuencia_muestreo_señal_original, endpoint=None)[0:int(len(transformada)/2)]
eje_frecuencias2 = np.linspace(0, frecuencia_muestreo, duracion*frecuencia_muestreo, endpoint=None)[0:int(len(transformada2)/2)]

#grafico en tiempo y en frecuencia
fig, axes = plt.subplots(1, 2)
fig2, axes2 = plt.subplots(1, 2)

axes[0].plot(eje_tiempo, eje_amplitud)
axes[1].set_xlabel("t (seg)")
axes[1].plot(eje_frecuencias, modulo_transformada)
axes[1].set_xlabel("f (Hz)")

axes2[0].plot(eje_tiempo2, eje_amplitud2)
axes2[1].set_xlabel("t (seg)")
axes2[1].plot(eje_frecuencias2, modulo_transformada2)
axes2[1].set_xlabel("f (Hz)")

plt.show()