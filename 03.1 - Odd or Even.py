import time

print('I can help you figure out if a whole number is odd or even.')

time.sleep(1.5)

#user input
while True:
    try:
        n = int(input('What is a number you would like to test?\n'))
        break    
    except ValueError:
        print('Please print a whole number.')

#uses remainder to determine if divisible by 2    
if (n % 2) == 0:
    print(f'The number {n} is even')
else:
    print(f'The number {n} is odd')