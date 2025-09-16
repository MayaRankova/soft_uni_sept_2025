

# input
chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())



# prices
chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15

discount_percent = 2.50


# calculations
total_price = (( chicken_menu * chicken_menu_price) + ( fish_menu * fish_menu_price) + ( vegan_menu * vegan_menu_price))
discount = total_price * (discount_percent / 100)
dessert_price = (total_price * 0.2)
delivery_price = 2.5

total_price_order = total_price + dessert_price + delivery_price
print(total_price_order)
