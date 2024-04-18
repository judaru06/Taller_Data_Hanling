import pandas as pd
import numpy as np
import re

# Leer el archivo CSV
df = pd.read_csv('parte_compleja.csv')
matriz_compleja_str = df.values
matriz_compleja = np.zeros(matriz_compleja_str.shape, dtype=complex)
for i in range(matriz_compleja_str.shape[0]):
    for j in range(matriz_compleja_str.shape[1]):
        matriz_compleja[i, j] = complex(matriz_compleja_str[i, j])
parte_real = np.real(matriz_compleja)
parte_imaginaria = np.imag(matriz_compleja)
# Crear un DataFrame de pandas para las partes real e imaginaria
df_real = pd.DataFrame(parte_real)
df_imaginaria = pd.DataFrame(parte_imaginaria)

# Escribir los DataFrames en archivos CSV
df_real.to_csv('parte_real.csv', index=False)
df_imaginaria.to_csv('parte_imaginaria.csv', index=False)