# Четене на входни данни
pocket_money = float(input())      # джобни на ден
earnings_per_day = float(input())  # печалба от продажби на ден
expenses = float(input())          # разходи за периода
gift_price = float(input())        # цена на подаръка

# Изчисляване на общата събрана сума
total_saved = 5 * (pocket_money + earnings_per_day) - expenses

# Проверка дали може да купи подаръка
if total_saved >= gift_price:
    print(f"Profit: {total_saved:.2f} BGN, the gift has been purchased.")
else:
    needed = gift_price - total_saved
    print(f"Insufficient money: {needed:.2f} BGN.")
