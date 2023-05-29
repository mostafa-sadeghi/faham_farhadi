import turtle
import time
import random
delay = 0.1


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


win = turtle.Screen()
win.register_shape("strawberry.gif")
win.title("Our first game")
win.bgcolor('blue')

win.setup(width=600, height=600)
win.tracer(0)
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")


head = turtle.Turtle()
head.speed('fastest')
head.shape("square")

head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"


food = turtle.Turtle()
food.speed('fastest')
food.shape("circle")
food.color("red")

food.penup()
food.shapesize(0.5, 0.5)
food.goto(0, 0)

segments = []

while True:
    win.update()
    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed("fastest")
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments):
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    time.sleep(delay)
