# Входни данни
price_racket = float(input())  # цена на една ракета
count_rackets = int(input())   # брой ракети
count_shoes = int(input())     # брой маратонки

# Изчисления
price_shoes = price_racket / 6  # 1 чифт маратонки = 1/6 от цената на ракетата

total_rackets = count_rackets * price_racket
total_shoes = count_shoes * price_shoes

# Останала екипировка = 20% от (общата цена на ракетите и маратонките)
other_equipment = 0.2 * (total_rackets + total_shoes)

# Обща цена
total_price = total_rackets + total_shoes + other_equipment

# Джокович плаща 1/8 от общата цена
djokovic_part = total_price / 8
sponsors_part = total_price * 7 / 8

# Закръгляне
djokovic_part_floor = int(djokovic_part)  # към по-малкото цяло число
sponsors_part_ceil = int(-(-sponsors_part // 1))  # към по-голямото цяло число (ceil без import)

# Изход
print(f"Price to be paid by Djokovic {djokovic_part_floor}")
print(f"Price to be paid by sponsors {sponsors_part_ceil}")
