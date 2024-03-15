import random
# a range of values
# 0123456789
import random

for number in range(0, 10):
    print(number, end ='')



print()
# third arg is skip 0369
for number in range(0, 10, 3):
    print(number, end='')



print()

number = int(input("Enter The upper Range"))
sum = 0
for i in range(0, number):
    #check for divisibility
    if(not i % 2):
        #then it is even
        sum += i

print(sum)



for i in range(1 , 100):
    if not (i % 3) and not (i % 5):
        print(f"Fizz Buzz {i}")
        continue
    elif (not i % 3):
        print(f"Fizz {i}")
        continue
    elif (not i % 5):
        print(f"Buzz {i}")
        continue
    print(i)

