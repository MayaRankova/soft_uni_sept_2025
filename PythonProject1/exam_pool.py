# Входни данни
budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_extra = int(input())

# Проверка за отстъпка при повече от 7 нощувки
if nights > 7:
    price_per_night *= 0.95  # Намаляваме цената с 5%

# Изчисляваме общата сума за нощувки
total_nights_cost = nights * price_per_night

# Изчисляваме допълнителните разходи (процент от бюджета)
extra_costs = budget * (percent_extra / 100)

# Обща нужда за почивката
total_cost = total_nights_cost + extra_costs

# Проверка дали бюджетът е достатъчен
if budget >= total_cost:
    money_left = budget - total_cost
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_needed = total_cost - budget
    print(f"{money_needed:.2f} leva needed.")
