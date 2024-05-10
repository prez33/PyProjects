year = int(input('What year would you like to check?\nYear: '))

while True:
    try:
        if (year % 4) == 0 and (year % 100) != 0:
            print(f'The year {year} is a leap year')
            break
        elif (year % 100) == 0 and (year % 400) == 0 and (year % 4) == 0:
            print(f'The year {year} is a leap year')
            break
        else:
            print(f'The year {year} is not a leap year')
            break
    except ValueError:
        print('The year must be a whole number.')