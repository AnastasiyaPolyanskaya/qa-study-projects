### Задача 2: Производители принтеров
Найти всех производителей принтеров.  
Вывести только уникальные значения столбца maker.

### SQL-запрос:

```sql
SELECT DISTINCT maker
FROM Product
WHERE type = 'Printer';
