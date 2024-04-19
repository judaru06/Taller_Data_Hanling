import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re

def parse_complex_numbers_correctly(matrix_str):
    # Limpiar y preparar la cadena para el procesamiento
    matrix_str = matrix_str.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '')
    # Expresión regular mejorada para capturar cualquier número complejo
    numbers = re.findall(r'[\+\-]?\d*\.?\d*e?[\+\-]?\d*[+-]\d*\.?\d*e?[\+\-]?\d*j', matrix_str)
    complex_numbers = [complex(num.replace('+-', '-').replace('++', '+').replace('-+', '-').replace('--', '+')) for num in numbers]
    
    # Verificar la cantidad correcta de números complejos
    if len(complex_numbers) != 144:
        print(f"Extracted numbers: {numbers}")
        print(f"Complex numbers: {complex_numbers}")
        raise ValueError(f"Expected 144 complex numbers, but got {len(complex_numbers)}")
    
    return np.array(complex_numbers).reshape(12, 12)


# Cargar los datos
data_1 = pd.read_csv(r'D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Datos\music_data_1_angles.csv')
data_2 = pd.read_csv(r'D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Datos\music_data_2_angles.csv')

# Aplicar la función de parseo
data_1['parsed_matrices'] = data_1['Rx'].apply(parse_complex_numbers_correctly)
data_2['parsed_matrices'] = data_2['Rx'].apply(parse_complex_numbers_correctly)

# Extraer partes reales e imaginarias y guardarlas
real_parts_1 = np.array([m.real for m in data_1['parsed_matrices']])
imaginary_parts_1 = np.array([m.imag for m in data_1['parsed_matrices']])
real_parts_2 = np.array([m.real for m in data_2['parsed_matrices']])
imaginary_parts_2 = np.array([m.imag for m in data_2['parsed_matrices']])

#Esto es por si lo quiero guardar con otros formatos
#np.savetxt('D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Imagenes\real_matrices.csv', real_parts.reshape(-1, 144), delimiter=',', header=','.join([f'R{i}' for i in range(1, 145)]))
#np.savetxt('D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Imagenes\imaginary_matrices.csv', imaginary_parts.reshape(-1, 144), delimiter=',', header=','.join([f'I{i}' for i in range(1, 145)]))

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
        plt.savefig(f"{save_path}/heatmap_1_figure_{i+1}.png")
        plt.close()  # Cerrar la figura para liberar memoria


# Llamada a la función para generar y guardar las figuras
plot_heatmaps(real_parts_1, imaginary_parts_1, num_figures=4, save_path="D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Imagenes\Angulo_1")
plot_heatmaps(real_parts_2, imaginary_parts_2, num_figures=4, save_path="D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Imagenes\Angulo_2")
