from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
for _ in range(0, 4):
    tommy.forward(100)
    tommy.left(90)

my_screen = Screen()
my_screen.exitonclick()
