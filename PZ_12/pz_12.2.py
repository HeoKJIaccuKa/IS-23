# 2.Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.


def write_string_for_user():
    """Функция в которой вводится строка."""
    str_user = input("Введите строку: ")
    return str_user

def translate_word(str_u):
    '''Функция которая возвращает каждый символ в верхнем регистре.'''
    for i in str_u:
        yield i.upper()



a = translate_word(write_string_for_user()) #Вызов функций.
s = ''.join(a) # К строке добавляется каждое значение из строки в верхнем регистре.
print(s) #Вывод.
