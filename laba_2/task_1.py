money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 1

while money_capital >= 0 and spend <= money_capital + salary:
    if months > 0:
        spend *= (1 + increase)
        money_capital -= spend - salary
        months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months-1)