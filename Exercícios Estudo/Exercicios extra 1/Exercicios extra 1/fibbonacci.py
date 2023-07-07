"""
The Fibonacci sequence starts with the numbers 0 and 1. Then each consecutive
element of the sequence is obtained by the sum of the two previous elements.
Complete the genFibonacci(n) function to _return_ a list of the first n
Fibonacci numbers. For example, if n=6, it should return [0, 1, 1, 2, 3, 5].
The function only has to work for n>=2.
"""

# made with while loops
def genFibonacci(n):
   assert n >= 2
   i = 1
   fib = [0,1]
   
   while i < (n - 1):
      fib.append(fib[i] + fib[i-1])
      i += 1

   return fib
   
# made with recursion
def genFibonacci2(n):
   if n == 2:
      return [0, 1]
   else:
      fib_list = genFibonacci(n-1)
      fib_list.append(fib_list[-1] + fib_list[-2])
   return fib_list


userInput = int(input("How many fibonacci numbers do you want: "))
print(genFibonacci(userInput))
print(genFibonacci2(userInput))
