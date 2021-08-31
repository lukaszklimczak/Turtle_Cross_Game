from turtle import Turtle, Screen
import random


Y_POSITIONS = [-200, -100,  0, 100, 200]
X_POSITIONS = [300, 400, 500, 600, 700, 800]


image = "car.gif"
image2 = "car2.gif"
image3 = "car3.gif"
image4 = "car4.gif"
image5 = "car5.gif"

car_models = [image, image2, image3, image4, image5]

screen = Screen()
screen.addshape(image)
screen.addshape(image2)
screen.addshape(image3)
screen.addshape(image4)
screen.addshape(image5)


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(car_models[random.randint(0, len(car_models) - 1)])
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.goto(X_POSITIONS[random.randint(0, len(X_POSITIONS) - 1)],
                  Y_POSITIONS[random.randint(0, len(Y_POSITIONS) - 1)])

    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def reset_position(self):
        y = self.ycor()
        self.goto(X_POSITIONS[random.randint(0, len(X_POSITIONS) - 1)], y)
