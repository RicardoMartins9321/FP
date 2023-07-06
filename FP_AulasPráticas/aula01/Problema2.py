# Calcular a velocidade media do automovel
v1 = int(input('What\'s the first velocity? '))
v2 = int(input('What\s the second velocity? '))

# d = v*t ; d = v1 * t1 ; d = v2 * t2; v1t1 = v2t2 , t1 = (v2/v1)t2
# vm = d*2 / (t1+t2) = 2d/((d/v1)+(d/v2)) = (2(v1v2))/(v1+v2)

vm = int(2 * ((v1*v2)/(v1+v2)))

print(f'Your average speed was {vm}km/h')
