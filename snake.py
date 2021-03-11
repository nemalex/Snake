import turtle
import time
from random import randint

step = 20

is_dead = False
pont = 0


def balra():
    if not fej.heading() == 0:
        fej.setheading(180)


def jobbra():
    if not fej.heading() == 180:
        fej.setheading(0)


def fel():
    if not fej.heading() == 270:
        fej.setheading(90)


def le():
    if not fej.heading() == 90:
        fej.setheading(270)


def hizik():
    testrész = turtle.Turtle()
    testrész.color("yellow")
    testrész.shape("circle")
    testrész.penup()
    kukac.append(testrész)


def gyumolcs_kirak():
    x = randint(-380 / step, 380 / step) * step
    y = randint(-300 / step, 300 / step) * step
    gyumolcs.goto(x, y)
    hizik()



palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(balra, "Left")
palya.onkey(jobbra, "Right")
palya.onkey(fel, "Up")
palya.onkey(le, "Down")


fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")
fej.setheading(0)

kukac = []

gyumolcs = turtle.Turtle()
gyumolcs.penup()
gyumolcs.shape("circle")
gyumolcs.color("red")
gyumolcs_kirak()

kijelzo = turtle.Turtle()
kijelzo.penup()
kijelzo.sety(240)
kijelzo.pencolor("yellow")
kijelzo.hideturtle()
kijelzo.write("0 pont", align="center", font=("Arial", 36, "normal"))

for i in range(0, 20):
    hizik()

while not is_dead:

    fejx = fej.xcor()
    fejy = fej.ycor()

    fej.forward(step)

    if fej.distance(gyumolcs.xcor(), gyumolcs.ycor()) < 20:
        gyumolcs_kirak()
        pont += 1
        kijelzo.clear()
        # kijelzo.write(f"{pont} pont", align="center", font=("Arial", 36, "normal"))
        kijelzo.write(len(kukac), align="center", font=("Arial", 36, "bold"))

    if 380 < fej.xcor() or fej.xcor() < -380 or 280 < fej.ycor() or fej.ycor() < -280:
        is_dead = True

    for resz in kukac:
        if resz.distance(fej.xcor(), fej.ycor()) < 20:
            is_dead = True

    kukac[-1].setx(fejx)
    kukac[-1].sety(fejy)
    kukac = [kukac[-1]] + kukac[:-1]

    palya.update()
    time.sleep(0.2)

kijelzo.clear()
kijelzo.write("A kukac meghalt", align="center", font=("Arial", 36, "normal"))
turtle.done()
