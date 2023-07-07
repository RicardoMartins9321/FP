"""
Crie uma função que conte quantos dígitos há numa dada string.
Por exemplo:  countDigits("23 mil 456") deve devolver 5.
Sugestão: o método isdigit verifica se uma string só tem dígitos,
e.g., "2".isdigit() -> True.
"""

# Defina a função aqui.
def countDigits(text):
   n = 0
   for i in text:
      if i in ("0","1","2","3","4","5","6","7","8","9"):
         n+=1
   return n

def main():
   str = input()
   print("str:", repr(str))
   print("result:", countDigits(str) )

if __name__ == "__main__":
   main()
