import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

class ComplexMatrixParser:
    def __init__(self, expected_size=144):
        self.expected_size = expected_size

    def parse(self, matrix_str):
        matrix_str = matrix_str.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '')
        numbers = re.findall(r'[\+\-]?\d*\.?\d*e?[\+\-]?\d*[+-]\d*\.?\d*e?[\+\-]?\d*j', matrix_str)
        complex_numbers = [complex(num.replace('+-', '-').replace('++', '+').replace('-+', '-').replace('--', '+')) for num in numbers]

        if len(complex_numbers) != self.expected_size:
            print(f"Extracted numbers: {numbers}")
            print(f"Complex numbers: {complex_numbers}")
            raise ValueError(f"Expected {self.expected_size} complex numbers, but got {len(complex_numbers)}")
        
        return np.array(complex_numbers).reshape(int(np.sqrt(self.expected_size)), int(np.sqrt(self.expected_size)))

class DataHandler:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)
        self.parser = ComplexMatrixParser()

    def parse_matrices(self, column_name):
        self.data['parsed_matrices'] = self.data[column_name].apply(self.parser.parse)

    def get_real_imaginary_parts(self):
        real_parts = np.array([m.real for m in self.data['parsed_matrices']])
        imaginary_parts = np.array([m.imag for m in self.data['parsed_matrices']])
        return real_parts, imaginary_parts

class MatrixVisualizer:
    def __init__(self, save_path):
        self.save_path = save_path

    def plot_heatmaps(self, real_matrices, imag_matrices, num_figures):
        sns.set(style="white")
        for i in range(num_figures):
            fig, axs = plt.subplots(2, 2, figsize=(16, 12))
            for j in range(2):
                sns.heatmap(real_matrices[2*i + j], ax=axs[j, 0], cmap='viridis', annot=True, fmt=".2f", cbar=True, square=True, cbar_kws={"shrink": .82})
                axs[j, 0].set_title(f'Parte Real del Dato {2*i + j + 1}')

                sns.heatmap(imag_matrices[2*i + j], ax=axs[j, 1], cmap='magma', annot=True, fmt=".2f", cbar=True, square=True, cbar_kws={"shrink": .82})
                axs[j, 1].set_title(f'Parte Imaginaria del Dato {2*i + j + 1}')
            
            plt.tight_layout()
            plt.savefig(f"{self.save_path}/heatmap_figure_{i+1}.png")
            plt.close()

# Ejemplo de uso
data_1_handler = DataHandler(r'D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Datos\music_data_1_angles.csv')
data_2_handler = DataHandler(r'D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Datos\music_data_2_angles.csv')

data_1_handler.parse_matrices('Rx')
data_2_handler.parse_matrices('Rx')

real_parts_1, imaginary_parts_1 = data_1_handler.get_real_imaginary_parts()
real_parts_2, imaginary_parts_2 = data_2_handler.get_real_imaginary_parts()

visualizer = MatrixVisualizer("D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Imagenes\Angulo_1")
visualizer.plot_heatmaps(real_parts_1, imaginary_parts_1, num_figures=4)
visualizer = MatrixVisualizer("D:\Maestria\Semestre_2\Programacion Cientifica\Taller_Data_Hanling\Imagenes\Angulo_2")
visualizer.plot_heatmaps(real_parts_2, imaginary_parts_2, num_figures=4)