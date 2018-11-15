# Ellie Ebrahimi 1/12/2018
# CSC131-004
#
# Purpose: The goal of this program is to enter a four digit binary number and display the number in base 10
#
# Variables: x,y,z,a
#
# Algorithm: 1) collect inputs for the four digits and assign variables to them
#               2) create an if statement that has a condition of 1 or 0 for the appropraite digit
#               3) add them together
first = int(input("Enter the leftmost digit"))
second = int(input("Enter the next digit"))
third = int(input("Enter the next digit"))
forth = int(input("Enter the next digit"))

if first==1:
    x = 8
else:
    x = 0
    
if second==1:
    y = 4
else:
    y = 0
    
if third==1:
    z = 2
else:
    z = 0
    
if forth==1:
    a = 1
else:
    a = 0
    
print(x+y+z+a)
