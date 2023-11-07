q = int(input('Enter the day: '))
m = int(input('Enter the month: '))
year = int(input('Enter the year: ')) 
k = year % 100

u = m + 1
j = year // 100
if k < 10:
    print(f'The date is {q}/{m}/0{k}')
else:
    print(f'The date is {q}/{m}/{k}')
    


h = (q + (u) + k + (k/5) + (j/4) - 2j) % 7