# Calcular a distancia entre pontos
import math
x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

dist = float(math.dist([x1, y1], [x2, y2]))
print(dist)
