income = float(input("Введите доход: "))
expense = float(input("Введите расход: "))
tax_rate = float(input("Введите налоговую ставку (%): "))

profit_before_tax = income - expense
tax_amount = profit_before_tax * (tax_rate / 100)
profit_after_tax = profit_before_tax - tax_amount

print("Чистая прибыль:", profit_after_tax)
