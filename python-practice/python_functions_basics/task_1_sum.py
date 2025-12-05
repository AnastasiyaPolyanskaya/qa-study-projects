# Задача 1 - Функция суммы двух чисел

def sum_numbers(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


# Пример использования:
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

result = sum_numbers(num1, num2)
print("Сумма чисел:", result)
