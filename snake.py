from turtle import Turtle


class Snake:

    def __init__(self):
        segments = []
        x = -40
        snake_length = 3
        for square_index in range(0, snake_length):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.setpos(x, 0)
            segments.append(new_square)
            x += 20
        return snake_length


    def snake_length(self):
        

