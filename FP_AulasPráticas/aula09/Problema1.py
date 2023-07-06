with open('pg3333.txt', 'r', encoding='utf-8') as file:
    letters = {}
    for line in file:
        for letter in line:
            if letter.isalpha():
                letetr = letter.lower()
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1

for x in sorted(letters, key=lambda x: letters[x], reverse=True):
    print(x, letters[x])


""" with open('pg3333.txt', 'r', encoding='utf-8') as file:
    palavras = {}
    for line in file:
        for word in line.split():
            if word not in palavras:
                palavras[word] = 1
            else:
                palavras[word] += 1

for x in sorted(palavras, key=lambda x: palavras[x]):
    print(x + ':', palavras[x])
 """
