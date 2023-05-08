from turtle import Turtle, Screen
import random

zelva = Turtle()
zelva.shape("turtle")
zelva.pensize(4)
colors = ["alice blue", "azure4", "cornsilk2", "dark orange", "dark salmon", "DarkGreen", "DarkOliveGreen2", "lavender",
          "light pink", "MediumOrchid", "misty rose", "NavajoWhite4", "OrangeRed3", "plum1", "thistle2", "YellowGreen",
          "tomato", "SteelBlue2"]
moves = 3
my_screen = Screen()
my_screen.bgcolor("DeepSkyBlue3")

while moves != 9:
    random_color = random.choice(colors)
    zelva.color(random_color)
    for _ in range(moves):
        zelva.forward(100)
        zelva.right(360 / moves)
    moves += 1
my_screen.exitonclick()
