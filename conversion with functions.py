#Zane Bernard and Nikolas Young
#2/23/2018
#CSC131-005
#define functions
def display_welcome():
    print('This program converts temperature (F<->C)')
    print("Enter 'F' to convert F->C'")
    print("Enter 'C' to convert C->F'")
def conversion(selection,temp):
    if selection == 'F':
        converted_temp = (temp - 32) * 5/9
        print(converted_temp)
    elif selection == 'C':
        converted_temp = (temp *9.5) + 32
        print(converted_temp)
#main program
display_welcome()
selection = input('Enter Selection: ')
starting_temp = int(input('Enter staring temperature: '))
ending_temp = int(input('Enter ending temperature: '))
print(format('Degree', '^15') *2)
print(format('Farenheit', '^15'), format('Celsius', '^15'))

while starting_temp <= ending_temp:
    converted = conversion(selection, starting_temp)
    print(format(starting_temp, '^15'), format(converted, '^15'))
    starting_temp = starting_temp + 1
