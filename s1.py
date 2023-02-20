even_numbers = []
odd_numbers = []

for i in range(10):
    n = float(input('enter a number: '))
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

print("even_numbers", even_numbers)
print("odd_numbers", odd_numbers)
