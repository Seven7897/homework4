# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

from itertools import count


my_string = input("Введите елементы через пробел : ").split()
i = 0
while (i < len(my_string)):
    j = i + 1
    countt = 0
    while j < len(my_string):
        if j != i:
            if my_string[i] == my_string[j]:
                my_string.pop(j)
                countt +=1
                j = i
        j += 1
    if countt != 0 :
        my_string.pop(i)
        i = -1
    i += 1
print(my_string)
