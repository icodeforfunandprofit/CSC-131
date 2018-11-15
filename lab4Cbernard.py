#--------------------------------------------------------------------#
#Zane Bernard CSC-131 #004
#welcome screen
print("Problem 3: counts the number of positive and negative numbers")
#get input
current = input("Enter a number (enter 'q' to quit): ")
#define variables for loop
current = 0
pos_val = 0
neg_val = 0
#loop kills if q is entered
while current != "q":
#convert current into integer, and increment pos or neg by 1 if conditions are met
    if int(current)>=0:
        pos_val = pos_val+1
    else:
        neg_val = neg_val+1
    current = input("Enter a number: ")
#print results
print("Number of positive values entered:", pos_val)
print("Number of negative values entered:", neg_val)
