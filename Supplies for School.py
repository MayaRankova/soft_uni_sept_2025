
pens_count = int(input())
markers_count = int(input())
cleaner_litters = int(input())
discount_percent = int(input())

# prices
pens_price = 5.80
markers_price = 7.20
cleaner_price = 1.2

# total_price
total_price = (pens_count * pens_price) + (markers_count * markers_price) + (cleaner_litters * cleaner_price)

discount = total_price * (discount_percent / 100)
final_price = total_price - discount
print(final_price)

