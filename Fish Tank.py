lenght = int(input())
width = int(input())
height = int(input())
percentage = float(input())


volume_cm3 = lenght * width * height


volume_litters = volume_cm3 / 1000

usable_litters = volume_litters * (1 - percentage / 100)
print(usable_litters)
