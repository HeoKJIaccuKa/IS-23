# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл
import re


def open_file():
    '''Функция, которая работает с файлом. Открывает, читает файл.'''
    text = ""
    with open("dostoevsky.txt", "r", encoding="UTF-8") as f2:
        f3 = f2.read() #чтение файла.
        for k in f3: #цикл, который проходится по каждому элементу в файле.
            text += k #счетчик
        return text #возвращает содержимое файла.


def reg_search_file(text):
    """Функция, которая создаёт новый файл и записывает в него данные."""
    with open("dostoevsky_2.txt", "w", encoding="UTF-8") as f1:
        for i in text.split("\n"): #Цикл, проходится по каждому значению в файле.
            if re.search(r"1857", i): #Регулярное выражение, поиск числа 1857г.
                indx = text.index("1857") #Нахождение индекса элемента.
            elif re.search(r"1860", i):
                indx_2 = text.index("1860")
        for k in text[indx:indx_2]: #Запись в файл данных через цикл.
            f2 = f1.write(k)

print(reg_search_file(open_file())) #Вызов функций
