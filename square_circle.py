import turtle


def draw_square(turtle_object):
    for i in range(1,5):
        turtle_object.forward(100)
        turtle_object.right(90)


def draw_circle_from_square():
    window = turtle.Screen()
    window.bgcolor("blue")
    # Create turtle object
    anthony = turtle.Turtle()
    anthony.shape("turtle")
    anthony.color("white")
    anthony.speed(9)
    for i in range(1, 37):
        draw_square(anthony)
        anthony.right(10)
    window.exitonclick()


draw_circle_from_square()
