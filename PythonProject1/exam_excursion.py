number_people = int(input())
number_nights = int(input())
number_transport = int(input())
number_ticket = int(input())

price_nights = 20
price_transport = 1.60
price_tickets = 6

sum_per_person = (number_nights * price_nights) + (number_transport * price_transport) + (number_ticket * price_tickets)

total_sum = sum_per_person * number_people
total_sum_expenses = total_sum * 1.25  # adding 25% expenses

print(f"{total_sum_expenses:.2f}")
