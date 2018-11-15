import turtle
import random

def random_direction(window, drunkard):
    """sets a random direction for the turtle: forward, backward,
    left, or right (relative to the starting position). Returns
    this direction as a degree."""
    
    degree_turn = random.randrange(0, 360, 90)
    
    return degree_turn

def convert_time(input_time, speed):
    """takes the input speed given by the user and changes its value
    relative to the speed (e.g. the time must be longer if the speed
    is quicker to compensate for the shorter time between turns in the
    while loop). Returns the new converted time."""
    time = input_time * speed
    return time

def main():

    #Window setup
    screen_width=800
    screen_height=800
    turtle.setup(screen_width,screen_height)
    window = turtle.Screen()
    window.title("DRUNKARD'S WALK")
    drunkard = turtle.getturtle()
    drunkard.penup()
    drunkard.setposition(0,0)
    
    #Define shape
    drunkard.shape("circle")
    
    #Welcome Screen
    print("This program simulates a random (Drunkard's) walk")
    
    #User sets the time
    input_time = int(input("Enter number of seconds to run: "))
    
    #User sets the speed
    print("Enter speed (1-slow, 2-faster, ..., 10-fastest:)")
    speed = int(input("Enter speed (1-slow, 2-faster, ..., 10-fastest): "))
    drunkard.speed(speed)
    
    #call function to convert speed
    time = convert_time(input_time, speed)
    
    #allows the walk to continue until the time depletes.
    while time > 0:

        #call random_direction to set a random direction
        degree_turn = random_direction(window, drunkard)

        #move drunkard
        drunkard.pendown()
        drunkard.left(degree_turn)
        drunkard.forward(10)

        #increment the time
        time = time - 1
        
main()
     

