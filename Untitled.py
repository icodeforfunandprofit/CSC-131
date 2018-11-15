# Zane Bernard 1/12/2018
# CSC131-004
#
# Purpose: The goal of this program is to enter an integer value for power and base and print the result
#
# Variables: x,y
#
# Algorithm: use input for variable x 
#
import math
number = (int(input("What base?")))
x = number
number2 = (int(input("What power of" + str(x))))
y = number2
print(int(math.pow(x,y)))
