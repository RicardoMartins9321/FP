def longestPrefixRepeated(s):
    i = 0 
    prefixoEscolhido = ""

    while (i+1 <= len(s)-(i+1)):
        prefixoSelecionado = s[0:(i+1)]
        if prefixoSelecionado in s[(i+1):]:
            prefixoEscolhido = prefixoSelecionado
        i += 1
    return prefixoEscolhido


def main():
    palavra = input("Escreve aqui a tua palavra: ")
    resultado = longestPrefixRepeated(palavra)
    if resultado == "":
        print("A palavra que introduziu não apresenta repetição de prefixos!")
    else:
        print("O maior prefixo da palavra que se repete é: {}.".format(resultado))


main()