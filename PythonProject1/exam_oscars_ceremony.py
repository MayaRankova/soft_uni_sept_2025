# Вход: наем за залата
hall_rent = int(input())

# Изчисляване на разходите
statues = hall_rent * 0.7
catering = statues * 0.85
sound = catering / 2

# Общо разходи
total = hall_rent + statues + catering + sound

# Извеждане на резултата с 2 десетични знака
print(f"{total:.2f}")
