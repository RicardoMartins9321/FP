# programa para calcular o custo de uma chamada


tempo_cham = int(input("Qual a duração da chamada (em segundos): "))

if tempo_cham <= 60:
    custo = 0.12

elif tempo_cham >60:
    custo_segundos = 0.12/60
    s = tempo_cham - 60             
    custo = 0.12 + s*custo_segundos

else: print("Invalid Input!")

print("A tua chamada teve um custo de", custo,"$")