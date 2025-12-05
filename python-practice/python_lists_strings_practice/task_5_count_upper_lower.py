# Задача 5 - Подсчёт букв верхнего и нижнего регистра

text = "Hello World! ПрИвЕт!"

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Исходный текст:", text)
print("Букв в верхнем регистре:", upper_count)
print("Букв в нижнем регистре:", lower_count)
