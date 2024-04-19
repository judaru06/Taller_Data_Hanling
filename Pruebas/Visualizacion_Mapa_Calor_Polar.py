import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ast
import re

def safe_literal_eval(s):
    """
    Evalúa de manera segura un string conteniendo estructuras de Python,
    específicamente diseñado para manejar números complejos y listas de listas.
    """
    try:
        # Aseguramos que los números complejos tengan el formato correcto
        s = re.sub(r'(\d)\s*([+-])\s*(\d)', r'\1\2\3j', s)
        s = s.replace('[ ', '[').replace('\n', ', ').replace('j ', 'j, ')
        return np.array(ast.literal_eval(s), dtype=complex)
    except Exception as e:
        print(f"Error parsing string: {s}")
        print(f"Exception: {e}")
        return np.zeros((1,1))  # Devuelve un array de fallback si hay un error

def plot_data(file_path, max_images):
    data = pd.read_csv(file_path)
    
    # Convertir las entradas de las columnas 'ang' y 'Rx' de string a objetos de Python
    data['ang'] = data['ang'].apply(safe_literal_eval)
    data['Rx'] = data['Rx'].apply(safe_literal_eval)
    
    # Limitar el número de imágenes a generar
    for i in range(min(max_images, len(data))):
        angle_data = data.iloc[i]['ang']
        correlation_matrix = data.iloc[i]['Rx']
        
        if correlation_matrix.ndim != 2 or correlation_matrix.shape[0] <= 1:
            print(f"Skipping index {i} due to invalid data shape: {correlation_matrix.shape}")
            continue
        
        # Crear mapa de calor
        plt.figure(figsize=(10, 8))
        plt.imshow(correlation_matrix, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.savefig(f'heatmap_{i}.png')
        plt.close()  # Cerrar la figura actual para liberar memoria
        
        # Crear gráfico polar, asegurando que los datos son correctos
        if angle_data.ndim != 1:
            print(f"Skipping index {i} due to invalid angle data shape: {angle_data.shape}")
            continue
        plt.figure(figsize=(8, 8))
        ax = plt.subplot(111, polar=True)
        theta = np.deg2rad(angle_data)  # Convertir ángulos de grados a radianes
        radii = 10 * np.random.rand(len(angle_data))  # Generar radios aleatorios para la visualización
        bars = ax.bar(theta, radii, width=0.1, bottom=0.1)
        plt.savefig(f'polar_{i}.png')
        plt.close()

# Ajusta el número de imágenes a generar aquí
plot_data(r'Datos\\music_data_1_angles.csv', max_images=4)
