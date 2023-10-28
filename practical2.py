# Get user's weight
weight = float(input('input your weight in kg: '))
# Get user's height
height = float(input('input your height in metres: '))

# Getting the Body Mass Index (BMI) of the user

BMI = weight / height**2

# Print out the user's Body mass index
print(f'Thank you for using this program, your Body Mass Index (BMI) is {BMI}')
