# Reeborg's World - Maze Challenge

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
def at_goal():
    print("Are you at goal?")
def front_is_clear():
    print("Is there no wall in front of you?")
def right_is_clear():
    print("Is there no wall to the right of you?")

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        
     
        
    

