import json

email = "name@gmail.com"
password = "Upse1pl"

new_data = {
    "faceBook" : {
        "email" : email,
        "password" : password
    }
}

try:
    with open("data.json", "w") as data_file:
        # put dataa in
        # takes an optional 3red argument indent = 4 used for redability
        json.dump(new_data, data_file, indent=4)
except:
    print("General error occurred")


# read from json

try:
    with open("data.json", "r") as data_file_read:

        dataa = json.load(data_file_read)
        print(dataa)

except:
    print("General exception occurred")