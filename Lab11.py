#CSC-131 Dr. Ebrahimi
#Zane Bernard

def displayBackwards(s):
    '''
        Reverses the order, and returns the string back.
    '''
    #creates a list to store the characters
    backward = []

    #assign a value for length so the 'last term' can increment down
    last_term = len(s)
    for k in s:
        backward.append(s[last_term -1])

        #makes the 'last term' one before the last after each iteration
        last_term -= 1

    #joins the list into one string
    return ''.join(backward)

def displayBackwards_r(s):
    '''
        Reverses the order, and returns the string back.
    '''
    
    if s == '':         #exits the recursion once the string passed is empty
        return s   
    #cuts off the first letter each time until string is empty, then
    #concatenates the first letter in reverse order, returning the string
    #'backwards'
    else:
        return displayBackwards(s[1:]) + s[0]

def exponentiation(x,y):
    '''
        Raises x to the power of y and returns the answer.
    '''
    z = x**y

    return z

def exponentiation_r(x,y):
    '''
        Raises x to the power of y and returns the answer.
    '''

    #exits recursion once the y value reaches 0
    if y == 0:
        return 1
    #returns y back up the stack to be multiplied by 3 again each time
    else:
        return x*exponentiation(x,y-1)

def displayAsterisks(num):
    '''
        Prints descending rows of asterisks determined by the number that
        is passed.
    '''

    while num > 0:
        print('{:^30}'.format('*'*num))
        num -= 2
def displayAsterisks(num):
    '''
        Prints descending rows of asterisks determined by the number that
        is passed.
    '''
    
    if num == 0:
        return 0
    else:
        return num - displayAsterisks(num-2)
        











    
