days = int(input('Number of days: '))
days_in_a_year = 365

days_in_a_week = 7
years = days // days_in_a_year

days_left = days % days_in_a_year

weeks = days_left // days_in_a_week

days = days_left % days_in_a_week

print(f'Years: {years}')
print(f'Weeks: {weeks}')
print(f'Days: {days}')