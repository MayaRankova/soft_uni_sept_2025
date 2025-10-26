start = input()
end = input()

for a in range(int(start[0]), int(end[0]) + 1):
    for b in range(int(start[1]), int(end[1]) + 1):
        for c in range(int(start[2]), int(end[2]) + 1):
            for d in range(int(start[3]), int(end[3]) + 1):
                # Проверяваме дали всички цифри са нечетни
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end=" ")
