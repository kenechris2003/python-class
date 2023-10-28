from random import *

random_num = randint(1,100)

while True:
    try:
        guess = int(input('Enter a random number(1-100): '))
        if guess == random_num:
            print('Congratulation you guessed correctly')
            break
        elif guess < random_num:
            print('Try again, your answer is less than the number')
        else:
            print('Try again, your answer is greater than the number')
    except:
        print('Invalid number')