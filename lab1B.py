# Zane Bernard 1/12/2018
# CSC131-004
#
# Purpose: The goal of this program is to enter an integer value and display the value 2 raised to that integer
#
# Variables: x,y
#
# Algorithm: input a number and use the value stored into the variable into the math function
#
import math
number = int(input("What power of two?:"))
x = 2
y = number
print(int(math.pow(x,y)))
