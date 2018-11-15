def valid_input():
    file_name = input('Input file name: ')
    valid = False
    
    while not valid:
        try:
            input_file = open(file_name, 'r')
            valid = True
        except IOError:
            file_name = input('File not found. Try again: ')

    return input_file
            
def valid_output():
    file_name = input('Output file name: ')
    valid = False

    while not valid:
        try:
            output_file = open(file_name, 'w')
            valid = True
        except IOError:
            file_name = input('File not found. Try again: ')

    return output_file

def strip_placeholder(line):
    if '<' in line and '>' in line:
        placeholder = line.strip('<>')

    return placeholder
