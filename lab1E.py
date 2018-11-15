# Zane Bernard 1/17/2018
# CSC131-004
#
# Purpose: The goal of this program is to convert an integer into binary
#
# Variables:
#
# Algorithm:
#a) Pick a number between 0 and 31
#b) Create a variable to hold this number and store the number you have chosen in this
#   variable
#c) Use a print statement to print out to the screen to let the user know what number
#   you have chosen
#d) Now print out the message:
#       "the number in binary, with the digits in reverse order is:"
#e) Create a variable called remainder and assign the result of (number %2) to that
#   variable.
#       a. For example, remainder = number%2
#f) Now assign the result of number/2 to the variable number.
#       a. For example, number = number/2
#       b. It may look a little off that the same variable name is on both sides of the =
#       sign, but the division on the right side of the = sign will happen first and the
#       translator is smart enough to handle this.
#g) Print the value of the remainder
x=7
print("5 in binary, with the digits in reverse order is:")

remainder = x%2
number = x//2
print(remainder)

remainder1 = number%2
num2 = number//2
print(remainder1)

remainder2 = num2%2
num3 = num2//2
print(remainder2)

remainder3 = num3%2
num4 = num3//2
print(remainder3)

remainder4 = num4%2
num5 = num4//2
print(remainder4)
