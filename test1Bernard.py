#Zane Bernard CSC-131 #004
#welcome screen
print("Problem: Sums a Series of Numbers and Calculates Their Average!")
#define variables
current = 0
total = 0
counter = 0
#while statement determines when to quit (in this case, when "" is entered)
while current != "":
#gets input
    current = input("Enter first number (press 'enter key' to quit): ")
    while current != "":
#start counter
        counter = counter + 1
#convert current into an integer
        integer = int(current)
#store the current into a continuous total
        total = total + integer
#get new input
        current = input("Enter a number: ")
#print results
print("Sum:",int(total))
print("Average:",int(total/counter))
