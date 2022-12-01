# number1 = int(input('enter first number: '))
# number2 = int(input('enter second number: '))

# output = number1 + number2

# print(f'{number1} + {number2} = {output}')

# exercise 1:
# برنامه ای بنویسید که دو عدد از ورودی بگیرد و همینطور عملگر را از ورودی بگیرد و نتیجه را نمایش دهد
# operator = input('''to sum enter +,
# to sub enter -,
# to mul enter * and to div enter /''')

#  4 رنگ را از ورودی بگیر و کل رنگ و همینطور اولین مقدار و آخرین مقدار  را نمایش بده

color1 = input('enter first color: ')
if color1 == 'red':
    exit()
color2 = input('enter first color: ')
if color2 == 'red':
    exit()
color3 = input('enter first color: ')
if color3 == 'red':
    exit()
color4 = input('enter first color: ')
if color4 == 'red':
    exit()
colors = []
colors.append(color1)
colors.append(color2)


colors.append(color3)
colors.append(color4)
print(f'colors are : {colors}')
print(f'first color is : {colors[0]}')
print(f'first color is : {colors[-1]}')
