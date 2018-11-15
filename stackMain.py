def main():
    import stack

    mystack = stack.getStack()

    for item in range(1, 5):
        stack.push(mystack, item)
        print('Pushing', item, 'on stack')
        peek = stack.peek(mystack, (int(input('Enter an element you want to peek into the stack: '))))
        if peek == True:
            print('Element is in stack')
        else:
            print('Element is not in stack')

    while not stack.isEmpty(mystack):
        item = stack.pop(mystack)
        print('Popping', item, 'from stack')

main()
