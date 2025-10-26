# Четем първоначалния брой пакети
sea_packages = int(input())
mountain_packages = int(input())

# Цени на пакетите
PRICE_SEA = 680
PRICE_MOUNTAIN = 499

profit = 0

while True:
    command = input()

    if command == "Stop":
        break

    if command == "sea":
        if sea_packages > 0:
            profit += PRICE_SEA
            sea_packages -= 1
    elif command == "mountain":
        if mountain_packages > 0:
            profit += PRICE_MOUNTAIN
            mountain_packages -= 1

    # Проверка дали са продадени всички пакети
    if sea_packages == 0 and mountain_packages == 0:
        print("Good job! Everything is sold.")
        break

# Отпечатваме печалбата
print(f"Profit: {profit} leva.")
