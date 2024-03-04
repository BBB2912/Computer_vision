from turtle import Turtle,Screen
from paddle import Paddle
from boll import  Boll
from pingpong_scoreboard import Scoreboard
import time
screen=Screen()

screen.title('!..Ping Pong..!')
screen.setup(1400, 800)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

r_paddle=Paddle((680,0))
l_paddle=Paddle((-680,0))

r_paddle_score=Scoreboard((100,250))
l_paddle_score=Scoreboard((-100,250))

boll=Boll()
screen.onkeypress(r_paddle.up,'w')
screen.onkeypress(r_paddle.down,'s')
screen.onkeypress(l_paddle.up,'Up')
screen.onkeypress(l_paddle.down,'Down')

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(boll.move_speed)
    boll.boll_move()
    if boll.ycor()>380 or boll.ycor()<-380:
        boll.bounce_y()
    if (boll.distance(r_paddle)<70 and boll.xcor()>650) or (boll.distance(l_paddle)<70 and boll.xcor()<-650):
        boll.bounce_x()
    if boll.xcor()>680:
        boll.replace_boll()
        l_paddle_score.update_score()
    if boll.xcor()<-680:
        boll.replace_boll()
        r_paddle_score.update_score()














screen.mainloop()