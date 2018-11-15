#import classfile multitemp (celcius, kelvin, farhen)
from multitempclass import *

#create a list of objects that are different temperature types
temps = [Farhenheit(75), Celsius(40), Kelvin(320), Kelvin(350), Farhenheit(45), Celsius(27)]

print('------ Temperatures in Fahrenheit, Celsius and Kelvin------------')
for item in temps:
    print(item)
#tell me if the temperatures are above freezing or not

print('------ All temperatures in Fahrenheit------------')
#loop through the entire list, creating a new list,
# where you have converted everything to Fahrenheit
#tell me if the temperatures are above freezing or not

print('------ All temperatures in Celsius------------')
#loop through the entire list, creating a new list,
# where you have converted everything to Celsius
#tell me if the temperatures are above freezing or not

print('------ All temperatures in Kelvin------------')
#loop through the entire list, creating a new list,
# where you have converted everything to Celsius
#tell me if the temperatures are above freezing or not

