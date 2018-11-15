def valid_input():
    '''opens input file while handing invalid input.'''
    
    file_name = input('Input file name: ')      #user inputs file
    valid = False                               #flag for invalid input

    #handles invalid input
    while not valid:
        try:
            input_file = open(file_name, 'r')   #try to open the file
            valid = True                        #if it succeeds, the flag is flipped
        except IOError:         #for when there is an error, the program doesn't crash
            file_name = input('File not found. Try again: ')
    
    return input_file           #returns input_file for use
            
def valid_output(filename):
    '''opens output file while handling invalid input.'''

    file_name = input('Output file name: ')
    valid = False

    while not valid:
        try:
            output_file = open(file_name, 'w')     #'r+' = reads and writes
            valid = True
        except IOError:
            file_name = input('File not found. Try again: ')

    filename.append(file_name)
    return output_file          #returns output_file for use

def get_all_placeholders(word):
    '''formats the placeholder correctly, asks for input based on that placeholder
    and returns the input back as a string.'''
    
    base = word.strip('<>')                     #gets rid of '<>'
    placeholder = base.replace('-', ' ')        #gets rid of '-'
    print('Enter a(n) '+ placeholder)           
    new_word = input('>>> ')                    #gets input based on placeholder
    return (new_word + ' ')                     #returns word with ' ' for formatting

def display(output_file, display, filename):
    '''gives the user a choice to either read the output file back or close the
    file.'''
    
    print('Would you like to see the result (y/n)?')
    output = input('>>> ')
    if output == 'y':
        output_file.close()                     #closes file
        output_file = open(filename[0], 'r')    #reopens it for reading
        print(output_file.read())               #reads and displays
        return True                 #return True for valid input 
    elif output == 'n':
        return True
    else:
        print('Invalid input!')
        return False                #return False for invalid input
    
                
