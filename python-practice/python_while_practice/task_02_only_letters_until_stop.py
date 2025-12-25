## Task 02 - Печать элементов, пока они содержат только буквы

**Условие:**  
Цикл работает, пока текущий элемент списка состоит только из букв.

```python
films = input().split()

index = 0
while index < len(films) and films[index].isalpha():
    print(films[index])
    index += 1
