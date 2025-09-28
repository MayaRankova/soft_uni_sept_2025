from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

free_time = break_duration - lunch_time - rest_time

difference = abs(free_time - episode_duration)
if free_time >= episode_duration:
    print(f'You have enough time to watch {series_name} and'
    f' left with {ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(difference)} more minutes.")


