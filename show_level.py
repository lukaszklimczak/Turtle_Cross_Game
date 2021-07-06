from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_levelboard()
        self.goto(-200, 240)

    def update_levelboard(self):
        self.clear()
        self.goto(-200, 240)
        self.write(f"Level: {self.level}", align="center", font=("courier", 30, "bold"))

    def point(self):
        self.level += 1
        self.update_levelboard()

    def game_over(self):
        self.goto(0, 50)
        self.write("GAME OVER", align="center", font=("Courier", 60, "bold"))
