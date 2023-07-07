from cmath import sqrt
import math

a = int(input("cateto A: "))
b = int(input("cateto B: "))
c = sqrt(a**2 + b**2)

alpha = math.acos(a/c) * 180


print(c)
