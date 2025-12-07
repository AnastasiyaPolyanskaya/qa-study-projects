## Task 7 - ПК с CD-ROM

Найти номер модели и цену всех ПК, у которых имеется CD-ROM (cd > 0).

```sql
SELECT model,
       price
FROM PC
WHERE cd > 0;
