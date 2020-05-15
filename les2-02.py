# Задача 2
import math
print("Введите предложение:")
first_string = input()
first_list = list(first_string.split(" "))

if (math.fmod(len(first_list),2) == 0):
    i = int(len(first_list) / 2)
    while i > 0:
        first_list[i*2-1], first_list[i*2-2] = first_list[i*2-2], first_list[i*2-1]
        i -= 1
else:
    i = int((len(first_list) - 1)/ 2)
    while i > 0:
        first_list[i * 2 - 1], first_list[i * 2 - 2] = first_list[i * 2 - 2], first_list[i * 2 - 1]
        i -= 1
print(first_list)