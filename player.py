from turtle import Turtle, Screen

image = "turtle2.gif"

screen = Screen()
screen.addshape(image)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(image)
        self.shapesize(2)
        self.penup()
        self.setheading(90)
        self.color('black')
        self.goto(0, -270)

    def move_forward(self):
        self.forward(20)

    def reset_position(self):
        self.goto(0, -270)


