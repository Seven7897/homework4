# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

number = int(input("Задайте число : "))
list = []

while (number >= 2):
    if number % 2 == 0:
        number /= 2
        list.append(2)
    if number % 3 == 0:
        number /= 3
        list.append(3)
    if number % 5 == 0:
        number /= 5
        list.append(5)
    if number % 7 == 0:
        number /= 7
        list.append(7)
    if number % 11 == 0:
        number /= 11
        list.append(11)
    if number % 13 == 0:
        number /= 13
        list.append(13)
    if number % 17 == 0:
        number /= 17
        list.append(17)
    if number % 19 == 0:
        number /= 19
        list.append(19)
print(list)