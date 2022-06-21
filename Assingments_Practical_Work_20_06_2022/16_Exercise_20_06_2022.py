import math

v = float(input("Insert the initial velocity(v): "))
d = float(input("Insert the distance: "))
a = 9.8
answer = math.sqrt(v ** 2 + 2 * a * d)
print("Answer: ", answer)
