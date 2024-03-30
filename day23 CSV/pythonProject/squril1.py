import pandas

def squrilData():
    data = pandas.read_csv("./CSV/2018.csv")

    # returns a whole table where the expression is true
    graySquNum = data[data["Primary Fur Color"] == "Gray"].count()[["Primary Fur Color"]]
    graySquCount = graySquNum["Primary Fur Color"]

    cinSquNum = data[data["Primary Fur Color"] == "Cinnamon"].count()[["Primary Fur Color"]]
    cinSquCount = cinSquNum["Primary Fur Color"]

    blacSquNum = data[data["Primary Fur Color"] == "Black"].count()[["Primary Fur Color"]]
    blacSquCount = blacSquNum["Primary Fur Color"]


    squrils = {
        "Color" :["Gray", "Cinnamon", "Black"],
        "Count" : [graySquCount, cinSquCount, blacSquCount]
    }

    print(squrils)

    nicellyFormated = pandas.DataFrame(squrils)

    print(nicellyFormated)

if __name__ == "__main__":
    squrilData()
    print("main exe")