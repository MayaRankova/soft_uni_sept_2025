hours = int(input())
minutes = int(input())

total_minutes = (hours * 60) + minutes + 15

new_hour = (total_minutes // 60) % 24
new_minute = total_minutes % 60
print(f'{new_hour}:{new_minute:02d}')
