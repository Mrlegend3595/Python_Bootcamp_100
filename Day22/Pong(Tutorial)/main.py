from turtle import Screen
from time import sleep

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

R_PADDLE_POSITION= (350,0)
L_PADDLE_POSITION= (-350,0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True

while game_is_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()


    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
