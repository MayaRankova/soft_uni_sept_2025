# Вход: такса за една година
annual_fee = int(input(""))

# Цени по условие:
shoes_price = annual_fee * 0.60           # 40% по-малко от таксата
clothes_price = shoes_price * 0.80        # 20% по-евтино от кецовете
ball_price = clothes_price / 4            # 1/4 от цената на екипа
accessories_price = ball_price / 5        # 1/5 от цената на топката

# Обща цена:
total_cost = (annual_fee + shoes_price + clothes_price + ball_price + accessories_price)

print(f"{total_cost:.2f} лв.")
