## Task 10 - Принтеры с разрешением > 600 dpi

Найти модели и цены лазерных принтеров, у которых разрешение превышает **600 dpi**.

```sql
SELECT model,
       price
FROM Printer
WHERE type = 'Laser'
  AND resolution > 600;
