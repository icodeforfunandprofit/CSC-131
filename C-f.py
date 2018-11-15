#Zane Bernard 1/31/2018
#CSC131-004
#
#Purpose: The goal of this program is to convert Celcius into Farenheit
# Display program welcome
print('This program converts temperature (F<->C)')
print("Enter 'F' to convert F->C'")
print("Enter 'C' to convert C->F'")
#Get temp to convert
which = input('Enter selection: ')
temp = int(input('Enter temperature to convert: '))
#Determine conversion and display results
if which == 'F':
    converted_temp = (temp - 32) * 5/9
    print(temp, 'degree in Farenheit equals', converted_temp, 'degrees Celsius')
else:
    if which == 'C':
        converted_temp = (temp *9.5) + 32
        print(temp, 'degree in Celsius equals', converted_temp, 'degrees Farenheit')
    else:
        print("Enter a valid input ('F' or 'C')")
