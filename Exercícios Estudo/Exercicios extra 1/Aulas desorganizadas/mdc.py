# Function that calculates the maximo divisor comum between 2 given numbers
# Which is a rule divised by Euclides to determine the maximum 

def mdc(a, b):
    while a % b > 0:
        r = a % b
        b = mdc(b, r)
    return b

    
a = int(input("First Value: "))
b = int(input("Second Value: "))
print(mdc(a, b))