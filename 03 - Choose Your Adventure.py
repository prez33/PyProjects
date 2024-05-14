# This is going to be a guessing game in which there is only one right answer to each question
# The user is not prompted beyond the question. 
# I want it to repeat the question until the user can guess right.
# Model after eXit game from Mr Robot 

import time

def start():
    return input('You awake in a dark room. You don\'t know where you are, but you see a door. What do you do?\n').lower()

def intro():
    return input('The door is locked, but you notice a mat. What do you do?\n').lower()

def hidden_loop():
   return  input('You notice a computer on the desk. What do you do?\n').lower()

def see_mat():      
   return  input('You find a key. What do you do?\n').lower()
               
def use_key():       
    return  input('The key does not fit in the door. What do you do?\n').lower()

def room():      
   return  input('You see a chest against the wall. What do you do?\n').lower()
        
def open_chest():
   return  input('The chest opens to reveal a dark hole. What do you do?\n').lower()



# program start
print("""
  _______
 /  ___  \\
|  /   \  |
| |     | |
| |     | |
| |_____| |
|  _____O |
| |     | |
|_|_____|_|
""")            
response = start()


# see if lift mat or hidden loop
while True:
    if ('open' in response or 'try' in response) and  'door' in response:
        print("""
          _______
         /  ___  \\
        |  /   \  |
        | |     | |
        | |     | |
        | |_____| |
        |  _____O |
        | |     | |
        |_|_____|_|
       ____________
      /___________/
     
        """)
        response = intro()
        break
#     
# This is the hidden loop    
    elif response == 'stay' or response == 'wait':
        print("""
              ______
            / |     |
           |__|_____|
           |__|_____|
              \\______\\
              """)
        response = hidden_loop()
# power on computer       
        while True:
            if 'on' in response:
                print("""
  __________________________  
  |  ___________________   |
  |  |                  |  |
  |  |  []              |  | 
  |  |  test.exe        |  |
  |  |                  |  |
  |  |                  |  |
  |  |__________________|  |                 
  |________________________| 
  """)
                response = input('The computer powers on. It appears there is only one program installed. What do you do?\n').lower()
                break
# loop until on            
            else:
                 response = input('You notice a computer on the desk. What do you do?\n').lower()
#next step: boot program that brings you back to the beginning of the choose your adventure.         
        while True:    
            if 'run' in response:
                print('The program boots up and the screen shows:\n')
                break
            else:
                response = input('The computer powers on. It appears there is only one program installed. What do you do?\n').lower()
    else:
        response = start()   

# lift mat to find key    
while True:
    if ('under' in response or 'lift' in response) and 'mat' in response:
        response = see_mat()
        break
    else:
        response = intro()

# try to unlock door
while True:
    if ('unlock' in response and 'door' in response) or ('try' in response and 'key' in response):
        response = use_key()
        break
    else:
        response = see_mat()

# search room
while True:
    if ('search' in response or 'look' in response) and 'room' in response:
        response = room()
        break
    else:
        response = use_key()

# open chest
while True:
    if 'open' in response or 'unlock' in response and 'chest' in response:
        response = open_chest()
        break
    elif 'try' in response and 'key' in response:
        response = open_chest()
        break
    else:
        response = room()
        
if 'in' in response or 'down' in response and 'hole' in response:
    print('You found a tunnel out of the room and escaped!')
elif response == 'stay' or response == 'wait':
    print('The president enters through the locked door and congratulates you on passing the test.')
    time.sleep(2)
    input('Are you ready for your first mission? (Yes or Hell Yea!)\n')
else:
    open_chest()
