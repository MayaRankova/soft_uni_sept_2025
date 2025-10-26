# Входни данни
days = int(input())
total_food = float(input())

total_dog_eaten = 0
total_cat_eaten = 0
total_biscuits = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_eaten += dog_food
    total_cat_eaten += cat_food

    total_day_eaten = dog_food + cat_food

    # Всеки трети ден получават бисквитки – 10% от изядената храна за деня
    if day % 3 == 0:
        biscuits = total_day_eaten * 0.10
        total_biscuits += biscuits

total_eaten_food = total_dog_eaten + total_cat_eaten

# Изчисления за процентите
percent_eaten = (total_eaten_food / total_food) * 100
percent_dog = (total_dog_eaten / total_eaten_food) * 100
percent_cat = (total_cat_eaten / total_eaten_food) * 100

# Изход
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")
