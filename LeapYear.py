print('Enter your diserable input:')
number = int(input())
if number % 400 == 0 | (number % 4 ==0 & number % 100 != 0):
    print('The number is leap year')
else:
    print('The number is not leap year')
