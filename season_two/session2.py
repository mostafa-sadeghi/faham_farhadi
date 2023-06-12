import turtle
import time
import random
delay = 0.2


high_score = 0
score = 0


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
# win.register_shape("strawberry.gif")
win.title("Our first game")
win.bgcolor('blue')

win.setup(width=600, height=600)
win.tracer(0)
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")


head = turtle.Turtle()
head.speed('fast')
head.shape("square")

head.color("black")
head.penup()
head.goto(0, 100)
head.direction = ""


food = turtle.Turtle()
food.speed('fastest')
food.shape("circle")
food.color("red")

food.penup()
food.shapesize(0.5, 0.5)
food.goto(0, 0)

pen_for_score = turtle.Turtle()
pen_for_score.speed('fastest')
pen_for_score.ht()
pen_for_score.penup()
pen_for_score.goto(0, 260)
pen_for_score.write(
    f"Score: 0 High Score: {high_score}", align="center", font=("Arial", 24))


segments = []

while True:
    win.update()

    if head.distance(food) < 15:
        score += 1
        pen_for_score.clear()
        pen_for_score.write(
            f"Score: {score} High Score: {high_score}", align="center", font=("Arial", 24))
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed("fast")
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

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # TODO   اصلاح بیشترین امتیاز زمانی که امتیاز ما از قبلی کمتر باشه
        # TODO اضافه کردن خط به گوشه های صفحه
        high_score = score
        score = 0
        pen_for_score.clear()
        pen_for_score.write(
            f"Score: {score} High Score: {high_score}", align="center", font=("Arial", 24))
        time.sleep(.4)
        head.goto(0, 0)
        head.direction = ""
        for body in segments:
            body.ht()
        segments = []

    move()

    for body in segments:
        if body.distance(head) < 15:
            time.sleep(.4)
            head.goto(0, 0)
            head.direction = ""
            for body in segments:
                body.ht()
            segments = []

    time.sleep(delay)
