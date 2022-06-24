my_tuple = (1, 2, 3)
number = 0
for i in range(len(my_tuple)):
    number += my_tuple[i] * 10 ** (len(my_tuple) - i - 1)
print(number)
