#-----------------------------------------------------------------------------------------------------------------#
#Zane Bernard CSC-131 #004
#welcome screen
print("Problem 2: sums a series of positive integers")
#get first input
first_num = int(input("Enter first number to sum (enter -1 to quit): "))
#define the variables for the loop
current = 0
total = 0
#loop the addition
while current != -1:
#if loop that determines whether to add to the first number or move onto the next number (only when current is 0)
    if current == 0:
        total = first_num + current
    elif current < 100:
        total = total + current 
    current = int(input("Enter next number: "))
#print results
print("Total is", total)
