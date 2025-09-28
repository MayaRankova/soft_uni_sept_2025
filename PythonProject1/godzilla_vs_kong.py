budget = float(input())
statists = int(input())
clothes_price = float(input())

# Цена за декор
decor = budget * 0.10
# Обща цена за облекло
total_clothes_price = clothes_price * statists

if statists > 120:
    total_clothes_price *= 0.90     # 10% discount

total_costs = decor + total_clothes_price

if budget >= total_costs:
    money_left = budget - total_costs
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_needed = total_costs - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")