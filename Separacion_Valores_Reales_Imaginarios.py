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

# Guardar las partes reales e imaginarias en archivos CSV
np.savetxt(r'D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Datos\real_matrices.csv', real_parts.reshape(-1, 144), delimiter=',', header=','.join([f'R{i}' for i in range(1, 145)]))
np.savetxt(r'D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Datos\imaginary_matrices.csv', imaginary_parts.reshape(-1, 144), delimiter=',', header=','.join([f'I{i}' for i in range(1, 145)]))
