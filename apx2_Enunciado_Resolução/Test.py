# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """

    with open(fname, "r") as text:
        text.readline() # Gets rid of the first line of the text file

        for line in text:
            words = line.strip().split(";")
            words[-1] = float(words[-1].replace("%","")) / 100
            produtos[words[0]] = (words[1],words[2],float(words[3]),float(words[4]))
        
    return produtos


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    
    compras = {}
    code = " "

    while code != "":
        code_and_quantity = input("Code? ").strip().split(" ")
        code = code_and_quantity[0]

        if len(code_and_quantity) > 1:
            quantity = int(code_and_quantity[1])
        else:
            quantity = 1

        if code in produtos.keys():
            name, _, base_price, tax = produtos[code]

            if code not in compras.keys():
                compras[code] = quantity
            else:
                compras[code] += quantity

            final_price = (base_price + base_price*tax) * quantity

            print(f"{name:s} {quantity:d} {final_price:.2f}")

    return compras


def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""

    gross_total = 0
    total_IVA = 0
    net_total = 0
    faturas_separadas = {}

    for code, quantity in compra.items():                          #ver o dicionário da função que regista as compras
        name, section, base_price, tax = produtos[code] 
        final_price = (base_price + base_price*tax) * quantity

        gross_total += base_price * quantity
        total_IVA += base_price * tax * quantity                          #calcular diferentes preços pedidos
        net_total += final_price

        if section not in faturas_separadas.keys():                         #preencher dicionário para fazer a fatura por secções
            faturas_separadas[section] = []         

        faturas_separadas[section].append((quantity, name, int(tax*100), final_price))      

    for section, p1 in faturas_separadas.items():                           #imprimir a fatura
        print(section)
        for p2 in p1:
            quantity, name, tax, final_price = p2
            print(f"{quantity:d} {name:s} ({tax:2d}%) {final_price:.2f}")

    print(f"Total Bruto: {gross_total:.2f}")
    print(f"Total IVA: {total_IVA:.2f}")
    print(f"Total Liquido: {net_total:.2f}")

def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos) # mudei isto
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repeat = True
    num_faturas = []
    while repeat:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            num_faturas.append(compra)
        elif op == "F":
            num_compra = int(input("Numero compra? "))
            fatura(produtos, num_faturas[num_compra-1]) 
        elif op == "S":
            break

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
