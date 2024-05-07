# Day 1 Project

import time

print('I am the band name generator genie.')

time.sleep(1.5)

name = input('What is your name?\n')
time.sleep(.5)
x = input('Which city did you grow up in?\n')
time.sleep(.5)
y = input('What is your first pet\'s name?\n')
time.sleep(1)
band_name = x + ' ' + y

print(name + ' your band name is the ' + band_name)