## task_3_expensive_laptops.sql

### Задача 3: Дорогие ноутбуки
Найти номер модели, объём памяти и размер экрана ноутбуков, цена которых превышает 1000 долларов.

### SQL-запрос:

```sql
SELECT model,
       ram,
       screen
FROM Laptop
WHERE price > 1000;
