from turtle import Turtle
class Food(Turtle):

    # constructor
    def __init__(self):
        super().__init__()
        print("Self Reference")
        # below are turtle class inherited class
        self.shape()
        self.shapesize(stretch_len=0.5, stretch_wide=0.5)
        self.color("blue")