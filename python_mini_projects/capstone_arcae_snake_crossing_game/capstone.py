from turtle import Screen
from crossing_turtle import TURTLE
from crapstones import Crapstones
from crapstone_score_board import Scoreboard
import time

screen = Screen()
turtle = TURTLE()
crap_stones = Crapstones()
score_board = Scoreboard()

screen.tracer(0)
screen.title('crap stone turtle crossing game ')
screen.setup(800, 800)

screen.listen()

screen.onkey(turtle.up, 'Up')

is_game_on = True
while is_game_on:
    time.sleep(crap_stones.craps_speed)
    screen.update()
    crap_stones.add_crap_stone()
    crap_stones.crap_stones_move()
    if turtle.ycor() > 300:
        turtle.turtle_reposition()
        score_board.update_level()
        crap_stones.increase_speed()
    for crap in crap_stones.crap_stones:
        if crap.distance(turtle) < 20:
            is_game_on = False
            score_board.game_over()

screen.mainloop()
