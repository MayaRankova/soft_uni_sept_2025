excursion_price = float(input())
puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

total_order_price = ((puzzle_price * puzzle) +
                     (dolls_price * dolls) +
                     (bears_price * bears) +
                     (minions_price * minions) +
                     (trucks_price * trucks))

total_number = puzzle + dolls + bears + minions + trucks

if total_number >= 50 :
    total_order_price *= 0.75

rent = total_order_price * 0.10
profit = total_order_price - rent

difference = abs(profit - excursion_price)

if profit >= excursion_price:
    print(f'Yes! {difference:.2f} lv left.')
else :
    print(f'Not enough money! {difference:.2f} lv needed.')
