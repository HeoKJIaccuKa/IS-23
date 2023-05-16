# 2. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3


import random

size_matrix = random.randint(2, 8)

def create_matrix():
    '''Функция - создание матрицы.'''
    matrix = [[random.randint(0, 20) for i in range(size_matrix)] for j in range(size_matrix)] #Создание матрицы.

    print("Вывод матрицы:")
    obj = iter(matrix)  #Итерируемый объект проходит по каждому элементу.
    for i in range(size_matrix): # Цикл который проходит по каждому элементу в списке/матрице.
        print(next(obj)) #Вывод каждого элемента

    while True: #Пока True/ бесконечный цикл
        number = int(input(f"Введите число - элементов строки матрицы.\nДоступно строк: {size_matrix}: ")) #Ввод
        if 0 < number <= len([i for i in range(size_matrix)]): #Условие что введённое число в допустипом диапазоне.
            break
    print("Увеличение каждой строки матрицы на {}".format(number))
    print("Итоговая матрица: ")
    for j, k in enumerate(matrix): #Цикл который проходится по каждому значению в матрице.
        if j == number: # Проверка на строку.
            for i in range(len(k)):
                matrix[j][i] *= 3 #Умножение каждого элемента в массиве на 3.
        print(k) #Вывод.

create_matrix()
