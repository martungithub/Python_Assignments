def sum(a,b):

    '''Defining the sum(a,b) function.
    It will print sum of numbers from a to b if a < b
    otherwise will print the sum of numbers from b to a'''

    # The sum variable will keep the value of sum of numbers
    sum = 0

    if(a < b):
        while (a <= b):
            sum += a
            a += 1

    elif(a >= b):
        while (b <= a):
            sum += b
            b += 1
    return sum

#Function call
print("Sum of numbers: ",sum(5,5))