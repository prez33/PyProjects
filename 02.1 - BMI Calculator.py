# Additional exercise from 100 days of Coding creating a BMI calculator with my own twist
import time

#Purpose with some fun
print('I am the BMI Wizard.') 
time.sleep(.5)
print('Answer my questions and I will guess your BMI.')

#This calculates the height, whether it is meters or inches.
while True:
    try:
        y = input('Do you know your height in meters? (Yes or No)\n').lower()
        if y == 'y' or y == 'yes':
            height = float(input('What is your height in meters?\n'))
            break
        elif y == 'n' or y == 'no':
            height_inches = float(input('What is your height in inches?\n'))
            height = (height_inches * 0.0254)
            break
        else:
            print('Yes or No answers only. ')
            time.sleep(1)
    except ValueError:
        print('Height must be a number')
        time.sleep(1)

#Prints 2 decimal values for user to see their height in meters (pointless, I guess if you input your height in meters)
print('*magic dust* You are ' + "{:.2f}".format(height) + 'm tall!')
time.sleep(1)

#Same as height but with weight
while True:
    try:
        x = input('Do you know your weight in kg? (Yes or No)\n').lower()
        if x == 'y' or x == 'yes':
            weight = float(input('What is your weight in kg?\n'))
            break
        elif x == 'n' or x == 'no':
            weight_pounds = float(input('What is your weight in lbs?\n'))
            weight = (weight_pounds / 2.2)
            break
        else:
            print('Yes or No answers only. ')
            time.sleep (1)
    except ValueError:
        print('Height must be a number')
        time.sleep(1)

#Once again, same statement for weight (still pointless if you use metric), possibly funny given the introduction
print('The Great Wizard cannot be wrong! You are ' + "{:.2f}".format(weight) + 'kg!')

time.sleep(1)
print('This means your BMI is... ')
time.sleep(2)
print("{:.1f}".format(weight / height ** 2) + 'kg/m2')
