from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(-300, 300)
        self.level_display()

    def level_display(self):
        self.write(f'Level: {self.level}', align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('..Game Over..', align='center', font=('Courier', 24, 'normal'))

    def update_level(self):
        self.clear()
        self.level += 1
        self.level_display()
