def media():
    total = 0.0
    p = 0
    while True:
        n = input('Number: ')
        p += 1
        if n == '':
            break
        valor = float(n)
        total = total + valor
        media = total / p
    return media


print(media())
