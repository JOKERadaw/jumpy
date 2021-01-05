import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from kindgrass import grass
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
grass()
game=1

turty=Player()
scory=Scoreboard()
screen.bgcolor("black")



screen.listen(turty)
screen.onkey(turty.move, "space")

game_is_on = True


cars=[]
enemies_n=20
def spawn(number):
    for x in range(number):
        car = CarManager()
        cars.append(car)

spawn(enemies_n)
while game_is_on:
    for car in cars:
        car.move(game)
        if car.detect(turty):
            game_is_on=False
            #break

    if turty.finishline():

        turty.goto(0,-290)
        game+=1
        scory.upgrade(game)

        for car in cars:
            car.goto(-300,400)
            cars.remove(car)
        enemies_n+=2
        spawn(enemies_n)

    time.sleep(0.1)
    screen.update()
screen.exitonclick()