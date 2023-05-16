# 1. В матрице найти среднее арифметическое положительных элементов, кратных 3.
# 2. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3
import random

def create_matrix():
    '''Функция - создание матрицы.'''
    size_matrix = random.randint(2, 8)
    matrix = [[random.randint(0, 20) for i in range(size_matrix)] for j in range(size_matrix)] #Генерация массива.

    print("Вывод матрицы:")
    obj = iter(matrix) #Итерируемый объект проходит по каждому элементу.
    for i in range(size_matrix): # Цикл который проходит по каждому элементу в списке/матрице.
        print(next(obj))  #Вывод каждого элемента

    numb = [j for i in matrix for j in i if j % 3 == 0] #Проверка на кратность к 3 каждого элемента
    print("Среднее арифметическое положительных элементов кратных 3: {}".format(sum(numb)/len(numb) if len(numb) != 0 else sum(numb) // 1))

print(create_matrix()) #Вызов функции.
