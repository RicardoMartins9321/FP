"""
This function uses a helper function reverseAux which takes two arguments:
- n: the input integer that needs to be reversed
- reversed_n: an auxiliary variable that will store the reversed integer as the function recursively calls itself

The reverseAux function works by recursively dividing the input integer by 10 (removing the last digit)
and adding the last digit to the reversed_n variable. This is done by multiplying reversed_n by 10 and adding the last digit (n % 10).

When n becomes 0, the function returns the reversed_n variable.

The outer function reverseDigits simply calls the reverseAux function with the input integer and an initial reversed_n value of 0.

It uses recursion and mod and floor division operator to reverse the digits of an integer."""

def reverseAux(n, reversed_n):
    if n == 0:
        return reversed_n
    else:
        return reverseAux(n // 10, reversed_n * 10 + n % 10)

def reverseDigits(n):
    return reverseAux(n, 0)

print(reverseDigits(1234))
