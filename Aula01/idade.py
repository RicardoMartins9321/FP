nome = input("Como te chamas? ")
ano = int(input("Em que ano nasceste? "))
idade = 2030-ano

if 1900 < ano <2030:
    resposta = print(nome, "fará", idade, "anos em 2030")
else:
    print("Por favor introduza um valor válido")

