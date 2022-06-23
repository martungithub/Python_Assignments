numbers = []
inputs = ' '
answer = 0
while inputs != '':
    inputs = input("Enter Numbers: ")
    numbers.append(inputs)
numbers.pop()
numbers = [int(i) for i in numbers]
avarage = sum(numbers) / len(numbers)
for i in numbers:
    if i < avarage:
        print(i, " < ", avarage)
    elif i > avarage:
        print(i, " > ", avarage)
    else:
        print(i, " = ", avarage)



