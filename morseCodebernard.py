#zane bernard 2/24/2018
#csc 131-005
#Dr. Ebrahimi
english_letters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N',\
                   'O','P','Q','R','S','T','U','V','W','X','Y','Z',)
morse_letters = ('.-','-..','-.-','-..','.','..-.','--.','....','..','.---',\
                 '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-',\
                 '...-','.--','-..-','-.--','--..',)
#functions
def welcome():
    print("This program will convert between English and Morse code.")
def english_prompt():
    print("Enter English message, one sentence per line")
    print("End each sentence with a period (hit return when done)")
def morse_prompt():
    print("Enter morse-coded letters one per line.")
    print("Include one blank line between words, and two blank lines between sentences.")
    print("(Enter 'q' when done)")
def e_interpret():
    message = input()
    decoded = []
    index_found = False
    for x in english_letters:
        if x in message:
            letter_index = english_letters.index[x]
            x = 0
            while x < len(morse_letters) and not index_found:
                if x == letter_index:
                    m_letter = morse_letter[x]
                    decoded.append(m_letter)
                    index_found = True
                else:
                    x = x + 1
        print(decoded)
        print(end=" ")
#def m_interpret():
#main body
welcome()
which = input("(E)nglish to Morse code, or (M)orse code to English: ")
if which == "E" or "e":
    english_prompt()
    e_interpret()
elif which == "M" or "m":
    morse_prompt()
else:
     welcome()
