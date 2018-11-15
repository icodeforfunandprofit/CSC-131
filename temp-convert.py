# Temperature Conversion Program (Celsius-Fahrenheit / Fahrenheit-Celsius)

# Display program welcome
def welcome():
    print('This program will convert temperatures (Fahrenheit/Celsius)')
    print('Enter (F) to convert Fahrenheit to Celsius')
    print('Enter (C) to convert Celsius to Fahrenheit')

def tempConvert(which, temp):
    # Determine temperature conversion needed and display results
    if which == 'F':
        converted_temp = format((temp - 32) * 5/9, '.1f')
        #print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
        
    else:
        converted_temp = format((9/5 * temp) + 32, '.1f')
        #print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')

    return converted_temp



welcome()
print()
# Get temperature to convert
which = input('Enter selection: ')
temp = int(input('Enter temperature to convert: '))

converted = tempConvert(which)
print(converted)



