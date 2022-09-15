# Вычислить число c заданной точностью d
# при $d = 0.001, π = 3.141
import string


number = input("Задайте точность : ")
count = 0
for i in range(len(number)):
    if number[i] == ".":
        k = i + 1
        while k < len(number):
            count += 1
            k += 1


k = 1
pi = 0
for k in range(1, 1000000):
    pi = pi+4*((-1)**(k+1))/(2*k-1)


list = [None] * (count + 2)
i = 0
pii = str(pi)

while i <= count + 1:
    list[i] = pii[i]
    print(list[i])
    i += 1

list = "".join(list)
print(list)


