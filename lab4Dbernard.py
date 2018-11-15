#Zane Bernard CSC-131 #004
#welcome screen
print("Problem 4: nested while loops")
#define variables for the loop (set = 0)
row = 0
column = 0
current = 0
#loops for each row
while row<10:
#loops for each column within a numbered row
    while column<10:
#increments by 1 for the printed values and the column
        current = current + 1
        column = column + 1
#formatting and printing
        if row == 0 and current != 10:
            print("", current, end = "  ")
        elif current == 10 or row < 10 and current != 99:
            print(current, end = "  ")
        elif current == 99:
            print(current, end = " ")
#move to next line
    print("\n")
#increments row to move to next row
    row = row+1
#reset the column
    column = 0
    
