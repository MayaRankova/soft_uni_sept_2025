
flower_type = input()
count = int(input())
budget = int(input())
price = 0

if flower_type == 'Roses':
    price = 5 * count
    if count > 80:
       price *= 0.90

elif flower_type == 'Dahlias':
    price = 3.80 * count
    if count > 90:
        price *= 0.85

elif flower_type == 'Tulips':
    price = 2.80 * count
    if count > 80:
        price *= 0.85

elif flower_type == 'Narcissus':
    price = 3 * count
    if count < 120:
        price += price * 0.15

elif flower_type == 'Gladiolus':
    price = 2.5 * count
    if count < 80:
        price += price * 0.20

difference_between_price_and_budget = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count} {flower_type}"
          f" and {difference_between_price_and_budget:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference_between_price_and_budget:.2f} leva more.")