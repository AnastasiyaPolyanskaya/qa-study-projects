## Task 07 - Удвоение каждого элемента списка

**Условие:**  
Изменить список, умножив каждый элемент на 2.

```python

numbers = list(map(int, input().split()))

index = 0
while index < len(numbers):
    numbers[index] *= 2
    index += 1

print(numbers)
