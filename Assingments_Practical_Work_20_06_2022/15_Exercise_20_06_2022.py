import math

r = float(input("Insert r: "))
h = float(input("Insert h: "))
volume = math.pi * r ** 2 * h
print(f"Volume: {format(volume,'.1f')}")
