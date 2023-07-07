#programa para verificar se um numero é par

n = int(input("Escolha o número: "))

par = n%2

if par == 0:
    print(n, "é um número par")

elif par != 0: 
    print(n, "não é um número par")

else: print("Invalid input")