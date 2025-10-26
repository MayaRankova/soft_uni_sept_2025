# Четене на желаната печалба
desired_profit = float(input())
current_profit = 0.0

while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        break
    cocktail_count = int(input())

    # Цената на един коктейл е дължината на името му
    price_per_cocktail = len(cocktail_name)
    total_order_price = price_per_cocktail * cocktail_count

    # Ако цената на поръчката е нечетно число, прилагаме 25% отстъпка
    if total_order_price % 2 != 0:
        total_order_price *= 0.75

    # Добавяме към текущата печалба
    current_profit += total_order_price

    # Проверка дали е достигната желаната печалба
    if current_profit >= desired_profit:
        print("Target acquired.")
        print(f"Club income - {current_profit:.2f} leva.")
        exit()

# Ако е получена команда "Party!" и не е достигната печалбата
remaining = desired_profit - current_profit
print(f"We need {remaining:.2f} leva more.")
print(f"Club income - {current_profit:.2f} leva.")
