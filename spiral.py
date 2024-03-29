import turtle


def draw_spiral():
    turtle.speed(0)
    turtle.bgcolor("black")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    length = 10
    angle = 90

    for i in range(138):
        turtle.forward(length)
        turtle.right(angle)
        length += 5
        angle -= .01
        turtle.pencolor(colors[i % len(colors)])


draw_spiral()
turtle.exitonclick()
turtle.done()
