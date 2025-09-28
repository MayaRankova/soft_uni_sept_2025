budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())


video_card_price = 250
total_video_cards = video_cards * video_card_price

processor_price = total_video_cards * 0.35
ram_price = total_video_cards * 0.10

total_processors = processors * processor_price
total_ram = ram * ram_price

total_sum = total_video_cards + total_processors + total_ram


if video_cards > processors:
    total_sum *= 0.85


difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
