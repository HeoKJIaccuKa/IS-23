x = int(input("Введите число Х: "))
y = int(input("Введите число У: "))

if x>0 and y>0:
    print("I-я")

if x<0 and y>0:
    print("II-я")

if x<0 and y<0:
    print("III-я")

if x>0 and y<0:
    print("IV-я")