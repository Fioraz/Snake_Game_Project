import time
from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.position = ()

    def food_generator(self):
        food = Turtle(shape="square")
        food_x = random.randint(-290, 290)
        food_y = random.randint(-290, 290)
        self.position = (food_x, food_y)
        food.pos(self.position)
        time.sleep(1)



