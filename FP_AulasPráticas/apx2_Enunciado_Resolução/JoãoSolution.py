

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """

    CODIGO,NOME,SECCAO,PRECOBASE,TAXA = 0, 1, 2, 3, 4

    with open (fname, "r") as f:
        f.readline()

        for line in f:    
            produtos_lst = line.strip().split(";")
            produtos[produtos_lst[CODIGO]] = produtos_lst[NOME], produtos_lst[SECCAO], float(produtos_lst[PRECOBASE]), float(produtos_lst[TAXA].replace("%",""))/100
    
    return produtos


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """

    codigo = " "
    compras = {}

    while codigo != "":
        d = input("Code? ").strip().split(" ")
                                        
        codigo = d[0]                                                      #primeiro item da lista é o codigo

        if len(d)>1:                                                       #definir quantidade
            quantidade = int(d[1])
        else:
            quantidade = 1

        if codigo in produtos.keys():                                      #procurar o codigo na base de dados
            nome, _, preco, taxa = produtos[codigo]
            if codigo not in compras.keys():                               #adicionar quantidades
                compras[codigo] = quantidade
            else:
                compras[codigo] += quantidade

            print("{:s} {:d} {:.2f}".format(nome, quantidade, (preco + preco*taxa)*quantidade))

    return compras


        
def fatura(produtos, compras):
    """Imprime a fatura de uma dada compra."""

    total_bruto = 0
    total_iva = 0
    total_liquido = 0
    fatura_seccoes = {}                                                 #dicionário para fazer a fatura por secções

    for codigo, quantidade in compras.items():                          #ver o dicionário da função que regista as compras
        nome, seccao, preco, taxa = produtos[codigo] 
        preço_final = (preco + preco*taxa) * quantidade

        total_bruto += preco * quantidade
        total_iva += preco * taxa * quantidade                          #calcular diferentes preços pedidos
        total_liquido += preço_final

        if seccao not in fatura_seccoes.keys():                         #preencher dicionário para fazer a fatura por secções
            fatura_seccoes[seccao] = []         

        fatura_seccoes[seccao].append((quantidade, nome, int(taxa*100), preço_final))      

    for seccao, p1 in fatura_seccoes.items():                           #imprimir a fatura
        print(seccao)
        for p2 in p1:
            quantidade, nome, taxa, preço_final = p2
            print("{:d} {:s} ({:2d}%) {:.2f}".format(quantidade, nome, taxa, preço_final))

    print("Total Bruto: {:.2f}".format(total_bruto))
    print("Total IVA: {:.2f}".format(total_iva))
    print("Total Liquido: {:.2f}".format(total_liquido))



def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    faturas = []
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compras = registaCompra(produtos)
            faturas.append(compras)
            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
        # Acrescente outras opções aqui...
        elif op =="F":
            numero_compra = int(input("Numero compra? "))
            fatura(produtos, faturas[numero_compra-1])

        elif op == "S":
            repetir = False

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])