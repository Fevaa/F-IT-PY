money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
months = 0

while money_capital >= 0 and spend <= money_capital + salary:
    spend *= 1 + increase
    money_capital -= spend - salary
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
