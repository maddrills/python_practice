import random

# random int
randNumber = random.randint(1, 10)
print(randNumber)


# random without random int gets q random number from 1 to 10
randomNormal = int(random.random() * 10) + 1
print(randomNormal)

# random without random int gets q random number from 1 to 5
randomNormal = int(random.random() * 5) + 1
print(randomNormal)


# random float to the 2 decimal
randFloat = int(random.random() * 1000) / 100
print(randFloat)

