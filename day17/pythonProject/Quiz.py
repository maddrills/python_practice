question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
        "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Quiz:

    def __init__(self, question):
        self.question = question


    def questionDispay(self):
        question = ""
        answer = ""

        for qAndA in self.question:
            option1 = input("press Q to quit or Give your answer True Or False")
            if option1.lower() == "q":
                break
            else:
                question = qAndA["text"]
                answer = qAndA["answer"]
                print(f"Question is {question}")
                if option1 == "True" or option1 == "False":
                    if option1 == answer:
                        print("Good Your right")
                    else:
                        print("False")
                else:
                    continue


# py initialisation of class
matsQuiz = Quiz(question_data)

matsQuiz.questionDispay()
