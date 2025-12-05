# Задача 4 - Сравнение списков

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common = []

for item in list_a:
    if item in list_b:
        common.append(item)

print("Список A:", list_a)
print("Список B:", list_b)
print("Общие элементы:", common)
