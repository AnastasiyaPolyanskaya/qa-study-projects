## Task 03 - Подсчёт количества символов в строке

**Условие:**  
Посчитать, сколько раз символ встречается в строке.

```python

a = input()
b = input()

count = 0
for char in a:
    if char == b:
        count += 1

print(count)
