#Zane Bernard CSC 131 - 005
#03/28/2018
def palindromeChecker(word):
    """This function checks if a word is a palindrome. It does so by creating two
lists: one that represents the string forward, and another that represents the
string backward. Finally it checks the two strings to see if they are equal to
each other."""
    
    forward = []
    backward = []
    length = len(word)

    for k in range(len(word)):
        backward.append(word[length - 1])
        length = length - 1

    for k in word:
        forward.append(k)

    if forward == backward:
        return True
    
    else:
        return False
