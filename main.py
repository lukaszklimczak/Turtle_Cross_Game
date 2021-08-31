from turtle import Turtle, Screen
from player import Player
from traffic import Car
from show_level import Level
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("road2.gif")
screen.tracer(0)

player = Player()

number_of_cars = []
for i in range(20):
    number_of_cars.append(i)

cars = {k: Car() for k in number_of_cars}

screen.listen()
screen.onkey(player.move_forward, "Up")

level = Level()

speed = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)

    for i in range(len(number_of_cars) - 1):
        cars[i].move()

    for i in range(len(number_of_cars) - 1):
        if cars[i].xcor() < -330:
            cars[i].reset_position()

        if player.distance(cars[i]) < 15:
            game_is_on = False
            level.game_over()

    if player.ycor() > 250:
        level.point()
        time.sleep(1)
        player.reset_position()
        speed *= 0.5
        for i in range(len(number_of_cars) - 1):
            cars[i].reset_position()



screen.exitonclick()