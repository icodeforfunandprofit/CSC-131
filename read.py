def reduceWhitespace(line):
    no_space = line.split(' ')
    new_line = ''
    for k in no_space:
        if k != '':
            new_line = new_line + k + ' '

    return new_line

def countAllLetters(line):
    line = line.lower()
    counter = []
    temp = []
    for k in line:
        if k != ' ' and k not in temp:
            temp.append(k)
            counter.append([k, line.count(k)])            

    return counter

def main():
    line = input('Enter a string: ')
    new_line = reduceWhitespace(line)
    print(new_line)
    
    line = input('Enter a string: ')
    list_count = countAllLetters(line)
    print(list_count)

main()
