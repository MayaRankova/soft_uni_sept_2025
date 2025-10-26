# Четене на броя дни
N = int(input())

total_liters = 0.0
total_alcohol = 0.0

for _ in range(N):
    liters = float(input())
    degrees = float(input())

    total_liters += liters
    total_alcohol += liters * degrees

# Изчисляване на средния градус
average_degrees = total_alcohol / total_liters

# Извеждане на резултатите
print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

# Оценка на качеството според градусите
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:  # average_degrees > 42
    print("Dilution with distilled water!")
