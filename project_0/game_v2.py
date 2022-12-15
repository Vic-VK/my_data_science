import numpy as np
def random_predict(number:int=1) -> int: #определяет количество попыток
    
    """ Рандомно/случайно угадываем число
    Args:
    number(int, optional): Загаданное число. Defaults to 1.
    
    Returns:
    int: Число попыток
    """
    count=0 # переменнная счетчик/количество попыток    
    
    while True: # цикл, который подсчитывает попытки и позволяет вводить числа до тех пор пока пользователь не угодает число
        count+=1
        predict_number=np.random.randint(1, 101) #угадываем предполагаемое число
        if number == predict_number:
            break # конец игры, выход из цикла, если угодали
    return(count)
    
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int: #определяет среднее значение попыток при угадывании 1000 чисел функцией/алгоритмом random_predict(number)
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадования

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1) #фиксируем значение для одинакового получения/генерации случайных чисел (воспроизведение чисел не зависимо от компьютера и в любое время)
    random_array=np.random.randint(1,101, size=(1000)) #загадали список чисел
    for number in random_array: #цикл для создания списка количества попыток угадывания числа
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

def new_func(random_predict, score_game):
    score_game(random_predict)

if __name__=='__main__':
    #RUN
#   score_game(random_predict)
    new_func(random_predict, score_game)

