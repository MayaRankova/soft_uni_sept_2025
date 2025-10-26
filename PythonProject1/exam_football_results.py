# Четем резултатите от трите мача
match1 = input()
match2 = input()
match3 = input()

# Списък с резултатите за по-лесна обработка
matches = [match1, match2, match3]

# Броячи
wins = 0
losses = 0
draws = 0

# Обхождаме всеки резултат
for match in matches:
    home, away = match.split(":")  # Разделяме резултата на домакин и гост
    home = int(home)
    away = int(away)

    if home > away:
        wins += 1
    elif home < away:
        losses += 1
    else:
        draws += 1

# Извеждаме резултата
print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
