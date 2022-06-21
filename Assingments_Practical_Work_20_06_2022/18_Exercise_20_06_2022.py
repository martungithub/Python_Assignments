import math

s1 = float(input("Insert s1: "))
s2 = float(input("Insert s2: "))
s3 = float(input("Insert s3: "))
s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
print("Area: ", area)
