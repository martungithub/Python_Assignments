def pow(base, exp):

    '''Defining the pow(base,exp) funtion which will calculate
    the nth power of a number. The exp can also be negative '''
    
    #Res variable will keep the result
    res = 1
    count = 0

    while count < abs(exp):

        if(exp > 0):

            res = res * base

        elif(base != 0 and exp < 0):

            res = (1 / base ** (-exp))

        else:

            res = "Dividing by zero is undefined"

        count += 1

    return res

base = 0
exp = -2

#Function call
print(pow(base,exp))