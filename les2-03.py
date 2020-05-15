# Задача 3
#
seasons_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
num = int(input())
print(seasons_list[num-1])
Seasons = {"Зима":[12,1,2], "Весна":[3,4,5],"Лето":[6,7,8], "Осень":[9,10,11]}
for key, value_list in iter(dict.items(Seasons)):
    for value in value_list:
        if value == num:
            print(key)