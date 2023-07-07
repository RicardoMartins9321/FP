# programa para calcular o indice de imc
# e de seguida indicar a que categoria pertence
# IMC:          <18.5   [18.5, 25[  [25, 30[    30 ou mais 
# Categoria:    Magro   Saudável    Forte       Obeso 


m = float(input("Coloque aqui o seu peso (kg): "))
h = float(input("Coloque aqui a sua altura (m): "))
imc = m / (h*h)

if imc < 18.5:
    print("Categoria: Magro")
elif 18.5 <= imc < 25:
    print("Categoria: Saudavel")
elif 25 <= imc < 30:
    print("Categoria: Forte")
elif imc > 30:
    print("Categoria: Obeso")

else:
    print("Invalid Input! ")