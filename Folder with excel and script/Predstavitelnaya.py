try:
    
    import os
    import time
    import numpy as np
    import pandas as pd
    import math
    import warnings
    import matplotlib.pyplot as plt
    plt.rcParams["figure.autolayout"] = True
    # plt.style.use('classic')
    from matplotlib.offsetbox import AnchoredText
    # plt.rcParams["figure.figsize"] = (100,100)
    
    warnings.filterwarnings('ignore')
except Exception as exc:
    print('Ошибка во время загрузки библиотек:',exc)
    input('Нажмите Enter чтобы выйти')
    quit()



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

def simple_read(file: str,sheet,column: str) -> np.ndarray: #получить чистый список магнитуд из файла
    try:
        data = pd.read_excel(file,sheet_name=sheet)
    except Exception as exc:
        print('Ошибка во время чтения файла:',exc)
        input('Нажмите Enter чтобы выйти')
        quit()
    #TODO если не удалось найти ML, то изменить на другое
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

def get_ab_values(mag: np.ndarray, M_co: float) -> tuple[float,float]: 
# оценки a,b методом максимального правдоподобия СРАВНИТЕЛЬНЫЙ АНАЛИЗ МЕТОДОВ ОЦЕНКИ МАГНИТУДЫ
#ПРЕДСТАВИТЕЛЬНОЙ РЕГИСТРАЦИИ ЗЕМЛЕТРЯСЕНИЙ стр 101.
    M_bin = 0.1 #интервал группировки
    M_filtered = mag[mag>=M_co] 
    M_mean = np.mean(M_filtered) 

    b_value = math.log10(math.e)/(M_mean-M_co+M_bin/2)
    N = len(M_filtered)
    try:
        a_value = math.log10(N)+b_value*M_co
    except ValueError as err:
        print('Ошибка во время счёта a_value:',err)
        if N==0:
            print('Вероятнее всего нельзя посчитать c заданным уровнем доверия')
    except Exception as exc:
        print('Ошибка во время определения a_value:',exc)


    return a_value, b_value

def MAXS(mag_values,discrete_counts):
    
    
    return mag_values[np.argmax(discrete_counts)]
    
        

def Goodness_of_fit(mag,mag_values,discrete_counts,cumulative_counts):
    M_bin = 0.1
    
    mag = np.round(mag,1) #группируем все магнитуды округлением до M_bin
    M_co_start = min(mag) #значение магнитуды нижней отсечки
    M_array = np.arange(M_co_start,max(mag)+M_bin,0.1) #часть выборки с магнитудой m>=M_c
    R = np.array([])

    for M_co in np.round(np.arange(M_co_start,max(mag)+M_bin,M_bin),1): # округление нужно
        mag = mag[mag>=M_co]
        a,b = get_ab_values(mag,M_co)
        
        #синтетические кумулятивные значения в соответствии с законом повторяемости 
        N_array = S = 10**(a-b*M_array)
        M_array = M_array[1:]

        B = cumulative_counts[np.where(mag_values == M_co)[0][0]:]
        
        R_last = 100- np.sum( np.abs(B - S))/sum(cumulative_counts)*100
        R = np.append(R,R_last)
        
        if R_last >= 95:
            return M_co
        #TODO draw Residual (100-R) as a function of minimum magnitude cutoff
    return R
def LLS(mag,mag_values):
    
    M_bin = 0.1
    n = len(mag_values) # number of bins. #? must change with every step of M_co
    M_co_start = round(min(mag),1) #round down to catch all values?
    M_co_finish = round(max(mag),1)
    M_co_to_test = np.array(np.arange(M_co_start,M_co_finish,M_bin)) # ? M_co_finish+M_bin: 5.1 is not for tesst
    
    _2QI = []
    I_list = []
    t_list = []
    
    for M_co in M_co_to_test:
        
        
        # ? redo n definition
        mag = mag[mag>=M_co] # ?
        M_i_array = np.array([M_co+i*M_bin for i in range(0,n+1)])
        # N_array = np.array([np.count_nonzero((M_co+i*M_bin-M_bin/2 <=mag) & (mag <=M_co+i*M_bin+M_bin/2)) for i in range(n)]) # TODO redo with new definition of M_i_array
        N_array = np.array([np.count_nonzero((mag >= M_i-M_bin/2) & (mag<=M_i+M_bin/2)) for M_i in M_i_array]) # redon with new definition of M_i_array
        # ? mag <= or mag < : possible double count
        
        Q_0 = sum(N_array)
        P = N_array/Q_0
        P[P==0]=0.0000000000001 #log of 0 is not defined
        
        try:
            a,b = get_ab_values(mag,M_co)
        except:
            print('Не могу посчитать a,b в методе LLS(1)')
            print(f"Если значение M = {round(M_co,1)} близко к максимальному значению в выборке ({max(mag_values)}), значит не получается посчитать методом LLS с заданным уровнем доверия")
            return 'error1'

        PIE =10**(-b*(M_i_array-M_co))/sum(10**(-b*(M_i_array-M_co))) #wrong expression in 2022 there it's e in the denominator
        I=  np.sum(P*np.log(P/PIE))
        #если уровень значимости ниже, от отвергаем гипотезу о прямолинейности ??
        # TODO систематическое смещение
        
        if I<0.05:
            # print('by I')
            return round(M_co,1)
        I_list.append(I)

        ##################ВЫЯСНЕНИЕ ПРИЧИНЫ НЕЛИНЕЙНОСТИ#####################
        try:
            a,b = get_ab_values(mag[mag>=M_co+M_bin],M_co)
        except:
            print('Не могу посчитать a,b в методе LLS(2)')
            print(f"Если значение M = {round(M_co,1)} близко к максимальному значению в выборке ({max(mag_values)}), значит не получается посчитать методом LLS с заданным уровнем доверия")
            return 0
        X_i_array = 10**(-b*(M_i_array-M_co))
        # psi = np.array([sum(i**k*X_i_array) for k in [0,1,2]]) 
        psi = np.array([])
        for k in [0,1,2]:
            summa = 0
            for i in range(1,len(M_i_array)):
                summa+= i**k*X_i_array[i]
            psi = np.append(psi,summa)
        
        
        p_hat = N_array[0]*psi[0]/(Q_0-N_array[0])
        
        Var_p_hat = (N_array[0]*psi[0]**2/(Q_0-N_array[0])**2) + ((N_array[0]**2*psi[0]**3*psi[2])/((Q_0-N_array[0])**3*(psi[0]*psi[2]-psi[1]**2)**2))

        t = (1-p_hat)/(Var_p_hat)**0.5
        # print('t',round(t,2))
        if t < 0.95:
            # print('by t')
            return round(M_co,1)

        t_list.append(t)
        
    return 'couldnt'

def draw(mag_values,discrete_counts,cumulative_counts,M_MAXS=0,M_LLS=0,M_GFT=0,a=0,b=0):
    fig, ax = plt.subplots()
    
    plt.scatter(mag_values,discrete_counts,marker="^",s=40)
    plt.yscale('log')
    plt.xlim(min(mag_values)-0.1,max(mag_values)+0.1)
    plt.ylim(1,max(cumulative_counts)+0.1*max(cumulative_counts))
    plt.grid()
    
    M = np.arange(0,6,0.1)
    N = 10**(a-b*M)
    plt.plot(M,N)
    
    plt.scatter(mag_values,cumulative_counts)

    # TODO add their xticks
    plt.plot([M_MAXS,M_MAXS],[-1,10**4],c='green')
    plt.plot([M_GFT,M_GFT],[-1,10**4],c='red')
    plt.plot([M_LLS,M_LLS],[-1,10**4],c='blue')

    text = AnchoredText(f"{filename_to_open}\n{choosen_sheetname}\n{M_MAXS=}\n{M_LLS=}\n{M_GFT=}", 
                    prop=dict(size=11), frameon=True,loc='upper right',
                    )
    text.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(text)
    # plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    global filename_to_open 
    current_directory = os.getcwd()
    xlsx_files_in_directory  =[]
    try:
        for filename in os.scandir(current_directory):
            if filename.is_file() and filename.name.endswith('xlsx'):
                xlsx_files_in_directory.append(filename.path)
                
                filename_to_open = filename.name
        if len(xlsx_files_in_directory)==0:
            raise Exception('В папке со скриптом не обнаружено .xlsx документа')
        if len(xlsx_files_in_directory)>1:
            raise Exception('В папке со скриптом обнаружено больше 1 .xlsx документа')
    except Exception as exc:
        print(exc)
        input('Нажмите Enter чтобы выйти')
        quit()
        
        
    
    filepath_to_open = xlsx_files_in_directory[0]
   
    print('Работаем с',filepath_to_open)
    
    # TODO ошибка если обнаружено несколько
    # TODO ошибка если не обнаружено
    # TODO указать какие обнаружены
    Flag = True
    while Flag:
        try:
            available_sheets = pd.ExcelFile(filepath_to_open).sheet_names
        except FileNotFoundError as err:
            print('Не найден файл по указанному адресу')
            continue
        
        print(f'Введите цифру, чтобы выбрать один из {len(available_sheets)} лист(ов).\nЧтобы дополнительно вывести рисунок, через пробел после цифры добавьте любой символ\nЧтобы выйти, отправьте пустое сообщение.')
        for i,sheet_name in enumerate(available_sheets,1):
            print(f'{i}) {sheet_name}')

        
        request = input('Выбор: ')
        if not request:
            print('Чтобы выйти, нажмите Enter ещё раз')
            print('Чтобы остаться, отправьте не пустое сообщение')
            if not input():
                exit()
            else:
                continue
        choice, *args = request.split()
        try:
            n_choice = int(choice)
        except ValueError:
            print('Не могу распознать введённое как число')
            continue
        
        

        try:
            global choosen_sheetname
            choosen_sheetname = available_sheets[n_choice-1]
        except IndexError as err:
            print('ERROR:',err)
            print('Вероятнее всего, неправильно выбран номер листа')
            continue
        
        
        mag = simple_read(filepath_to_open,n_choice-1,'ML')
        # TODO сделать выбор листа
        # TODO сделать проверку на наличие столбца с таким названием
        try:
            mag_values,discrete_counts,cumulative_counts = calculate(mag)
        except Exception as exc:
            print('Ошибка во время анализа прочитанных магнитуд:', exc)
            input('Нажмите Enter чтобы выйти')
            quit()
        try:
            M_MAXS = MAXS(mag_values,discrete_counts)
        except Exception as exc:
            print('Ошибка во время счёта M_MAXS:',exc)
            M_MAXS = 0
        try:
            M_GFT = Goodness_of_fit(mag,mag_values,discrete_counts,cumulative_counts)
        except Exception as exc:
            print('Ошибка во время счёта M_GFT:',exc)
            M_GFT = 0
        try: 
            M_LLS = LLS(mag,mag_values)
        except Exception as exc:
            print('Ошибка во время счёта M_LLS:',exc)
            M_LLS = 0
        print('========================')
        print(f'Результат для листа {choosen_sheetname}:')
        print(f'{M_MAXS=}')
        print(f'{M_GFT=}')
        print(f'{M_LLS=}')
        if args:
            draw(mag_values,discrete_counts,cumulative_counts,M_MAXS,M_LLS,M_GFT)
        print('========================')
        