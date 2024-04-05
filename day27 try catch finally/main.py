def tryCatchFunction():
    try:
        file = open("a_file.txt")
        a_dictionary = {"key": "value"}
        print(a_dictionary["randomKey"])
    except FileNotFoundError:
        file = open("a_file.txt","w")
        file.write("Something")
    except KeyError as error_message:
        print(f"Key Error {error_message}")
    else:
        content = file.read()
        print(content)
    finally:
        file.close()
        print("file was close.")


def rasingException():
    """ rais an exception that throws a new exception """
    raise TypeError("An error Occurred")



if __name__ == "__main__":
    tryCatchFunction()
    print("main call")