actor_name = input()
academy_points = float(input())
n = int(input())

total = academy_points
threshold = 1250.5

for i in range(n):
    judge_name = input()
    judge_points = float(input())

    added = len(judge_name) * judge_points / 2
    total += added

    if total > threshold:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total:.1f}!")
        break
else:
    need = threshold - total
    print(f"Sorry, {actor_name} you need {need:.1f} more!")
