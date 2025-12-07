## Task 9 - ПК производителя A

Найти модели и цены ПК производителя **A**.

```sql
SELECT PC.model,
       PC.price
FROM Product
JOIN PC ON Product.model = PC.model
WHERE Product.maker = 'A';
