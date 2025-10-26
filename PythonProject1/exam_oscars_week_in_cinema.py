# Четем входа
film = input()
hall_type = input()
tickets_sold = int(input())

# Цени за билетите по филми и вид на зала
prices = {
    "A Star Is Born": {"normal": 7.50, "luxury": 10.50, "ultra luxury": 13.50},
    "Bohemian Rhapsody": {"normal": 7.35, "luxury": 9.45, "ultra luxury": 12.75},
    "Green Book": {"normal": 8.15, "luxury": 10.25, "ultra luxury": 13.25},
    "The Favourite": {"normal": 8.75, "luxury": 11.55, "ultra luxury": 13.95}
}

# Изчисляваме приходите
income = tickets_sold * prices[film][hall_type]

# Отпечатваме резултата, форматиран до 2 знака след десетичната запетая
print(f"{film} -> {income:.2f} lv.")

