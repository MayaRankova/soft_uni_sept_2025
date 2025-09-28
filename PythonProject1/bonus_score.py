num = int(input())

bonusScore = 0.0
if num <= 100:
    bonusScore = 5
elif num > 100 and num < 1000:
    bonusScore = num * 0.2
else:
    bonusScore = num * 0.1
if num % 2 == 0:
    bonusScore = bonusScore +1
if num % 10 == 5:
    bonusScore = bonusScore + 2
print(bonusScore)
print(num + bonusScore)