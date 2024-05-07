# Day 2  - Tip Calculator

import time

#intro
print('Welcome to the Tip and Split App.')
time.sleep(.5)
print('As the name suggests, I can easily help calculate the tip and help you split the check. ')
time.sleep(1)

#People splitting check
while True:
    try:
        p = int(input('How many people are you splitting the check with?\n')) + 1
        break
    except ValueError:
            print('Number of people must be put in as a whole number value.')
#p = int(input('How many people are you splitting the check with?\n'))
        
#calculate tip percent
while True:
    try:        
        t = float(input('What percent tip would you like to leave?\n')) / 100
        break
    except ValueError:
        print('Only input numbers. Do not put special characters or letters.')
#t = float(input('What percent tip would you like to leave?\n')) / 100

#Check amount
while True:
    try:
        c = float(input('What is the amount on your check?\n$'))
        break
    except ValueError:
        print('Amount needs to just be the numerical values.')
#c = float(input('What is the amount on your check?\n$'))

#formula for calculating tip - adding to bill - splitting bill
tip_amount = (c * t)
bill_total = (tip_amount + c)
bill_split = (bill_total / (p + 1))

#Output
print('Your total amount due is $'"{:.2f}".format(bill_total) + '.')
time.sleep(1)
print(f'When split between {p} people, that means you each owe $'"{:.2f}".format(bill_split) + '.')
