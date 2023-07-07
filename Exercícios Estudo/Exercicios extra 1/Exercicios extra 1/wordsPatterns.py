# ID: 

"""
Imagine que está a fazer palavras cruzadas (em Inglês) e falta-lhe uma
palavra com o padrão "?YS???Y", onde os "?" representam letras por preencher.
Complete este programa para o ajudar a descobrir a palavra.
O programa já inclui instruções para ler uma lista de palavras inglesas a
partir do ficheiro wordlist.txt.
"""

# This function reads words from a file.
def load(fname):
   with open(fname) as f:
      lst = []
      for line in f:
         # loads words separated and without withespaces into a list
         words = line.strip().split()
         lst.extend(words)
   return lst


""" a)
Complete a função matchesPattern(s, pattern) para devolver
True se s corresponder ao padrão fornecido e False, no caso contrário.
Uma string s corresponde ao padrão se e só se tiver os mesmos carateres
que o padrão nas mesmas posições, exceto onde o padrão tem ?.
Nas posições dos ?, não importa que carateres estão na string s.
A correspondência não deve fazer distinção entre maiúsculas e minúsculas.
"""
def matchesPattern(s, pattern):
   num_car = 0
   num_verified = 0
   
   # checks the word for further parameters if the lengths of both words are equal
   if len(s) == len(pattern):
      for i in s.lower():
         if i == pattern[num_car].lower() or pattern[num_car] == "?":
            num_verified += 1
         num_car += 1

   # returns False as it doesn't verify the base requirement      
   else:
      return False

   # verifies and returns whether all the chars in the word were correct or not   
   return(num_verified == len(s))

""" b)
Complete a função filterPattern(lst, pattern) para extrair duma lista de strings
as strings que têm o padrão dado.
Sugestão: use a função matchesPattern para testar cada palavra.
"""
def filterPattern(lst, pattern):
   strings = []
   num = 0

   # appends the words loaded from the text file that verify the pattern
   for i in range(len(lst)):
      if matchesPattern(lst[num], pattern):
         strings.append(lst[num])
         
      num += 1
         
   return strings
   


def main():
   print("a)")
   print( matchesPattern("secret", "s?c??t") )  #-> True
   print( matchesPattern("secreta", "s?c??t") ) #-> False
   print( matchesPattern("socket", "s?c??t") )  #-> True
   print( matchesPattern("soccer", "s?c??t") )  #-> False
   print( matchesPattern("SEcrEt", "?ecr?t") )  #-> True
   print( matchesPattern("SEcrET", "?ecr?t") )  #-> True
   print( matchesPattern("SecrEt", "?ECR?T") )  #-> True

   words = load("Exercícios estudo\Exercicios extra 1\wordlist.txt")

   print("b)")
   # Solution to "S?C??T"
   lst = filterPattern(words, "s?c??t") #-> ['sachet', 'secret', 'socket']
   print(lst)

   assert isinstance(lst, list),  "result lst should be a list"
   assert "secret" in lst,  "result should contain 'secret'"

   # Solution to "?YS???Y"
   lst = filterPattern(words, "?ys???y") #-> ['mystery', 'mystify']
   print(lst)


# Call main function:
if __name__ == "__main__":
   main()