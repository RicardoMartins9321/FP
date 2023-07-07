"""This function takes in a string "s" and initializes two variables: "i" to 0, 
and "prefixoEscolhido" (which means "chosen prefix" in Portuguese) to an empty string.

It then enters a while loop that runs as long as "i+1" is less than or equal to the difference between the length of the 
string "s" and "i+1" (which means that the loop runs while the index "i" is less than the length of the string "s" minus "i+1").

Inside the loop, the variable "prefixoSelecionado" (which means "selected prefix" in Portuguese) is assigned the value of the
substring of "s" from the first character to "i+1". The function then checks if "prefixoSelecionado" is present 
in the substring of "s" from "i+1" to the end. If it is, it assigns the value of "prefixoSelecionado" to "prefixoEscolhido".

After that, it increments the value of "i" by 1. Once the loop completes, the function returns the value of "prefixoEscolhido",
which is the longest prefix that is repeated somewhere else in the string "s".

It should be noticed that the function does not use the find method."""

def longestPrefixRepeated(s):
    i = 0 
    prefixoEscolhido = ""

    while (i+1 <= len(s)-(i+1)):
        prefixoSelecionado = s[0:(i+1)]
        if prefixoSelecionado in s[(i+1):]:
            prefixoEscolhido = prefixoSelecionado
        else:
            break
        i += 1
    return prefixoEscolhido


s = input("Write a string: ")
print("The longest repeated prefix was: ",longestPrefixRepeated(s))