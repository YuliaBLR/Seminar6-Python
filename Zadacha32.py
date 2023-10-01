# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума) 
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

random_list = [random.randint(-20, 20) for _ in range(20)]
print(random_list)
minNum = int(input("Минимальный порог: "))
maxNum = int(input("Максимальный порог: "))
resalt_list = []
for i in range(0,len(random_list)-1):
    if minNum <= random_list[i] <= maxNum:
        resalt_list.append(i)
print(resalt_list)