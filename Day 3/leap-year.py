# 🚨 Don't change the code below 👇
from operator import truediv
from pickle import FALSE


year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
is_leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print('It\'s leap year!')
else:
    print('Not a leap year')
