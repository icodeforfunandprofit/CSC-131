# main file to look for palinfrome words

from palindrome import palindromeChecker


def main():
    # sample palindrome words: moon, Anna

    print('This program takes a word and checks it to see if',
          'the word is palindrome.')

    flag = 'y'
    while flag.lower() == 'y':
        word = input('Input a word: ')
    
        if palindromeChecker(word.lower()):
            print('>>>', word,'is Palindrome.\n')
        else:
            print('>>>', word, 'is not Palindrome.\n')

        flag = input('Do you want to continue (y/n)? ')
        print('___________________________')
        print()

    # print out the docstring
    print(palindromeChecker.__doc__)
    
main()
