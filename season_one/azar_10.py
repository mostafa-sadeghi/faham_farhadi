# numbers = input('''enter some numbers
# Like: 1 2 3 4
# :> ''')

# list_of_numbers = numbers.split(' ')
# نمایش مقادیر موجود در لیست قبل از حذف
# print('original list', list_of_numbers)

# حذف یک خانه از داخل لیست
# del list_of_numbers[0]
# نمایش مقادیر موجود در لیست بعد از حذف
# print('list after delete', list_of_numbers)

# حذف یک مقدار مشخص از داخل لیست
# number = input('enter number for deleting:> ')
# list_of_numbers.remove(number)
# print('list numbers after delete',list_of_numbers)


# اضافه کردن مقدار به لیست

# number = input('enter a number to add: ')
# list_of_numbers.append(number)
# print('list numbers after add', list_of_numbers)

# tuple:

# numbers = (1, 2, 3, 4)
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# امکان تغییر در تاپل وجود ندارد
# امکان حذف از تاپل وجود ندارد
# امکان اضافه کردن در تاپل وجود ندارد

# numbers[1] = 5

# list
# numbers = [1, 2, 3, 4]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])

# امکان تغییر در لیست وجود دارد
# امکان حذف از لیست وجود دارد
# امکان اضافه کردن در لیست وجود دارد
# numbers[1] = 5
# print(numbers)

# dict | dictionary

student_favorites = {
    'ali': 'football',
    'reza': 'baseball',
    'sina': 'tennis'
}

print(student_favorites['ali'])
print(student_favorites['reza'])
print(student_favorites['sina'])


# exercise:  یک دیکشنری بسازی که نمرات درس های ریاضی، علوم، ورزش، برنامه نویسی و زبان یک دانش اموز رو ذخیره کند

# حذف از دیکشنری
# print('student favorites before delete', student_favorites)
# del student_favorites['ali']
# print('student favorites after deleting', student_favorites)
# اضافه کردن به دیکشنری
# student_favorites['nima'] = 'pingpong'
# print('student favorites after add', student_favorites)

# چسباندن رشته
s1 = 'a'
s2 = 'b'
s = s1 + s2
print(s)
# چسباندن لیست
l1 = [1, 2]
l2 = [3, 4]
l = l1 + l2
print(l)

# درمورد دیکشنری چطور؟
# خیر
# x1 = {
#     'id': 1,
#     'name': 'vihan'
# }
# x2 = {
#     'id': 2,
#     'name': 'nikan'
# }

# x = x1 + x2
