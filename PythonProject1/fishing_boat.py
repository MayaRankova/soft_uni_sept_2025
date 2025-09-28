

budget = int(input())
season = input()
fishers = int(input())

rent = 0


if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fishers <= 6:
    rent *= 0.90
elif 7 <= fishers <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if fishers % 2 == 0 and season != 'Autumn':
    rent *= 0.95

diff = abs(budget - rent)
if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")