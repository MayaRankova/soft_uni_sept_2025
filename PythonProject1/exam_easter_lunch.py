# Входни данни
eggs_one = int(input())
eggs_two = int(input())

# Четем команди, докато не получим "End"
while True:
    command = input()

    if command == "End":
        # Ако командата е "End" – играта приключва
        print(f"Player one has {eggs_one} eggs left.")
        print(f"Player two has {eggs_two} eggs left.")
        break

    if command == "one":
        eggs_two -= 1
    elif command == "two":
        eggs_one -= 1

    # Проверяваме дали някой е останал без яйца
    if eggs_one == 0:
        print(f"Player one is out of eggs. Player two has {eggs_two} eggs left.")
        break
    elif eggs_two == 0:
        print(f"Player two is out of eggs. Player one has {eggs_one} eggs left.")
        break
