import math


figure = input()
if figure == 'square':
    a = float(input())
    area = a * a
elif figure == 'rectangle':
        a = float(input())
        b = float(input())
        area = a * b
elif figure == 'circle':
    a = float(input())
    area = math.pi * math.pow(a ,2)
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = (a * h) /2

print(str(area))