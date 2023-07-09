# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date one week from the date entered
from datetime import datetime,timedelta
today = datetime.now()
print("Today is : ", str(today))
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))
one_week = timedelta(weeks=1)
date = input("enter a date:(dd/mm/yyyy)")
input_date = datetime.strptime(date, '%d/%m/%Y')
print(" a week from your date:", str(input_date + one_week))

