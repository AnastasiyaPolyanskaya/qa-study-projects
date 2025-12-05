# Задача 2 - Среднее арифметическое списка чисел

def average(numbers):
    """Возвращает среднее арифметическое списка чисел."""
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)


values = [10, 15, 20, 5]

avg = average(values)

print("Список чисел:", values)
print("Среднее значение:", avg)
