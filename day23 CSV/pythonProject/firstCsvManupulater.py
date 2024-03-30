import csv
import pandas
def openCsvAndDisplayByLineArray():
    with open("./CSV/weather_data.csv", mode="r") as csvData:
        # print(csvData.read())
        # data = csvData.read().split("\n")
        # print(data)

        #or
        data2 = csvData.readlines()
        print(data2)

def csvLibUsed():
    temp = []
    with open("./CSV/weather_data.csv", mode="r") as csvData:
        # the csv reader coverts the csv file into an iterable that each holds an array split by,
        data = csv.reader(csvData)

        for values in data:
            print(values)

            try:
                temp.append(int(values[1]))
            except:
                continue

    print(temp)

def padaDataView():
    data = pandas.read_csv("./CSV/weather_data.csv")
    if 0:
        # it will be printed in a nice tabular view
        print(data)

        #if you only want the wedther data
        print(data["temp"])

        # the highest temp
        print(data["temp"].max())

        # row has the highest temp in  the week
        # need a binary operator
        # when true then it will display the row its true on
        print(data[data["temp"] == data["temp"].max()])
        #panda treets a series heading as an object so you can also do the above as
        print(data[data.temp == data.temp.max()])

    #geting the temp out of the a row
    monday = data[data.day == "Monday"]
    # 0    12
    print(monday.temp)
    # 12
    print(monday.temp[0])


def makePandaCsvData():
    # {'name': ['mat', 'vio', 'george'], 'marks': [45, 49, 50]}
    dataObject = {
        "name":["mat","vio","george"],
        "marks":[45,49,50],
    }
    # use the DataFrame class
    # it will have a nicely formatted dataframe
    pandaData = pandas.DataFrame(dataObject)
    print(pandaData)





if __name__ == "__main__":

    #csvLibUsed()
    #padaDataView()
    makePandaCsvData()
    print("Main.exe")
