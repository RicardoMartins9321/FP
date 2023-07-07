"""
Com 33 ovos, podemos encher 2 caixas de dúzia e sobram 9 ovos.
Complete o programa para calcular o número de dúzias e o resto
de qualquer número de ovos.
"""
n = int(input("Quantos ovos? "))
duzias = n // 12
n_sobra = n%12

print("Com", n, "ovos")
print("podes encher", duzias , "caixas")
print("e sobram", n_sobra , "ovos")
