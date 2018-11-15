def main():
    import countAllLetters  #import module

    file_name = input('Enter a file name: ')
    input_file = open(file_name, 'r')   #opens a .txt file
    
    line = input('Enter a string: ')
    
    list_count = countAllLetters.countALLLetters(line)  #returns the mode of string
    
    print(list_count)
    input_file.close()  #closes .txt file
    
main()
