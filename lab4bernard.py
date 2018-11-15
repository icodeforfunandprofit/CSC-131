####################################################################################################################
#Zane Bernard CSC-131 #004
print("Problem 1: while loop that adds up even numbers between 100 and 200")
#define variables for the counter
current = 100
count = 0
total = 100
#up to 50 for even numbers within 100-200
while count < 50:
#store the sum
      current = current + 2
      total = current + total
#increment the counter
      count = count + 1
#print the results
print("Total equals",total)
