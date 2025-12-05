# Задача 3 - Фильтрация только букв из строки

text = "Hello123! Привет456?"

letters = ""

for char in text:
    if char.isalpha():
        letters += char

print("Исходная строка:", text)
print("Только буквы:", letters)
