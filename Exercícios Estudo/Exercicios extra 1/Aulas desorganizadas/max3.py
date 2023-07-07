#To find the biggest of 4 numbers

x1 = float(input("number1? "))
x2 = float(input("number2? "))
x3 = float(input("number3? "))
x4 = float(input("number4? "))

if x1>x2: mx1 = x1

else: mx1 = x2 

if x3>x4: mx2 = x3

else: mx2 = x4

if mx1>mx2: mx = mx1

else: mx = mx2

print("-----------------")
print("Maximum:", mx)