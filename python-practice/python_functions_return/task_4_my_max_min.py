# Задача 4 - Собственные реализации max и min

def my_max(numbers):
    """Возвращает максимальное число из списка."""
    if not numbers:
        return None
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    return current_max


def my_min(numbers):
    """Возвращает минимальное число из списка."""
    if not numbers:
        return None
    current_min = numbers[0]
    for num in numbers[1:]:
        if num < current_min:
            current_min = num
    return current_min


values = [12, 3, 45, -7, 18]

print("Список:", values)
print("Максимум (my_max):", my_max(values))
print("Минимум (my_min):", my_min(values))
