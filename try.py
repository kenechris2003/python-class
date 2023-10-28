age = int(input('Enter your age: '))
age_category = input('Enter your age category: ')
ac = age_category.lower()

if (age > 18 or ac == 'adult'):
    print('Your eligible to vote')
else:
    print('Sorry you not eligible to vote')
    print('Your are not yet an adult')