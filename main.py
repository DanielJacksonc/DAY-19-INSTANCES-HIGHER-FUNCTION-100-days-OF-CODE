
from turtle import Turtle, Screen

# from turtle import
click = Turtle()
screen = Screen()


def forward():
    click.forward(10)


def backward():
    click.backward(10)


def clockwise():
    new_heading = click.heading() + 10
    click.setheading(new_heading )


def counter_clockwise():
    new_heading = click.heading() - 10
    click.setheading(new_heading)


def clear():
    click.clear()
    click.reset()


screen.listen()
screen.onkey(key="W", fun=forward)
screen.onkey(key="S", fun=backward)
screen.onkey(key="A", fun=clockwise)
screen.onkey(key="D", fun=counter_clockwise)
screen.onkey(key="C", fun=clear)









screen.exitonclick()