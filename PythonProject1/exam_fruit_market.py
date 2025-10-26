# входни данни
price_strawberries = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_strawberries = float(input())

# цени на останалите плодове
price_raspberries = price_strawberries / 2
price_oranges = price_raspberries * 0.6
price_bananas = price_raspberries * 0.2

# обща сума
total = (kg_strawberries * price_strawberries +
         kg_raspberries * price_raspberries +
         kg_oranges * price_oranges +
         kg_bananas * price_bananas)

# резултат
print(f"{total:.2f}")
