# Задача 5 — Подсчёт букв в верхнем и нижнем регистре

text = "Hello World! PYTHON is Awesome!"

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Строка:", text)
print("Количество заглавных букв:", upper_count)
print("Количество строчных букв:", lower_count)
