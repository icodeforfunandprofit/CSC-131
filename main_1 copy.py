def main():
    import reduceWhitespace

    file_name = input('Enter a file name: ')
    input_file = open(file_name, 'r')

    line = input_file.readline()

    new_line = reduceWhitespace.reduceWhitespace(line)
    print(new_line)

    input_file.close()
    
main()
