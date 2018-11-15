def drawX(my_turtle):
    my_turtle.up()
    my_turtle.setposition(-400,300)
    my_turtle.down()
    my_turtle.setposition(400,-300)
    my_turtle.up()
    my_turtle.setposition(400,300)
    my_turtle.down()
    my_turtle.setposition(-400,-300)

def drawW(my_turtle):
    my_turtle.up()
    my_turtle.setposition(-100,0)
    my_turtle.down()
    my_turtle.right(45)
    for i in range (0,2):
        my_turtle.forward(70.7106781187)
        my_turtle.left(90)
        my_turtle.forward(70.7106781187)
        my_turtle.right(90)

def movingTurtle(my_turtle):
    my_turtle.up()
    my_turtle.setposition(0, -300)
    turtle.resizemode('user')
    stretch_wid = 20
    stretch_len = 20
    my_turtle.setheading(90)
    my_turtle.shapesize(stretch_wid, stretch_len)
    while my_turtle.ycor() < (300):
        my_turtle.forward(15)
        my_turtle.shapesize(stretch_wid,stretch_len)
        stretch_wid = stretch_wid - .5
        stretch_len = stretch_len - .5
import turtle

def main():
   # set window size
    screen_width = 800
    screen_height = 600
    turtle.setup(screen_width,screen_height)

    # get reference to turtle window
    window = turtle.Screen()
    
    # set window title bar
    window.title('Lab 7')
    my_turtle = turtle.getturtle()

    drawX(my_turtle)

    drawW(my_turtle)

    movingTurtle(my_turtle)

    turtle.exitonclick()


main()
