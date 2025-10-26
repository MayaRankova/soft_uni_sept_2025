# Входни данни
budget = float(input())
destination = input()
season = input()
days = int(input())

# Цени за един ден според дестинацията и сезона
price_per_day = 0

if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    elif season == "Summer":
        price_per_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    elif season == "Summer":
        price_per_day = 12500
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    elif season == "Summer":
        price_per_day = 20250

# Изчисляваме общата цена
total_price = price_per_day * days

# Проверка за отстъпки/оцскъпявания
if destination == "Dubai":
    total_price *= 0.70   # 30% отстъпка
elif destination == "Sofia":
    total_price *= 1.25   # 25% оскъпяване

# Проверяваме дали бюджетът е достатъчен
if budget >= total_price:
    leftover = budget - total_price
    print(f"The budget for the movie is enough! We have {leftover:.2f} leva left!")
else:
    needed = total_price - budget
    print(f"The director needs {needed:.2f} leva more!")
