from turtle import Turtle
class grass(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("green")
        self.goto(0,-294)
        self.turtlesize(1, 80)