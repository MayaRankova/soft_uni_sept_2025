budget = float(input())
fuel_liters = float(input())
day = input()


fuel_price = 2.10
guide_price = 100


total_price = fuel_liters * fuel_price + guide_price


if day == "Saturday":
    total_price *= 0.90   # 10% отстъпка
elif day == "Sunday":
    total_price *= 0.80   # 20% отстъпка


difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Safari time! Money left: {difference:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
