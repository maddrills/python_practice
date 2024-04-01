#you can pass in an optional argument with its lable which
# which will be interpraated as a dictionary in the function body


def calculate(**kwargs):
    print(kwargs)

def calculater1(n, **calckWith):
    n += calckWith["one"]
    n *= calckWith["two"]

    print(n)




# {'add': 3, 'multiply': '4'}
calculate(add=3, multiply = "4")
# 1254
calculater1(16, one=22, two=33)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="VCmotors", model="GT-R")

# VCmotors
print(my_car.make)