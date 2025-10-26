team_name = input()
matches_played = int(input())

if matches_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    wins = 0
    draws = 0
    losses = 0

    for _ in range(matches_played):
        result = input()
        if result == 'W':
            wins += 1
        elif result == 'D':
            draws += 1
        elif result == 'L':
            losses += 1

    total_points = wins * 3 + draws * 1
    win_rate = (wins / matches_played) * 100

    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    print(f"Win rate: {win_rate:.2f}%")
