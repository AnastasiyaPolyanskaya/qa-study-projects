## Task 06 - Нечётные числа в квадрате до первого чётного

**Условие:**  
Выводить квадраты чисел, пока они идут нечётные.
Остановка на первом чётном числе.

```python

numbers = list(map(int, input().split()))

index = 0
while index < len(numbers) and numbers[index] % 2 != 0:
    print(numbers[index] ** 2)
    index += 1
