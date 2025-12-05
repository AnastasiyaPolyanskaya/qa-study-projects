text = input("Введите строку: ")

print("Буквы в строке:")

for char in text:
    if char.isalpha():
        print(char)
