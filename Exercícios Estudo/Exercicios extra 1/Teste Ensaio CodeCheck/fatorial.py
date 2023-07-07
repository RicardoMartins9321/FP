"""
Complete a função factorial(n) para calcular e devolver o factorial de n.
Use uma instrução de repetição for ou while.
Recorde que n! = 1*2*3*...*n, para n>=1, e 0! = 1, por definição.
A função só aceita argumentos inteiros não negativos.
"""

def factorial(n):
   assert isinstance(n, int), "n should be an int"
   assert n >= 0            , "n should not be negative"
   factorial = 1
   for i in range(1, n+1):
      factorial *= i

   return factorial
