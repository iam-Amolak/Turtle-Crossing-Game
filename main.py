import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move_turtle, "Up")

i = 0
game_is_on = True
score.update_score()

while game_is_on:
    i += 1
    time.sleep(0.1)
    screen.update()
    if i%6==0 and score.level<=2:
        car.generate_car()
    car.move_cars(score.level - 1)

    if turtle.ycor() == FINISH_LINE_Y:
        turtle.reset_turtle()
        score.increase_level()

    for cars in car.all_cars:
        if cars.distance(turtle) <= 20:
            # screen.clear()
            score.game_over()
            game_is_on = False

screen.exitonclick()