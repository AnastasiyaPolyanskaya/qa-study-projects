-- Basic SQL Queries
-- Учебные запросы для тренировки SELECT, WHERE, ORDER BY, LIMIT

-- 1. Получить все записи из таблицы products
SELECT *
FROM products;

-- 2. Получить название и цену товара
SELECT name, price
FROM products;

-- 3. Найти товары дороже 1000 рублей
SELECT *
FROM products
WHERE price > 1000;

-- 4. Выбрать первые 5 товаров с сортировкой по цене (по возрастанию)
SELECT *
FROM products
ORDER BY price ASC
LIMIT 5;

-- 5. Найти товары определённой категории
SELECT *
FROM products
WHERE category = 'electronics';

-- 6. Поиск товаров с ценой в диапазоне
SELECT *
FROM products
WHERE price BETWEEN 500 AND 1500;

-- 7. Получить уникальные категории товаров
SELECT DISTINCT category
FROM products;
