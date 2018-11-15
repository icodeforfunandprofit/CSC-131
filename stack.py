def getStack():
    '''Creates and returns an empty stack'''
    return []

def isEmpty(s):
    '''Returns True if stack empty, otherwise returns False'''
    if s == []:
        return True
    else:
        return False

def top(s):
    '''Returns the top item of stack, item not removed'''
    try:
        return s[len(s)-1]
    except:
        print("Stack is Empty, can't return the top element!")

def push(s, item):
    '''Pushes item on the top of stack'''
    s.append(item)

def pop(s):
    '''Removes and returns top item of stack.
    If stack empty, raises a ValueError.
    '''
    try:
        item = s[len(s)-1]
        del s[len(s)-1]
        return item
    except:
        print("Stack is Empty, can't delete from it!")

def peek(s, item):
    '''Returns True if item on stack, otherwise returns False.'''
    if item in s:
        return True
    else:
        return False
