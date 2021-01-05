COLORS = ["red", "orange", "yellow", "brown", "blue", "purple"]


from turtle import Turtle

import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 2
        self.n=1
        self.penup()
        self.shape("square")
        self.turtlesize(1,2)
        self.color(COLORS[random.randint(0,5)])
        self.x=random.randint(300,1000)
        self.y=random.randint(-260,270)
        self.goto(self.x,self.y)
    def move(self,game):
        if self.xcor()<-310:
            self.goto(-300,400)
            self.goto(500,0)
            self.goto(400,self.y)
#if the level number grow also the speed do

        if game!=self.n:
            self.MOVE_DISTANCE+=self.MOVE_INCREMENT
            self.n+=1
        self.backward(self.MOVE_DISTANCE)

        

    def detect(self,turty):
        return turty.ycor()<=self.y+20 and turty.ycor()>=self.y-20 and turty.distance(self)<25
