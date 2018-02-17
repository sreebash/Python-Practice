print('Please input your number:')
number = int(input())
temp = number

while number > 1:
    number -= 1
    temp = temp*number

if temp == 0:
    print(1)
else:
    print(temp)