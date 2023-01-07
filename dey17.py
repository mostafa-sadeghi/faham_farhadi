# age = 28
# if age >= 18:
#     print("you are adult")
#     print('you are greater than 18')
# else:
#     print('you are not adult')
#     print("you're age is lower than 18")
###################################################

# if age >= 18:
#     print('you are adult')

# elif age >= 10 and age < 18:
#     print('you are junior')
# else:
#     print('you are kid')
###################################################
# if age >= 18:
#     print('you are adult')
# elif 10 <= age < 18:
#     print("you are junior")
# else:
#     print('you are kid')


# entry = input('enter "exit" to exit from program ')
# if entry == "exit":
#     exit()
# if entry != "exit":
#     print(entry)

# entry = input('enter a number> ')
# if entry == '12' or entry == '14' or entry == '16':
#     print('OK')
# else:
#     print("not OK")


# loop
# numbers = [1, 2, 3, 4]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# for x in numbers:
#     print(x)

# name = "nikan"
# for y in name:
#     print(y)

# chars = ('a', 'b', 'c')
# for c in chars:
#     print(c)


# for i in range(100):
#     print(i)
# count = 0
# for i in range(100, 501, 2):
#     # print(i)
#     count += 1
# print(count)

# c = 0
# for i in range(100, 501):
#     if i % 2 == 0:
#         c += 1
# print(c)


import turtle
s = turtle.Screen()
s.bgcolor('orange')
p = turtle.Pen()
p.pencolor('cyan')
p.pensize(4)
p.shape('turtle')

# draw triangle

for i in range(3):
    p.fd(100)
    p.lt(120)

p.begin_fill()
p.fillcolor('red')
for i in range(3):
    p.fd(100)
    p.rt(120)
p.end_fill()

# exercise مربع تو پر و توخالی
