import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True
snake = Snake()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # segments[0].left(90)
    # segments[0].right(90)
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    #
    # if new_square.xcor() == 290 or new_square.xcor() == -290 or new_square.ycor() == 290 or new_square.ycor() == -290:
    #     game_is_on = True


screen.exitonclick()
