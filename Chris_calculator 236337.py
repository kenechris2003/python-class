
print('What operation would you like to perform?')
print('0: Exit')
print('1: Addition')
print('2: Subtraction')
print('3: Multiplication')
print('4: Division')
print('5: modulus')

operationSelector = int(input('Enter choice (0/1/2/3/4/5): '))
if operationSelector == 0:
    print('Quitting Calculator')
else:
    value1 = int(input('Enter first number =  '))
    value2 = int(input('Enter second number =  '))


    if operationSelector == 1:
                    addition = value1 + value2
                    print(f'The sum of the two numbers is {addition}')
    elif operationSelector == 2:
                    subtraction = value1 - value2
                    print(f'The difference of the two numbers is {subtraction}')
    elif operationSelector == 3:
                    multiply = value1 * value2
                    print(f'The multiplication the the two numbers is {multiply}')
    elif operationSelector == 4:
            if value2 == 0:
                print('MathError')
            else:
                divison = value1 / value2
                print(f'The division of the two numbers is {divison}')   
    elif operationSelector == 5:
                modulus = value1 % value2
                print(f'The modulus of the first number to the second number is {modulus}')



