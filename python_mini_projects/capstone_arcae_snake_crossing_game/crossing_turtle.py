from turtle import Turtle

INITIAL_POS = (0, -350)


class TURTLE(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.goto(INITIAL_POS)

    def up(self):
        self.forward(10)

    def turtle_reposition(self):
        self.goto(INITIAL_POS)
