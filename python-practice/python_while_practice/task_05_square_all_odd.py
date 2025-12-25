## Task 05 - Все нечётные числа в квадрате

**Условие:**  
Вывести квадрат каждого нечётного числа из списка.

```python

numbers = list(map(int, input().split()))

index = 0
while index < len(numbers):
    if numbers[index] % 2 != 0:
        print(numbers[index] ** 2)
    index += 1
