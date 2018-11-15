#Zane Bernard and Jared Wright 2/2/2018
#CSC131-004
#
#Purpose: The goal of this program is enter a number of coin values that add
#         up to a displayed target value.
#Welcome screen
print("Enter coin values as 1-penny, 5-nickel, 10-dime and 25-quarter.")
print("Hit return after the last entered coin value")
#format
print(format("-", "->20"))
#--------------------------------------------------------------------------------
#import random
import random
amount = random.randint(1,99)
print("Enter coins that add up to", amount, "cents, one per line.")
#--------------------------------------------------------------------------------
#get input for first coin
sum_value = int(input("Enter first coin: "))
#user input happens to have the exact amount necessary
if sum_value == amount:
        print("Success... It will be equal to", amount, "cents.")
        print("Finished.")
#user goes over the amount (most likely a small amount)
if sum_value > amount:
        print("Sorry - you entered", sum_value,"cents.")
        restart = input("Try again? Enter y/n: ")
        if restart == "y":
            sum_value = 0
        elif restart == "n":
            print("Have a nice day!")
        elif restart != "y" or "n":
            print("Invalid input!")
#user inputs something other than the correct coins needed
if sum_value != 1 or 5 or 10 or 25:
    print("Invalid input!")
    restart = input("Try again? Enter y/n: ")
    if restart == "y":
            sum_value = 0
    elif restart == "n":
            print("Have a nice day!")
            quit = 1
    elif restart != "y" or "n":
            print("Invalid input!")
            quit = 1
#--------------------------------------------------------------------------------
#loop input
while sum_value < amount:
#quit function to exit loop
    if quit == 1:
        sum_value = 100
    current = int(input("Enter next coin: "))
    sum_value = sum_value + current
#user gets answer right-exits loop
    if sum_value == amount:
        print("Success... It will be equal to", amount, "cents.")
        print("Finished.")
#directs from quit function to exit loop
    if sum_value > amount:
        if sum_value == 100:
            print("Have a nice day!")
#user goes over
        else:
            print("Sorry - you entered", sum_value,"cents.")
#restart function
            restart = input("Try again? Enter y/n: ")
            if restart == "y":
                sum_value = 0
            elif restart == "n":
                print("Have a nice day!")
            elif restart != "y" or "n":
                print("Invalid input!")
#-----------------------------------------
