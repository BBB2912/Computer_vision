from turtle import Turtle
import random

CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Crapstones:

    def __init__(self):
        self.crap_stones = []
        self.craps_speed = 0.1

    def add_crap_stone(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 6:
            crap_stone = Turtle('square')
            crap_stone.penup()
            crap_stone.shapesize(stretch_len=3, stretch_wid=1)
            crap_stone.setheading(180)
            crap_stone.color(random.choice(CAR_COLORS))
            x = random.randrange(450, 600, 100)
            y = random.randint(-250, 250)
            crap_stone.goto(x, y)
            self.crap_stones.append(crap_stone)

    def crap_stones_move(self):
        for crap in self.crap_stones:
            crap.forward(20)

    def increase_speed(self):
        self.craps_speed *= 0.9
