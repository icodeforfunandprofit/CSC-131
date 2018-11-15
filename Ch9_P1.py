# Chapter 9 - Exercise P1

def addDailyTemp(week_temps, dayofweek, temp):

    """ Udpates the temperatures of a particular week in dictionary
        week_temps with the provided dayofweek and average temperature
        of that day.
    """



    


def main():
    print('This program will store the average temperature for a given day')
    terminate = False
    week_temps = dict()

    daynames = {'sun': 'Sunday', 'mon': 'Monday', 'tue': 'Tuesday',\
                'wed': 'Wednesday', 'thur': 'Thursday', 'fri': 'Friday', \
                'sat': 'Saturday'}

    while not terminate:
        day = input("Enter 'sun', 'mon', 'tue', 'wed', 'thur', 'fri', or 'sat': ")
        print("Enter the temperture for", daynames[day], end=": ")
        temp = input("")

        addDailyTemp(week_temps, day, temp)
        
        response = input('\nContinue with another day? (y/n): ')
        if response == 'n':
            terminate = True

    print(week_temps)



main()
