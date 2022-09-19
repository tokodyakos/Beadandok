# Maximum keresés

from operator import index

lista = [-1000, -600, -200, -500]

max, a = -1000, 0
index = 0

for i in lista:
    index += 1
    print("max: ", max, "i:", i, "index: ", index)