# входни данни
annual_fee = int(input())

# изчисления
sneakers = annual_fee * 0.6           # 40% по-малко от таксата
outfit = sneakers * 0.8               # 20% по-евтин от кецовете
ball = outfit / 4                     # 1/4 от цената на екипа
accessories = ball / 5                # 1/5 от цената на топката

# общи разходи
total_cost = annual_fee + sneakers + outfit + ball + accessories

# изход
print(f"{total_cost:.2f}")
