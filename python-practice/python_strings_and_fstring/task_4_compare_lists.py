# Задача 4 - Сравнение двух списков: поиск общих элементов

list1 = [1, 3, 5, 7, 9, 11]
list2 = [2, 3, 5, 8, 11]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Первый список:", list1)
print("Второй список:", list2)
print("Общие элементы:", common)
