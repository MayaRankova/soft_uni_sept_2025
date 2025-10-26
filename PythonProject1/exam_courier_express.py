# Четене на входните данни
weight = float(input())
service_type = input()
distance = int(input())

# Цени за стандартна услуга (лв. на км)
if weight < 1:
    price_per_km = 0.03
    express_percentage = 0.8
elif weight < 10:
    price_per_km = 0.05
    express_percentage = 0.4
elif weight < 40:
    price_per_km = 0.10
    express_percentage = 0.05
elif weight < 90:
    price_per_km = 0.15
    express_percentage = 0.02
else:  # weight <= 150
    price_per_km = 0.20
    express_percentage = 0.01

# Изчисляване на стандартната цена
standard_price = price_per_km * distance

# Ако е express, добавяме надценка
if service_type == "express":
    express_price = standard_price + (express_percentage * weight * price_per_km * distance)
    total_price = express_price
else:
    total_price = standard_price

# Отпечатване на резултата със зададените формати
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")
