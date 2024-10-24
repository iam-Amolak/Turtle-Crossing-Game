from random import randint, randrange
from turtle import Turtle

from player import MOVE_DISTANCE

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 0.1

    def generate_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(COLORS[randint(0, 5)])
        rand_y = randrange(-250, 250)
        car.goto(300, rand_y)
        self.all_cars.append(car)

    def move_cars(self, level):
        for cars in self.all_cars:
            cars.backward(MOVE_DISTANCE + level * MOVE_INCREMENT)

    # def update_speed(self):
    #     self.speed += MOVE_INCREMENT
    #     self.move_cars()
