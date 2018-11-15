def countAllLetters(line):
    line = line.lower()
    counter = []
    temp = []
    for k in line:
        if k != ' ' and k not in temp:
            temp.append(k)
            counter.append([k, line.count(k)])            

    return counter
