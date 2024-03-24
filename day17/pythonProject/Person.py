# define a class
class Person:

    # make a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #make a field that isent initialised by a constructor
        self.followers = 0


    #rember in classes every method needs to explisitly refer itself as its first parameter
    def newFollower(self, oneMore):
        self.followers = oneMore


# create the object
mathew = Person("Mathew", 25)

print(mathew.name)
print(mathew.age)
print(mathew.followers)

mathew.followers = 1250
print(mathew.followers)

# you can also add an attribute to a class like this also
mathew.passion  = "Gaming"
print(mathew.passion)

# and here you can call the method
mathew.newFollower(500)
print(mathew.followers)