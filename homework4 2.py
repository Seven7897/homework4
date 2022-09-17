# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

number = int(input("Задайте число : "))
list = []
while (number > 2 or number > 1):
    i = 2
    number1 = number
    while (number == number1):
        if number % i == 0:
            number /= i
            print(i)
            list.append(i)
        i += 1
print(list)
