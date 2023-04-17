import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    # segments[0].left(90)
    segments[0].right(90)

    if new_square.xcor() == 290 or new_square.xcor() == -290 or new_square.ycor() == 290 or new_square.ycor() == -290:
        game_is_on = True


screen.exitonclick()
