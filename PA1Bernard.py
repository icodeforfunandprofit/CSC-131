#Zane Bernard CSC-131 #005
#3/2/2018
#Welcome Screen
print("Let's Play of Game of Lucky Seven!")
print("2 dice will roll. If the dots add up to 7, you win $4. Else, you lose $1")
print("There are lots of ways to win! (e.g. 1 and 6, 2 and 5, etc.)")
#get input
money = int(input("Enter amount into the pot: $"))
#initialize variables
counter = 0
lst = []
import random
#loop runs as money is still in the pot
while money > 0:
#roll two random dice
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
#actions when the roll is equal to 7
    if (die_1 + die_2) == 7:
        money = money + 4
        counter = counter + 1
        print("Number of Rolls:",counter)
        print("First Roll:",die_1)
        print("Second Roll:",die_2)
        print("You Have: $",money)
        lst.append(money)
        print(format('.', '.<80'))
#actions when the roll is not equal to 7
    elif (die_1 + die_2) != 7:
        money = money - 1
        counter = counter + 1
        print("Number of Rolls:",counter)
        print("First Roll:",die_1)
        print("Second Roll:",die_2)
        print("You Have: $",money)
        lst.append(money)
        print(format('.', '.<80'))
#results
print("Number of Rolls:",counter)
print("Highest amount won: $",max(lst))
