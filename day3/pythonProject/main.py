# if else

# odd even
# while(1) also works
enteredNumber = 0
while True:
    try:
        enteredNumber = int(input("Input Number "))
    except:
        print("Invalid Input Type")
        continue
    break

print(f"your entered number is {enteredNumber}")


if(enteredNumber % 2 == 0):
    print("even")
else:
    print("odd")




# if elif else
if(enteredNumber <= 5 and enteredNumber > 0):
    print("greater than 5 but grater than 0")
elif(enteredNumber > 5):
    print("grater than 5")
else:
    print("less than 0")

print(not 2000 % 100);




year = int(input("Enter Year "))
status = False

# leep year
if(not year % 4):
    status = True
if(not year % 100):
    status = False
if(not year % 400):
    status = True

print(status)

#5
print(len("hello"))

#2 o(n)
print("hello".count("l"))