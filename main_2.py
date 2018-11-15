def main():
    import countAllLetters

    file_name = input('Enter a file name: ')
    input_file = open(file_name, 'r')
    
    line = input_file.readline()
    
    list_count = countAllLetters.countALLLetters(line)
    
    print(list_count)

    input_file.close()

main()
