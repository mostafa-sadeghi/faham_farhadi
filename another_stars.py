'''
* * * *
* * * *
* * * *
* * * *
'''

# print('* '*4)
# print('* '*4)
# print('* '*4)
# print('* '*4)

# for i in range(4):
#     print('* '*4)

# i = 0
# while i < 4:
#     print('* '*4)
#     i = i + 1  # i +=1

# for 4
# while
# total = 0
# for i in range(4):
#     number = int(input('enter a number: '))
#     total = total + number

# print("total is:", total)


# exercise:
'''
* * *
* * *
* * *
'''
# for i in range(3):
#     print('* '*3)
# print('------------------------')
# i = 0
# while i < 3:
#     print('* ' * 3)
#     i += 1

"""نمره سه درس یک دانش آموز را از ورودی بگیری و معدلش رو پرینت کنی"""
"""معدل میشه مجموع نمرات تقسیم بر تعداشون که اینجا سه هست"""
"""با حلقه for  و while"""
scratch_score = float(input('enter scratch score: '))
java_score = float(input('enter java score: '))
python_score = float(input('enter python score: '))

average = (scratch_score + java_score + python_score)/3
print("student's average is:", average)