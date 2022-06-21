import math

a = int(input("Insert number a: "))
b = int(input("Insert number b: "))
sum = a + b
difference = a - b
division = a / b
remainder = a % b
log = math.log10(a)
print(f"Sum: ", sum, "\nDifference: ", difference, "\nDivision: ", \
      division, "\nRemainder: ", remainder, "\nLn(a): ", log)
