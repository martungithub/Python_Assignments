number = int(input("Insert the number: "))
number_str = ""
while number != 0:
    number_str += str(number % 10)
    number = number // 10
print(int(number_str))
