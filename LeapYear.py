print('Enter your input number:')
number = int(input())
if number % 4 == 0 and number % 100 != 0:
    print(number, 'is a leap year.')
elif number % 100 == 0 and number % 400 == 0:
    print(number, 'is a leap year.')
else:
    print(number, 'is not a leap year.')
