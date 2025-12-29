## Task 11 - Проверка строки на палиндром (цикл `while`)

**Условие:**

На вход принимается **одно значение в виде строки**.

С помощью цикла `while` необходимо проверить, **является ли введённая строка палиндромом**  
(строка читается одинаково **с начала и с конца**).

Если строка является палиндромом — вывести `Good`,  
если не является — вывести `Bad`.

---
### Решение

```python
s = input()

left = 0
right = len(s) - 1
is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Good")
else:
    print("Bad")
yaml
Копировать код
