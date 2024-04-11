import turtle
import turtle

pen = turtle.Turtle()

pen.speed(1)

pen.penup()
pen.goto(-100, 0)
pen.pendown()

pen.write("D", align="center", font=("Arial", 36, "bold"))
pen.forward(50)
pen.write("N", align="center", font=("Arial", 36, "bold"))
pen.forward(50)
pen.write("T", align="center", font=("Arial", 36, "bold"))

pen.hideturtle()

turtle.done()
