from turtle import Screen
import time

import random

from Day22.Pong.paddle import Paddle
from ball import Ball
from line import Line
from scoreboard import Scoreboard

CHANCE = 20

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong(My_Solution)")
screen.tracer(0)

line = Line()
scoreboard = Scoreboard()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()

screen.update()


screen.listen()
screen.onkey(key="Down",fun=paddle1.down)
screen.onkey(key="Up",fun=paddle1.up)
screen.onkey(key="w",fun=paddle2.up)
screen.onkey(key="s",fun=paddle2.down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    paddle1.move()
    paddle2.move()
    ball.move()

    #wall
    if ball.xcor() > -380 or ball.xcor() < 380:
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.setheading(-1 * (ball.heading()))

    #goal
    if ball.xcor() < -400 :
        scoreboard.increase_p1_score()
        scoreboard.update()
        ball.reset_ball()
    elif ball.xcor() > 400 :
        scoreboard.increase_p2_score()
        scoreboard.update()
        ball.reset_ball()

    #shoot
    for segment in paddle1.segments:
        if ball.distance(segment) < 18:
            ball.setheading(random.randint(100,260))

    for segment in paddle2.segments:
        if ball.distance(segment) < 18:
            ball.setheading(random.randint(280,440))

    if scoreboard.p1_score == CHANCE or scoreboard.p2_score == CHANCE:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()