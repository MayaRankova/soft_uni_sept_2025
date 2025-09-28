import math

record_seconds = float(input())
distance_meters = float(input())
time_per_meter = float(input())


ivan_time = distance_meters * time_per_meter


delays = math.floor(distance_meters / 15)
ivan_time += delays * 12.5


if ivan_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    difference = ivan_time - record_seconds
    print(f"No, he failed! He was {difference:.2f} seconds slower.")

