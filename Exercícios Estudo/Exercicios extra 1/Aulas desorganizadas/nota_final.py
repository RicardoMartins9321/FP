# Programa para calcular a nova nota final do aluno de FP
# CTP = (15% ATP1 + 15% ATP2) / 30%
# CP = (10% APx + 10% AP1 + 50% AP2) / 70%.
# NF = 30% CTP + 70% CP, desde que CTP >= 6.5 e CP >= 6.5.
# Se o aluno reprovar por nota mínima ou nota inferior a 10, o programa
# deve pedir as notas de recurso, ATPR e APR, e calcular a nova nota final

ATP1 = float(input("Avaliação do CTP1: "))
ATP2 = float(input("Avaliação do CTP2: "))
AP1 = float(input("Avaliação do CP1: "))
AP2 = float(input("Avaliação do CP2: "))


CTP = (0.15*ATP1 + 0.15*ATP2) * 0.3
CP =  (0.1*AP1 + 0.5*AP2 + 0.1*20) * 0.7

NF = CTP+CP

print("Nota final", NF)

