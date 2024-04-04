import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('datos_MUSIC_3.csv')

# Extraer la tercera columna que contiene la matriz compleja
matriz_compleja_str = df.iloc[:,2]
print(f'parte_compleja {type(matriz_compleja_str)}')
#print(matriz_compleja_str)

# Supongamos que tienes una matriz compleja llamada 'matriz_compleja'
matriz_compleja = np.array(matriz_compleja_str)

# Separar la parte real e imaginaria de la matriz
parte_real = np.real(matriz_compleja)
parte_imaginaria = np.imag(matriz_compleja)

#Imprimir las matrices separadas
print("Parte Real:")
print(f'parte_Real {type(parte_real)}')
print(parte_real[2])
print("\nParte Imaginaria:")
print(parte_imaginaria[2])
