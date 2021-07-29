year = int(input("Which year do you want to check? "))

if year % 4 > 0:
    print('not a leap year')
elif year % 4 == 0 and year % 100 > 0: 
    print('a leap year2')
elif year % 4 == 0 and year % 100 == 0:
    if year % 400 > 0:
        print('not a leap year3')
    else:
        print('leap year')