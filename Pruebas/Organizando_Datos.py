import pandas as pd
import ast

# Función para contar el número de ángulos por entrada en la columna 'ang'
def count_angles(angle_string):
    try:
        # Convertimos el string a lista usando ast.literal_eval y contamos las sublistas (ángulos)
        angle_list = ast.literal_eval(angle_string)
        return len(angle_list)
    except:
        # Si hay un error en la conversión, devolvemos 0
        return 0

# Carga del archivo CSV
data = pd.read_csv('datos_MUSIC_3.csv')

# Aplicamos la función para contar los ángulos
data['angle_count'] = data['ang'].apply(count_angles)

# Separar los datos en cinco grupos basados en la cantidad de ángulos
grouped_data = {n: data[data['angle_count'] == n] for n in range(1, 6)}

# Eliminamos la columna 'angle_count' antes de guardar los datos
for n in grouped_data:
    grouped_data[n].drop(columns=['angle_count'], inplace=True)

# Guardamos cada grupo en un archivo CSV
for n in range(1, 6):
    filename = f'music_data_{n}_angles.csv'
    grouped_data[n].to_csv(filename, index=False)