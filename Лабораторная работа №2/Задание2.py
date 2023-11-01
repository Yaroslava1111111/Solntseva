salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
savings = 0  # Изначально подушка безопасности ноль
for monthly_expenses in range(1, months + 1):
    minos = spend - salary  # Разница в доходах и расходах
    savings += minos  # Пополняем подушку безопасности на ежемесячную разницу доходов и расходов
    spend *= increase + 1  # Учитываем ежемесячный рост цен

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(savings, 2))
