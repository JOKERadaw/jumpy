from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-230,260)
        self.write("level: 1",font=FONT,align="center")
    def upgrade(self,game):
        self.clear()
        self.write(f"level: {game}", font=FONT, align="center")