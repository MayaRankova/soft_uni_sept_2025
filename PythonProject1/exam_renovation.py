import math

# Вход
height = int(input())
width = int(input())
percent_not_painted = int(input())

# Площ на стените
wall_area = height * width
total_area = wall_area * 4

# Площ за боядисване
paintable_area = total_area * (1 - percent_not_painted / 100)
paintable_area = math.ceil(paintable_area)

while True:
    line = input()
    if line == "Tired!":
        print(f"{paintable_area} quadratic m left.")
        break

    liters = int(line)
    paintable_area -= liters

    if paintable_area <= 0:
        if paintable_area < 0:
            print(f"All walls are painted and you have {abs(paintable_area)} l paint left!")
        else:
            print("All walls are painted! Great job, Pesho!")
        break
