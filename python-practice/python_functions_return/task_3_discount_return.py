# Задача 3 - Расчёт цены со скидкой

def apply_discount(price, discount_percent):
    """
    Возвращает цену товара со скидкой.
    discount_percent — величина скидки в процентах.
    """
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    return final_price


price = 3500
discount = 15

new_price = apply_discount(price, discount)

print("Исходная цена:", price)
print("Скидка:", discount, "%")
print("Цена со скидкой:", new_price)
