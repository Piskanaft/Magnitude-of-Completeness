import numpy as np
import pandas as pd


def simple_read(file: str,column: str) -> np.ndarray: #получить чистый список магнитуд из файла
    try:
        data = pd.read_excel(file)  
    except Exception as exc:
        print('Ошибка во время чтения файла:',exc)
        input('Нажмите Enter чтобы выйти')
        quit()
    # #TODO если не удалось найти ML, то изменить на другое
    try:
        raw_mag_column = data[column] #всё содержимое колонки
    except KeyError as err:
        print('ERROR:',err)
        print(f'Вероятнее всего, колонка с названием {column} не существует')
        input('Нажмите Enter чтобы выйти')
        quit()
    numeric_mags = raw_mag_column[pd.to_numeric(raw_mag_column,errors='coerce').notnull()] #те элементы, которые безошибочно переводятся в число
    mag = np.array(numeric_mags,dtype=float)
    return mag

def calculate(mag: np.ndarray) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    
    mag_values = np.round(np.arange(min(mag),max(mag)+0.1,0.1),1) #значения с шагом в 0.1
    discrete_counts = np.array([np.count_nonzero(np.round(mag,1) == m) for m in mag_values]) #watch out for rounding; кол-во магнитуд из списка для каждого из mag_values
    N = len(mag)
    cumulative_counts = [N]
    for i in range(len(mag_values)):
        cumulative_counts.append(cumulative_counts[-1]-discrete_counts[i])
    cumulative_counts = np.array(cumulative_counts[:-1])
    #TODO проверка на адекватность: len(mag), sum(discrete_counts)
    return mag_values,discrete_counts,cumulative_counts

def MAXC(mag_values,discrete_counts):
    return mag_values[np.argmax(discrete_counts)]
    