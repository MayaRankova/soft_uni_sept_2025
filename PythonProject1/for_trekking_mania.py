
n = int(input())


musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0


for _ in range(n):
    people = int(input())

    if people <= 5:
        musala += people
    elif people <= 12:
        monblan += people
    elif people <= 25:
        kilimandjaro += people
    elif people <= 40:
        k2 += people
    else:
        everest += people


total = musala + monblan + kilimandjaro + k2 + everest

print(f"{musala / total * 100:.2f}%")
print(f"{monblan / total * 100:.2f}%")
print(f"{kilimandjaro / total * 100:.2f}%")
print(f"{k2 / total * 100:.2f}%")
print(f"{everest / total * 100:.2f}%")
