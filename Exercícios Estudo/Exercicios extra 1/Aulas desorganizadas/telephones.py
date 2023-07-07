
tellList = ["975318642", "234000111", "777888333", "913672834", "933406580"]
nameList = ["Angelica", "Brad", "Claudia", "João", "Ana"]

# Function that checks whether or not a name is inside the 
# telephone list and if it is not, the function adds it to the list
def telToName():
    n = 0
    n_tel = input("Escreva o número de telemovel: ")
    for i in tellList:
        if i == n_tel:
            print(i, "-", nameList[n])
        n = n+1
    else: 
        print("Novo contacto", n_tel)
        
telToName()

nomes_associados = []

def nameToTels():
    parte_nome = input("Escreva o nome: ")
    for i in nameList:
        if parte_nome.lower() == i[0: len(parte_nome)].lower():
            nomes_associados.append(i)
    print("Contactos possiveis:", nomes_associados)

nameToTels()