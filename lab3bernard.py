########################################
#Zane Bernard 1/31/2018
#
#Problem 1: Determine whether a triangle is an equilateral triangle or not
#Welcome Screen
print('Problem 1: Practice using if statement')
#Get inputs for sides
first_side = int(input('Enter the first side: '))
second_side = int(input('Enter the second side: '))
third_side = int(input('Enter the third side: '))
#Determine if triangle is equilateral
if first_side==second_side==third_side:
    print('The triangle is equilateral')
else:
    print('The triangle is not equilateral')
#................................................#
print() #this will print out a blank line before the next problem
#Problem 2: Display specific words for associated characters
#Welcome Screen
print('Problem 1: Practice using Nested Loops')
#Get input
answer = input("Enter 'A' for apple, 'B' for banana, and 'C' for coconut: ")
#Nested Loops
if answer == 'A' or answer =='a':
    print('Apple')
else:
    if answer == 'B' or answer =='b':
        print('Banana')
    else:
        if answer == 'C' or answer =='c':
            print('Coconut')
        else:
            print('invalid input')
#................................................#
print() #this will print out a blank line before the next problem
#Problem 3: Display specific words for associated characters
#Welcome Screen
print("Problem 3: Practice using ELIF Headers")
#Get input
answer = input("Enter 'A' for apple, 'B' for banana, and 'C' for coconut: ")
#ELIF Determination
if answer == 'A' or answer == 'a':
    print('Apple')
elif answer == 'B' or answer == 'b':
    print('Banana')
elif answer == 'C' or answer == 'c':
    print('Coconut')
else:
    print('invalid input')
