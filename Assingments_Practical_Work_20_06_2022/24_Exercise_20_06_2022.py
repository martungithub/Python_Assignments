numbers = []
inputs = ''
while inputs != '0':
    inputs = input("Enter Name, or 0 to quit': ")
    numbers.append(inputs)
numbers = numbers[:-1]
answer = 0
for i in numbers:
    answer += int(i)
print("The arithmetic average։ ", answer / len(numbers))
