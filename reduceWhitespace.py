def reduceWhitespace(line):
    no_space = line.split(' ')
    new_line = ''
    for k in no_space:
        if k != '':
            new_line = new_line + k + ' '

    return new_line
