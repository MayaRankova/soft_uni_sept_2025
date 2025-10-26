# Четене на входни данни
budget = float(input())          # Бюджет за филма
extras_count = int(input())      # Брой на статистите
clothing_price = float(input())  # Цена за облекло на един статист

# Изчисляване на стойността на декора (10% от бюджета)
decor_cost = budget * 0.10

# Изчисляване на общата цена за облеклата
clothing_total = extras_count * clothing_price

# Ако има повече от 150 статиста, се ползва 10% отстъпка за облеклата
if extras_count > 150:
    clothing_total *= 0.90

# Общи разходи за декор и облекло
total_costs = decor_cost + clothing_total

# Проверка дали бюджетът е достатъчен
if total_costs > budget:
    needed_money = total_costs - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    money_left = budget - total_costs
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
