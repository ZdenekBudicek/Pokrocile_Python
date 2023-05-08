import turtle

# Vytvoření želvy a nastavení její velikosti
t = turtle
t.pensize(5)
t.pencolor("blue")
t.pen(fillcolor="red")
t.begin_fill()
# Vytvoření 12 cípů hvězdice
for i in range(12):
    t.forward(100)
    t.right(150)
t.end_fill()

my_screen = turtle.Screen()
my_screen.exitonclick()
