#drunkbird
#Nikolas Young
#3/28/18
#This program moves the turtle(Drunk_Man), which i changed to be an image of a bird
#(kiwi). the program simulates a random walk of a drunk person which i chan


import turtle
import random

def random_walk(Seconds,Speed,Drunk_Man,window):
    Drunk_Man.penup()
    Drunk_Man.setposition(0,0)
    Drunk_Man.pendown()

    while Seconds>0: 
#determines random angle
        New_location=[]
        Direction= random.randint(0,3)
#0 degree 
        if Direction== 0:
            Direction=0
        elif Direction == 1:
#90 degree
            Direction = 90
        elif Direction == 2:
#180 degree
            Direction = 180
        elif Direction == 3:
#270 degree
            Direction = 270
        else:
            Direction = 360

#determines random distance
        A=range(0,10) 
        Distance= random.randrange(5,10,5)
#packages direction and distance into one string
        New_location.append(Direction)
        New_location.append(Distance)
#sends info to update walk which draws a new line
        update_walk(New_location,Drunk_Man,Speed,window)
#counter goes down by one till o
        Seconds=Seconds-1

def update_walk(New_location,Drunk_Man,Speed,window):

#takes random direction an distance from random walk
    Direction=New_location[0]
    Distance=New_location[1]    

#speed of turtle
    Drunk_Man.speed(Speed)
#pen size/color
    Drunk_Man.pensize(1)
    Drunk_Man.shapesize(.5,.5,.5)
    turtle.colormode()
    Drunk_Man.pencolor("red")
#Determines if Object is out of bounds
    A= Drunk_Man.pos()
    X_pos= A[0]
    Y_pos=A[1]
    if  X_pos > 400:
        OutBound(Drunk_Man)
    elif X_pos < -400:
        OutBound(Drunk_Man)
    elif Y_pos > 400:
        OutBound( Drunk_Man)
    elif Y_pos < -400:
        OutBound( Drunk_Man)
    else:
        B=10
#Updates Movement of object
    Drunk_Man.left(Direction)
    Drunk_Man.forward(Distance)

#moves object back to center if it goes out of bounds
def OutBound(Drunk_Man):
    Drunk_Man.penup()  
    Drunk_Man.setposition(0,0)
    print("Drunk bird got lost, moved to center")
    Drunk_Man.pendown()
    



def main():

#Window setup
    screen_width=800
    screen_height=800
    turtle.setup(screen_width,screen_height)
    window = turtle.Screen()
    window.title('DRUNK BIRD')
    Drunk_Man = turtle.getturtle()
    Drunk_Man.penup()
    Drunk_Man.setposition(0,160)
    Drunk_Man.pendown()
    


    Drunk_Man.shape("circle")

#gretting
    print("This is the drunk simulator") 
#duration of flight
    print("Choose your character")
    print("1=Drunk bird 2=Drunk deer 3=Drunk man")
    Character=int(input(">"))
    print('Enter number of seconds to move')
    Seconds=int(input(">"))
    Seconds=Seconds*100
#Enter speed
    print("Enter speed (1-slow, 2-faster, ..., 10-fastest:)")
    Speed=int(input(">"))
    random_walk(Seconds,Speed,Drunk_Man,window)
    Speed=Speed*2
main()
     

