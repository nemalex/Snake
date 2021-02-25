import turtle
import time


def balra():
    fej.left(90)


def jobbra():
    fej.right(90)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(balra, "Left")
palya.onkey(jobbra, "Right")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

kijelzo = turtle.Turtle()
kijelzo.penup()
kijelzo.goto(0, 0)
kijelzo.pencolor("yellow")
kijelzo.hideturtle()

is_dead = False

while True:
    fej.forward(20)
    palya.update()
    time.sleep(0.3)
    if 380 < fej.xcor() or fej.xcor() < -380 or 180 < fej.ycor() or fej.ycor() < -180:
        is_dead = True
        kijelzo.write("A kukac meghalt", align="center")
