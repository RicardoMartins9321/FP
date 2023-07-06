litros = float(input('Litros: '))
preço = float(litros * 1.4)
if litros <= 40:
    print('Preço:', preço, '€')
if litros > 40:
    valor = float(preço - (0.1 * preço))
    print('Preço:', preço, '€')
