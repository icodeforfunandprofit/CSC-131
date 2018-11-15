########################################
#Zane Bernard 1/22/2018
#Section 004
#Problem 1: Prompt user input for 2 integer values, divide them, and then display
#           the result with 3 decimal places
print("Input Two Integer Values:")
firstInt = int(input())
secondInt = int(input())
x = (firstInt/secondInt)
print("When Divided, the Answer is:", format(x,'.3f'))

#Problem 2: Prompt user input for 2 float values, divide them, and then display
#           the result with 5 decimal places
print("Input Two Float Values: ")
firstFloat = float(input())
secondFloat = float(input())
x = (firstFloat/secondFloat)
print("When Divided, the Answer is:", format(x,'.5f'))

#Problem 3: Prompt user input for 2 float values, divide them, and then display
#           the result with 6 decimal places in scientific notation
print("Input Two Float Values Again Please :-)")
firstFloat = float(input())
secondFloat = float(input())
x = (firstFloat/secondFloat)
print("When Divided, the Answer is:", format(x, '.6e'))

#Problem 4: Prompt user input for an uppercase or lowercase letter and then
#           display the corresponding unicode
print("Enter an Uppercase or a Lowercase Letter. Your Choice!")
letter = input()
print ("The Unicode Equivalent is:", ord(letter))
#Problem 5: Prompt user input for two integer values and execute 7 basic math
#           operations: +,-,*,/,//,%,**
print("Last Time! Enter Two Integer Values. Math Magic Will Begin Soon:")
x = int(input())
y = int(input())
print("Add!", x+y)
print("Subtract!", x-y)
print("Multiply!", x*y)
print("Divide!", x/y)
print("Without Remainder!", x//y)
print("There's That Remainder!", x%y)
print("Exponent!", x**y)
