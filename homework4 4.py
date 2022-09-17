# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
stepen = int(input("Задайте степень : "))
number = 0
list = []
x = 'x'
def mnohochlen(n):
    if n == 1 :
        list.append(f"{random.randint(1, 101)}x + {random.randint(1, 101)} = 0")
        return 
    list.append(f"{random.randint(1, 101)}x**{n} +")
    return mnohochlen(n - 1)
print(mnohochlen(stepen))
print(*list)
