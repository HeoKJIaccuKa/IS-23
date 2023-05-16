#Открытие файла.
with open("text18-27.txt", encoding="UTF-8") as f1:
    f2 = f1.read() #Чтение первого файла.
    print(f"Содержимое файла: \n{f2}") #Вывод содержимого файла.
    print("\nКоличество пробелов: {}".format(len([i for i in f2 if i == " "]))) #Подсчет количества пробелов.

with open("text18-27.txt", "a", encoding='UTF-8') as f2:
    string_for_user = input("Введите любое предложение: ") # Вввод от пользователя.
    f2.write("\n"+string_for_user) #Запись в файл данных, а именно строки, которая данна от пользователя.
