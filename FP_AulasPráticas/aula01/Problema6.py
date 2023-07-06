import math
# Calcular a hipotenusa
a = float(input('Comprimento do cateto A: '))
b = float(input('Comprimento do cateto B: '))
h2 = float(a**2 + b**2)
h = float(math.sqrt(h2))

# Calcular o ângulo
cos = float(a/h)
ang1 = float(math.acos(cos))
ang = float(math.degrees(ang1))

print(f'A hipotenusa do trinângulo é {h}')
print(f'O valor do ângulo é {ang} graus')
