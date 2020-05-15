# Задача 1
# first_string = "cap, 0.1uf, 25V, NP0, 10, CC0603"
# first_list = list(first_string.split(","))
# print(first_list)
# print(len(first_list))
#
# for el in first_list:
#     print(type(el))
#
# second_list = ["cap", "0.1uF", "25V", 10, "CC0603"]
#
# for el in second_list:
#     print(type(el))


# Задача 2
# import math
# print("Введите предложение:")
# first_string = input()
# first_list = list(first_string.split(" "))
#
# if (math.fmod(len(first_list),2) == 0):
#     i = int(len(first_list) / 2)
#     while i > 0:
#         first_list[i*2-1], first_list[i*2-2] = first_list[i*2-2], first_list[i*2-1]
#         i -= 1
# else:
#     i = int((len(first_list) - 1)/ 2)
#     while i > 0:
#         first_list[i * 2 - 1], first_list[i * 2 - 2] = first_list[i * 2 - 2], first_list[i * 2 - 1]
#         i -= 1
# print(first_list)


# Задача 3
#
# seasons_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
# num = int(input())
# print(seasons_list[num-1])
# Seasons = {"Зима":[12,1,2], "Весна":[3,4,5],"Лето":[6,7,8], "Осень":[9,10,11]}
# for key, value_list in iter(dict.items(Seasons)):
#     for value in value_list:
#         if value == num:
#             print(key)

# Задача 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# print("Введите сроку из нескольких слов:")
# first_string = input()
# first_list = list(first_string.split(" "))
# print(first_list)
# for el in first_list:
#     print(el[0:10])

# Задача 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# my_list = [7, 5, 3, 3, 2]
# cycle = 1
# while cycle == 1:
#     print("Введите натуральное число:")
#     num = int(input())
#     try :
#         num_num = my_list.index(num)
#         my_list.insert(num_num + 1, num)
#     except Exception:
#         my_list.append(num)
#     print(my_list)
#     print("Еще одно число? 1 - да, 2 - нет:")
#     answ = int(input())
#     if answ == 2:
#         cycle = 0

# Задача 6
dict_pricelist = {"название": "", "цена": "", "количество": "", "ед.": ""}
cycle = 1
dict_count=0
pricelist_tuple_list=[]
pricelist_tuple_list.clear()


while cycle == 1:

    for key in dict_pricelist:
        print(f"Введите {key}")
        dict_pricelist[key] = input()
    print("Еще одно число? 1 - да, 2 - нет:")
    answ = int(input())
    try:
        if answ == 2:
            cycle = 2
    except Exception:
        print("Не число!\nЕще одно число? 1 - да, 2 - нет:")
        answ = int(input())
    pricelist_tuple_list.append(dict_pricelist)




print(pricelist_tuple_list)
print(dict_pricelist)
key = 0

temp_list = ["1","2"]
temp_list.clear()

#
# for key, value in dict_pricelist:
#     for newvalue in value:
#         temp_list.append(list(dict_pricelist[key]))


print(temp_list)
