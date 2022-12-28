import turtle

s = turtle.Screen()
p = turtle.Pen()
s.bgcolor('black')
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

p.pensize(4)
# p.speed('slowest')
p.penup()
p.setpos(-90, 30)
p.pendown()

p.pencolor(COLORS[0])
p.forward(200)
p.right(144)
p.pencolor(COLORS[1])
p.forward(200)
p.right(144)
p.pencolor(COLORS[2])
p.forward(200)
p.right(144)
p.pencolor(COLORS[3])
p.forward(200)
p.right(144)
p.pencolor(COLORS[4])
p.forward(200)
p.right(144)
p.penup()
p.setpos(80, -140)
p.pendown()
p.pencolor('olive')
p.write("hello every body", font=("Arial", 12, 'italic'))
p.hideturtle()


s.exitonclick()
