from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
cordinates = [100, 90]
# for _ in range(0, 20):
#     tommy.pendown()
#     tommy.forward(100)
#     tommy.penup()
#     tommy.left(90)
tommy.speed(1)
for _ in range(0, 10):
    tommy.forward(20)
    tommy.penup()
    tommy.forward(20)
    tommy.pendown()


my_screen = Screen()
my_screen.exitonclick()
