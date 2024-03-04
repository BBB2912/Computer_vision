from turtle import Turtle


PADDLE_ONE=(-650,0)
PADDLE_TWO=(650,0)
MOVEMENT=20

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=10)
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.goto(pos)

    def up(self):
        y_cor=self.ycor()+20
        self.goto(self.xcor(),y_cor)

    def down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)