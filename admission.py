from time import *
import pandas as pd

def all_upper(my_list):
    return [x.upper() for x in my_list]



# print(new_df.loc[2])
# pd.options.display.max_rows = 9999
# print(df.info())
# print(df.columns)
# print(df.tail())


jamb_cutOff = 200
jamb_max = 400
post_utme_cutOff = 50
post_utme_max = 100
print("*" *100)
print('Welcome to the University of Ibadan.....')
print("*" *100)
sleep(2)
while True:
    try:
        jamb_result = int(input('Enter your jamb score: '))
        break
    except:
         print('Please enter a valid jamb score: ')       
while jamb_result >= jamb_max:
    jamb_result = int(input('Enter your jamb score: '))
    
if jamb_result < jamb_cutOff:
    print('Sorry you are not eligible to write the post utme.......')

else:
    print('Congratulations, You are eligible for to write the post utme and also gain admission')
    sleep(1.5)
    # After writing the post utme  
    while True:
        try:
            post_utme_result = int(input('Enter your post utme score: '))
            break
        except:
         print('Please enter a valid post utme score: ')  
    while post_utme_result >= post_utme_max:
        post_utme_result = int(input('Enter your post utme score: '))

    if post_utme_result < post_utme_cutOff:
        print('Sorry you are not eligible for admission.......')
    else:
        print('Congratulations on passing the post utme, You are eligible to gain admission')
        sleep(1.5)

        aggregate = (jamb_result / 8) + (post_utme_result / 2)

        print(f'Your aggregate is {aggregate}')

        user_input = input('Enter Department you applied for: ').upper()

df = pd.read_csv('2023_cut-off_marks.csv')

new_df = df.dropna()

department = new_df["Programme"].values.tolist()

upper_list = all_upper(department)
if user_input in upper_list:
    for i in range(len(upper_list)):
        cut_Off = new_df["Merit"].values.tolist()
        if user_input == upper_list[i]:
                    print(f'Please hold while we check the departmental cutoff mark to see if you passed your departmental cutoff......')
                    sleep(1.5)
                    print(f'You are applying into {user_input}')
                    sleep(1.5)
    if aggregate >= cut_Off[i]:
        print('Congratulations, you have been admitted into the UNIVERSITY OF IBADAN, THE FIRST AND THE BEST!!!!!!')
    else:
        print('Sorry, Your aggregate is less than the departmental cut off for your course')
else:
    print('Sorry we do not offer this course in our school')




