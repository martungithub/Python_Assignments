def guess_enough(value, target):

    '''guess_enough(value,target) function determins the accuracy'''

    if abs(value**3 - target) < 0.0001:

        return True

    else:

        return False

def abs(n):

    '''abs(n) function returns the absolute value of a number'''

    if n > 0:

        return n

    else:

        return -n

def improve(root, target):

    '''Improves the estimate of the root'''

    return ((target / (root ** 2)) + (2 * root)) / 3

def cube(n):

    '''This is the main cube(n) function which calculates
    cube root of a given number.
    '''

    root = 1

    while not guess_enough(root, n):

        root = improve(root, n)

    return root

number = 8

#Function call
print("Cube root of" , number, ":", cube(number))
