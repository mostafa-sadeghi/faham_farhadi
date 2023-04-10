# print("hello every body")
# print("hello every body")
# print("hello every body")
# print("hello every body")
# print("hello every body")


# for i in range(5):
#     print(f"hello world {i}")

# string = "abcdef"
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# print(string[4])
# print(string[5])

# for s in string:
#     print(s)


# numbers = [1, 2, 3, 4, 5, 6, 7]
# for x in numbers:
#     print(x)

# y = ('a', '1', 'c')
# for v in y:
#     print(v)


# numbers = []

# for i in range(5):
#     num = int(input('enter a number '))
#     if num % 2 == 0:
#         numbers.append(num)

# print(numbers)

# نمایش تمام اعداد زوچ کنتر از 1000
# even_numbers = []
# for number in range(1, 1001):
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(even_numbers)

# مجموع اعداد را حساب کن
# total = 0

# for i in range(5):
#     number = int(input('enter a number '))
#     # total = total + number
#     total += number

# print("total is", total)


# مجاسبه مجموع با کمک لیست

# numbers = []
# for i in range(5):
#     number = int(input('enter a number '))
#     numbers.append(number)

# print("sum is :", sum(numbers))


# کشیدن مثلث با کمک  حلقه
import turtle
s = turtle.Screen()
s.bgcolor('orange')
p = turtle.Pen()
p.shape('turtle')
p.pencolor('red')
p.pensize(4)


for i in range(3):
    p.forward(150)
    p.left(120)


# کشیدن مربع با کمک حلقه

for i in range(4):
    p.forward(150)
    p.left(90)

# کشیدن پنج ضلعی و شش ضلعی با کمک حلقه for
