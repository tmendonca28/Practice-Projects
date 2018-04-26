import turtle


def create_window():
    window = turtle.Screen()
    window.bgcolor("blue")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()


def draw_square():
    anthony = turtle.Turtle()
    anthony.shape("turtle")
    anthony.color("black")
    anthony.speed(7)
    movement = 0
    while movement < 4:
        anthony.forward(100)
        anthony.right(90)
        movement = movement + 1


def draw_circle():
    juliet = turtle.Turtle()
    juliet.shape("arrow")
    juliet.circle(100)
    juliet.color("red")


def draw_triangle():
    ozzie = turtle.Turtle()
    ozzie.shape("circle")
    ozzie.forward(100)
    ozzie.left(120)
    ozzie.forward(100)
    ozzie.left(120)
    ozzie.forward(100)


create_window()