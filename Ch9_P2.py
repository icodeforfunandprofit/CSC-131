# Chapter 9 - Exercise P2
#Robert Deckelbaum and Zane bernard
#CSC-131

def moderateDays(week_temps):

    """ Passed a dictionary containin the average daily temperature for all
        the days of a given week, and returns a list containing the days of
        the week in which the average temperature was between 70-79 degrees.
    """
    mod_days = []
    
    for k in week_temps:
        if week_temps[k] > 70 and week_temps[k] < 79:
            mod_days.append(k)

    return mod_days

def main():
    daily_temps = {'sun': 68.8, 'mon': 70.2, 'tue': 67.2, 'wed': 71.8,
              'thur': 73.2, 'fri': 75.6, 'sat': 74.0}
    daynames = {'sun': 'Sunday', 'mon': 'Monday', 'tue': 'Tuesday',\
            'wed': 'Wednesday', 'thur': 'Thursday', 'fri': 'Friday', \
            'sat': 'Saturday'}

    mod_days = moderateDays(daily_temps)
        
    print(mod_days)



main()
