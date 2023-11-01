money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0  # Зададим по умолчанию количество месяцев равное нулю
while True:
    total_savings = money_capital + salary  # Полный наш бюджет складывается из зарплаты и подушки
    if spend <= total_savings:
        minos = salary - spend  # Разницы в доходах и расходах
        money_capital += minos  # Берем недостающие деньги из подушки
        spend *= increase + 1  # Задаем ежемесячный рост цен
    else:
        break
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
