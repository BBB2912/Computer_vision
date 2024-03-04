from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(pos)
        self.score = 0
        self.write_board()
        self.hideturtle()

    def write_board(self):
        self.write(f'{self.score}', align='center', font=('Courier', 100, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_board()
