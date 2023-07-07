A1, A2 = input("Coordenadas de A: ").split( )
B1, B2 = input("Coordenadas de B: ").split( )

A1 = int(A1)
A2 = int(A2)
B1 = int(B1)
B2 = int(B2)

distance = ((B1-A1)**2 + (B2-A2)**2 ** 0.5)
print("A distância entre os pontos é: ", distance)
