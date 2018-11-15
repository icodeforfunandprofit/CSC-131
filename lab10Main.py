#Zane Bernard CSC-131

# main
from phoneSpell import * 

def main():

    # Program welcome
    print('-'*51)
    print('This program allows the user to enter a spelled')
    print('phone number for the last four digits and generates')
    print('the phone number that produces that spelling')
    print('-'*51)

    # get phone number and display spelling
    terminate = False

    while not terminate:
        phone_spell = getPhoneSpell()
        displayPhoneNumber(phone_spell)

        # Continue
        response = input('\nEnter another phone spell? (y/n): ')
        if response.lower() == 'n':
            terminate = True


main()


