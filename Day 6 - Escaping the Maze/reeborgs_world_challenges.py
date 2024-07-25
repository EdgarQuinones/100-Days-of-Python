# Challenge 1 - Hurdles 

def turn_left():
    print("Turn left")
def move():
    print("Move")
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_right():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for jumps in range(0, 6):
    move()
    jump_right()
    
# Challenge 2 - Flag at random spot

# Same functions 
def at_goal():
    print("Are you at goal?")

while not at_goal():
    move()
    jump_right()
    if at_goal:
        break
    
# Challenge 3 - Randomly located walls

def front_is_clear():
    print("Is there no wall in front of you?")

while not at_goal():
    if at_goal():
         break
    elif front_is_clear():
        move()
    else:
        jump_right()
        
# Challenge 4 - Different jump heights 

def jump_check():
    safe = False
    number_of_jumps = 0
    while not safe:
        turn_left()
        move()
        turn_right()
        number_of_jumps += 1
        if front_is_clear():
            move()
            turn_right()
            for steps in range(number_of_jumps):
                move()
            turn_left()
            break

while not at_goal():
    if at_goal():
         break
    elif front_is_clear():
        move()
    else:
        jump_check()

 
