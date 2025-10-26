# Четем входните данни
drink = input()       # "Espresso", "Cappuccino" или "Tea"
sugar = input()       # "Without", "Normal" или "Extra"
count = int(input())  # брой напитки

# Определяме базовата цена според напитката и захарта
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1.00
    elif sugar == "Extra":
        price = 1.20

elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1.00
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60

elif drink == "Tea":
    if sugar == "Without":
        price = 0.50
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

# Изчисляваме междинната цена
total = price * count

# 1) Отстъпка за "Without" – 35%
if sugar == "Without":
    total *= 0.65

# 2) Отстъпка за "Espresso" при >= 5 броя – 25%
if drink == "Espresso" and count >= 5:
    total *= 0.75

# 3) Отстъпка при обща сума > 15 лв – 20%
if total > 15:
    total *= 0.80

# Отпечатваме резултата
print(f"You bought {count} cups of {drink} for {total:.2f} lv.")
