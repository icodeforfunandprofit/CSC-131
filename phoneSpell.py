
def getPhoneSpell():
    """ Return entered phone spell in the form 123-456-abcd """

    # prompt for phone input value: ex. 123-456-abcd and check if in valid form
    valid_input = False

    #handles invalid input
    while valid_input == False:
        input_number = input('Enter a phone number in spelled form (e.g. 123-456-abcd): ')

        #checks the numbers, letters, length, and dashes       
        if input_number[0:3].isdigit() and input_number[4:7].isdigit() and input_number[8:12].isalpha()\
        and input_number[3] == '-' and input_number[7] == '-' and len(input_number) == 12:

            valid_input = True
            
        else:
            valid_input = False
            
    #returns the valid input
    return input_number
def displayPhoneNumber(s):
    """ Display the possible phone number with the last four
        character replaced with the corresponding number from
        the phone keys.
    """

    #creates a dictionary that defines which letters correspond to which numbers
    digit_to_alpha = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', \
                      'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', \
                      'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9', \
                      'y': '9', 'z': '9'}

    #creates an empty string
    new_number = ''

    #translates 
    for k in range(len(s)):
        if s[k].isalpha():
            
            #adds the translated letter onto the string
            new_number = new_number + digit_to_alpha[s[k]]

    
    print(s[0:8]  + new_number)
