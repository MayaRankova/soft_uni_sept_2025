city = input()
package_type = input()
vip = input()
days = int(input())

# Проверка за валидност на дните
if days < 1:
    print("Days must be positive number!")
    exit()

# Цени по категории
prices = {
    "Bansko": {
        "withEquipment": 100,
        "noEquipment": 80
    },
    "Borovets": {
        "withEquipment": 100,
        "noEquipment": 80
    },
    "Varna": {
        "withBreakfast": 130,
        "noBreakfast": 100
    },
    "Burgas": {
        "withBreakfast": 130,
        "noBreakfast": 100
    }
}

# Отстъпки при VIP
discounts = {
    "withEquipment": 0.10,
    "noEquipment": 0.05,
    "withBreakfast": 0.12,
    "noBreakfast": 0.07
}

# Проверка за валиден град и пакет
if city not in prices or package_type not in prices[city]:
    print("Invalid input!")
    exit()

# При престой над 7 дни – един безплатен ден
if days > 7:
    days -= 1

# Изчисляване на базова цена
price_per_day = prices[city][package_type]

# Приложение на VIP отстъпка (ако има)
if vip == "yes":
    price_per_day -= price_per_day * discounts[package_type]

# Крайна цена
total_price = days * price_per_day

print(f"The price is {total_price:.2f}lv! Have a nice time!")
