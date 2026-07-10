from turtle import Screen
import time
from Day20_21.Snake_game.snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()

screen.update()

game_is_on = True

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

while game_is_on :
    screen.update()
    time.sleep(0.1)

    snake.move()

