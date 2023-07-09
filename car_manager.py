import random
from turtle import Turtle
from random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.generate_cars()

    def generate_cars(self):
        self.add_car()

    def add_car(self):
        my_chance = randint(1,5)
        if my_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=None, stretch_len=2, outline=None)
            new_car.penup()
            new_car.goto((300 + randint(200,500)), randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.setx(car.xcor()-MOVE_INCREMENT)

