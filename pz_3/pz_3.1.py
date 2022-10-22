import numpy as np

x,y = list(np.random.choice(range(+6, 11), 2))
print("x = {0}, y = {1}".format(x,y))

b = (x > 0 and y > 0)
print("Точка лежит во 2-й координатной четверти: ", b)