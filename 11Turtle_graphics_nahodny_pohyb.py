from turtle import Turtle, Screen
import random

zelva = Turtle()
zelva.shape("turtle")
pen = 1
colors = ["alice blue", "azure4", "cornsilk2", "dark orange", "dark salmon", "DarkGreen", "DarkOliveGreen2", "lavender",
          "light pink", "MediumOrchid", "misty rose", "NavajoWhite4", "OrangeRed3", "plum1", "thistle2", "YellowGreen",
          "tomato", "SteelBlue2"]
angle = [90, 180, 270, 360]
zelva.speed(0)
while True:
    random_color = random.randint(0, len(colors) - 1)
    zelva.color(colors[random_color])
    zelva.pensize(pen)
    zelva.forward(20)
    zelva.right(random.choice(angle))
    if pen < 10:
        pen += 0.5

my_screen = Screen()
my_screen.exitonclick()
