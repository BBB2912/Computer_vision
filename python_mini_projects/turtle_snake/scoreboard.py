from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(-100, 250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.score} High score:{self.high_score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()
    def read_high_score(self):
        with open('high_score.txt','r') as high_score_file:
            score=int(high_score_file.read())
        return score

    def write_high_score(self):
        with open('high_score.txt','w') as write_score:
            write_score.write(str(self.high_score))
