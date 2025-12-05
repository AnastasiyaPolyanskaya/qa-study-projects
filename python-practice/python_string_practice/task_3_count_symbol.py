text = input("Введите строку: ")
symbol = input("Введите символ для поиска: ")

count = 0

for char in text:
    if char == symbol:
        count += 1

print("Количество вхождений:", count)
