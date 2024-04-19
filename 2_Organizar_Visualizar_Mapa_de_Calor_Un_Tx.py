import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re
# Carga de la base de datos
data = pd.read_csv(r'D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Datos\music_data_1_angles.csv')

# Función para parsear los números complejos correctamente
def parse_complex_numbers_correctly(matrix_str):
    matrix_str = matrix_str.replace('[[', '').replace(']]', '').replace(' ', '')
    numbers = re.findall(r'[\+\-]?[\d\.]+(?:[\+\-][\d\.]+)?j', matrix_str)
    complex_numbers = [complex(num) for num in numbers]
    return np.array(complex_numbers).reshape(12, 12)

# Aplicación de la función a la columna de matrices complejas
data['parsed_matrices'] = data['Rx'].apply(parse_complex_numbers_correctly)

# Extracción de partes reales e imaginarias
real_parts = np.array([m.real for m in data['parsed_matrices']])
imaginary_parts = np.array([m.imag for m in data['parsed_matrices']])

def plot_heatmaps(real_matrices, imag_matrices, num_figures, save_path):
    # Configuración de estilo de Seaborn para mejorar la estética de los mapas de calor
    sns.set(style="white")

    for i in range(num_figures):
        fig, axs = plt.subplots(2, 2, figsize=(16, 12))  # 2x2 subplot por figura

        # Iterar sobre los primeros 2 datasets para cada figura
        for j in range(2):
            # Parte real
            sns.heatmap(real_matrices[2*i + j], ax=axs[j, 0], cmap='viridis', annot=True, fmt=".2f",
                        cbar=True, square=True, cbar_kws={"shrink": .82})
            axs[j, 0].set_title(f'Parte Real del Dato {2*i + j + 1}')

            # Parte imaginaria
            sns.heatmap(imag_matrices[2*i + j], ax=axs[j, 1], cmap='magma', annot=True, fmt=".2f",
                        cbar=True, square=True, cbar_kws={"shrink": .82})
            axs[j, 1].set_title(f'Parte Imaginaria del Dato {2*i + j + 1}')

        # Ajustar el layout para evitar solapamientos
        plt.tight_layout()
        # Guardar la figura
        plt.savefig(f"{save_path}/heatmap_figure_{i+1}.png")
        plt.close()  # Cerrar la figura para liberar memoria

# Cargando datos de ejemplo (deberás reemplazar estas líneas con la carga de tus archivos)
# real_parts = np.random.rand(10, 12, 12)  # Suponiendo que hay 10 matrices de 12x12
# imaginary_parts = np.random.rand(10, 12, 12)

# Llamada a la función para generar y guardar las figuras
plot_heatmaps(real_parts, imaginary_parts, num_figures=4, save_path="D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Imagenes")
