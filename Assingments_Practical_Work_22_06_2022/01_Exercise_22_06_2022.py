words = []
unique = []
inputs = ' '

while inputs != '':
    inputs = input("Enter Name, or enter to quit': ")
    words.append(inputs)

[unique.append(i) for i in words if i not in unique]
unique = unique[:-1]
[print(i) for i in unique]
