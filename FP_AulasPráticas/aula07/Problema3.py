def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))


def filterPartName(contacts):
    dic = {}
    partName = input('Parte do nome: ')
    for numero, nome in contacts.items():
        if partName.lower() in nome.lower():
            dic[numero] = nome
    print('Dicionario \n', dic)


def add_contacto(contactos):
    nome = input('Nome: ')
    numero = input('Número: ')
    if numero in contactos:
        print('Este contacto já existe')
    else:
        morada = input('Morada: ')
        contactos[numero] = (nome, morada)


def remove_contacto(contactos):
    numero = input('Número: ')
    if numero not in contactos:
        print('Este número não existe')
    else:
        contactos.pop(numero)


def search_number(contactos):
    numero = input('Número: ')
    if numero not in contactos:
        print(numero)
    else:
        print(contactos[numero])


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()
    return op


def main():
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
                 "727392822": ("Cristiano Aveiro", "Portugal"),
                 "387719992": ("Maria Matos", "Nárnia"),
                 "887555987": ("Marta Maia", "Coimbra"),
                 "876111333": ("Carlos Martins", "Porto"),
                 "433162999": ("Ana Bacalhau", "Under the sea")
                 }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == 'A':
            add_contacto(contactos)
        elif op == 'R':
            remove_contacto(contactos)
        elif op == 'N':
            search_number(contactos)
        elif op == 'P':
            filterPartName(contactos)
        else:
            print("Não implementado!")


main()
