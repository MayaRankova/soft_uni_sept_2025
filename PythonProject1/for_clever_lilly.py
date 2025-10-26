lili_age = int(input())
x = float(input())
price_for_toy = int(input())

money_saved = 0
money_gift = 10
toys_counter = 0

for age in range(1, lili_age + 1):
    if age % 2 == 0:
        money_saved += money_gift
        money_gift += 10
        money_saved -= 1
    else:
        toys_counter += 1


money_saved += toys_counter * price_for_toy


if money_saved >= x:
    print(f"Yes! {money_saved - x:.2f}")
else:
    print(f"No! {x - money_saved:.2f}")
