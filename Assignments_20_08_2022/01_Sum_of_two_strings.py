def sum_of_numbers(number1, number2):
    sum_of_nums = 0
    carry = 0
    result = ""

    if len(number1) > len(number2):
        number2 = "0" * (len(number1) - len(number2)) + number2

    elif len(number2) > len(number1):
        number1 = "0" * (len(number2) - len(number1)) + number1

    for i in range(len(number1) - 1, -1, -1):
        sum_of_nums = int(number1[i]) + int(number2[i]) + carry
        carry = sum_of_nums // 10
        result += str(sum_of_nums % 10)
    result = result[::-1]
    return result


number1 = input("Number 1: ")
number2 = input("Number 2: ")
print("Sum: ", sum_of_numbers(number1, number2))
