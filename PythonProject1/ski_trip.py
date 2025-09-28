days_for_stay = int(input())
room_type = input()
rating = input()

nights = days_for_stay - 1

price_per_night = 0

if room_type == 'room for one person':
    price_per_night = 18
elif room_type == 'apartment':
    price_per_night = 25
elif room_type == 'president apartment':
    price_per_night = 35

total_price = nights * price_per_night

if room_type == 'apartment':
    if days_for_stay < 10:
        total_price *= 0.70
    elif 10 <= days_for_stay <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50

elif room_type == 'president apartment':
    if days_for_stay < 10:
        total_price *= 0.90
    elif 10 <= days_for_stay <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80

if rating == 'positive':
    total_price *= 1.25
else:
    total_price -= total_price * 0.10

print(f'{total_price:.2f}')