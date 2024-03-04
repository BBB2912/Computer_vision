from turtle import Turtle


class Boll(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.x_move = 10
        self.y_move = 10
        self.goto(0, 0)
        self.move_speed = 0.1

    def boll_move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def replace_boll(self):
        self.goto(0, 0)
        self.bounce_x()
