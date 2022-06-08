def biggest_numbers(a,b,c):

    '''biggest_numbers(a,b,c) will find out two bigeest numbers
    and will print the sum of squares '''

    if(a <= b and a <= c): return pow(b + c,2)

    elif(b <= c and b <= a): return pow(a + c,2)

    else: return pow(a + b,2)

#Function call
print("Result: ",biggest_numbers(0,-1,-2))

