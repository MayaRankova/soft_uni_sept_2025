# Четем стойността на ваучера
voucher = int(input())

tickets_count = 0
other_count = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    # Определяме цената на покупката
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])  # билет
    else:
        price = ord(purchase[0])  # друг вид покупка

    # Проверяваме дали можем да купим
    if price > voucher:
        break

    voucher -= price

    # Увеличаваме брояча според типа
    if len(purchase) > 8:
        tickets_count += 1
    else:
        other_count += 1

# Отпечатваме резултата
print(tickets_count)
print(other_count)
