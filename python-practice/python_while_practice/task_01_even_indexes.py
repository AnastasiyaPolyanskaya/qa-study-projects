### Task 01 - Элементы списка с чётными индексами
**Условие:**  
Вывести элементы списка с индексами `0, 2, 4, ...`.

```python
numbers = list(map(int, input().split()))

index = 0
while index < len(numbers):
    print(numbers[index])
    index += 2
