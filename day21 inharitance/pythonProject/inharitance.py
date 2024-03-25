class pomarian:

    def __init__(self):
        self.bark = "loud"

    def dogBark(self):
        print(self.bark)


class squine(pomarian):
    def __init__(self):
        # not compulsory if no parameters
        super().__init__()
        # this will override the super variable
        self.bark = "Boow Boow"

    def dogBark(self):
        print("Squine")
        # the override can be seen here
        super().dogBark()
        print(self.bark)


pom = pomarian()
pom.dogBark()


sqn = squine()
sqn.dogBark()

# loud
# Squine
# loud
# loud