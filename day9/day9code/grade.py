studentMarks = {
    "Kamal Kahn" : 50,
    "James Bond" : 95,
    "Jacky Brown" : 75,
    "Will Smith" : 82
}

finalGrade = {}

def studentGrader(marks):

    for key in marks:
        if studentMarks[key] < 70:
            finalGrade[key] = "Fail"
        elif studentMarks[key] < 80:
            finalGrade[key] = "Acceptable"
        elif studentMarks[key] < 90:
            finalGrade[key] = "Exceed expectation"
        else:
            finalGrade[key] = "Ultimate"



if __name__ == "__main__":
    print("main call")

    studentGrader(studentMarks)

    print(finalGrade)

