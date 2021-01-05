from turtle import Turtle
STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.right(-90)
        self.goto(STARTING_POSITION)
        self.color("brown")
        self.finishline()
    def move(self):
        self.forward(MOVE_DISTANCE)
    def finishline(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True


