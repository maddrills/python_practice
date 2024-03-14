import random

stringOfNames = "James, John, Ben"

names = stringOfNames.split(", ")

print(names)

# num = int(random.random() * len(names))

num = random.randint(0, len(names) - 1)

print(num)

print(f"{names[num]} is going to buy the meal today!")






