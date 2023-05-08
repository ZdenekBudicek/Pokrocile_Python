from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("green")
screen.title("Snake_Game")
screen.setup(width=600, height=600)

# Vypne neustále refreshování stránky, tím pádem pohyb přestane bý trhavej.
# To co je pod Tracrem se už ani neukáže. Dokud to ručně neobnovím.
screen.tracer(False)

square1 = Turtle("square")
square1.goto(0, 0)
square1.penup()

square2 = Turtle("square")
square2.penup()
square2.goto(20, 0)

# Obnoví stránku, načte to co se dělo
screen.update()

for _ in range(20):
    square1.forward(10)
    square2.forward(10)
    time.sleep(0.1)
    screen.update()

# Cyklus for lze jít od zadu, ale musíme mu říct po jakých krocích,
# odečetl jsem vzdálenost len -1, chci jít do 0 a po krocích -1
parts = ["první", "druhý", "třetí", "čtvrtý", "pátý"]
for index in range(len(parts) - 1, 0, -1):
    print(parts[index])

screen.exitonclick()
