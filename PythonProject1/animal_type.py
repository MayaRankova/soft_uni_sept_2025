animal = input()
animal_type = ""

if animal == "dog":
    animal_type = "mammal"
elif animal == "crocodile":
    animal_type = "reptile"
elif animal == "tortoise":
    animal_type = "reptile"
elif animal == "snake":
    animal_type = "reptile"
else:
    animal_type = "unknown"

print(animal_type)