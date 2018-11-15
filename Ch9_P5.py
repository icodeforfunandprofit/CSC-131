# Chapter 9 - Exercise P5

def addVegetable(vegs, veg_name):

    """ Passed a set of vegatables in vegs, and a vegetable name to add,
        and return returns a new set with the vegatable name added, it not
        already in the set, andraises a ValueError exception otherwise.
    """
    if veg_name in vegs:
        raise ValueError
    else:
        vegs.add(veg_name)

def main():

    vegs = set()
    terminate = False

    while not terminate:
        veg_name = input("Enter a vegetable name: ")
        addVegetable(vegs, veg_name)

        response = input('\nContinue with another day? (y/n): ')
        if response == 'n':
            terminate = True

    print(vegs)

main()
