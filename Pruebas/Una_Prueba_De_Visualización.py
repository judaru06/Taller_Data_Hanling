import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generar datos de ejemplo para las partes real e imaginaria de la matriz de correlación
num_antenas = 12
datos_real = np.random.rand(num_antenas, num_antenas)
print(type(datos_real))
datos_imaginarios = np.random.rand(num_antenas, num_antenas)

# Visualización de la parte real de la matriz de correlación como un mapa de calor
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
sns.heatmap(datos_real, annot=True, cmap='coolwarm', fmt=".2f", xticklabels=range(1, num_antenas + 1), yticklabels=range(1, num_antenas + 1))
plt.title('Parte Real de la Matriz de Correlación')
plt.xlabel('Número de Antena')
plt.ylabel('Número de Antena')

# Visualización de la parte imaginaria de la matriz de correlación como un mapa de calor
plt.subplot(1, 2, 2)
sns.heatmap(datos_imaginarios, annot=True, cmap='viridis', fmt=".2f", xticklabels=range(1, num_antenas + 1), yticklabels=range(1, num_antenas + 1))
plt.title('Parte Imaginaria de la Matriz de Correlación')
plt.xlabel('Número de Antena')
plt.ylabel('Número de Antena')

plt.tight_layout()
plt.savefig('LAB_Prueba.png')
plt.show()
