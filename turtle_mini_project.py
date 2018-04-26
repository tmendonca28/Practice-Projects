import turtle


def draw_rhombus(turtle_obj):
    for i in range(0, 2):
        turtle_obj.backward(90)
        turtle_obj.right(40)
        turtle_obj.backward(90)
        turtle_obj.right(140)


def draw_circle(turtle_obj):
    turtle_obj.begin_fill()
    turtle_obj.circle(30)
    turtle_obj.end_fill()


def draw_objects():
    window = turtle.Screen()
    window.bgcolor("blue")
    anthony = turtle.Turtle()
    anthony.color("white")
    anthony.speed(9)
    anthony.setpos(0, -20)
    draw_circle(anthony)
    anthony.setpos(0, 0)
    anthony.right(-90)
    for i in range(0, 60):
        draw_rhombus(anthony)
        anthony.left(6)
    anthony.backward(300)
    window.exitonclick()


draw_objects()
