## Task 04 - Вывести числа больше 7

**Условие:**  
Вывести все элементы списка, которые больше 7.

```python

numbers = list(map(int, input().split()))

index = 0
while index < len(numbers):
    if numbers[index] > 7:
        print(numbers[index])
    index += 1
