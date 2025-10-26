winner_name = ""
winner_score = 0
players_scores = []

while True:
    name = input()
    if name == "Stop":
        break

    score = 0
    for ch in name:
        num = int(input())
        if num == ord(ch):
            score += 10
        else:
            score += 2

    players_scores.append((name, score))

# Определяне на победителя
# Критерий: най-висок резултат, при равенство печели вторият, който го е достигнал
max_score = -1
winner = ""
for name, score in players_scores:
    if score > max_score:
        max_score = score
        winner = name
    elif score == max_score:
        winner = name  # вторият, който достига максимума, става победител

print(f"The winner is {winner} with {max_score} points!")
