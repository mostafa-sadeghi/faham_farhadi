import turtle
s = turtle.Screen()
s.bgcolor('pink')
p = turtle.Pen()
p.shape('turtle')
p.pencolor('red')
p.pensize(4)


# draw star
# p.penup()
# p.goto(-60, 0)

# p.pendown()
# for i in range(5):
#     p.forward(150)
#     p.right(144)

# p.penup()
# p.goto(-90, 220)
# p.write("our nice star", font=15)


# draw animation clock
p.ht()
p.speed('fastest')
for i in range(12):
    p.setheading(i*-30 + 60)
    p.penup()
    p.forward(150)
    p.pendown()
    p.forward(25)
    p.penup()
    p.forward(30)
    p.write(i+1, font=15)
    p.setpos(0, 0)

p.penup()
p.home()
p.setpos(0, -240)
p.pendown()
p.circle(240)
p.penup()
p.home()
p.write("clock", font=14)
s.exitonclick()
