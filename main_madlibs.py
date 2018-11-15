#Zane Bernard
#CSC 131-005
import ml

def main():
    madlibs = True                  #game runs while flag is True
    print('Welcome! This is a MadLibs program. You will enter in two files: ')
    print()
    print('Your first file will be the template, and the second file will\n'
          'store your answers in the corresponding placeholders.')
    print()

    filename = []           #stores the filename to be used later
    
    while madlibs == True:          #controls termination
        #input the two text files 
        input_file = ml.valid_input()
        output_file = ml.valid_output(filename)

        line = input_file.readline()        #reads line
        allstrings = line.split(' ')        #splits words into strings in a list
        
        #iterates through the list and gets placeholders
        for i in allstrings:
            if '<' in i and '>' in i:                   #checks if the word is a placeholder
                new_word = ml.get_all_placeholders(i)   #calls function to replace placeholder with user input
                output_file.write(new_word)             #writes the input to the output_file
            else:
                i = i + ' '                             #space for formatting
                output_file.write(i)                    #writes to output_file
        
        display = False                     #flag for invalid input

        #handles invalid input for displaying the output_file
        while not display:
            display = ml.display(output_file, display, filename) #displays the output_file

        #gives the user choice to process another file                
        
        invalid = True
        while invalid:
            restart = input('Would you like to process another MadLib File (y/n)? ')
            if restart == 'y':
                madlibs = True      #while loop keeps going
                invalid = False
            elif restart == 'n':
                madlibs = False     #while loop terminates
                invalid = False
            else:
                print('Invalid input!')
                invalid = True

        #closes files for buffer
        input_file.close()
        output_file.close()
        
main()
        

    
    
