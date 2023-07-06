CTP = float(input('Nota CTP: '))
CP = float(input('Nota CP: '))
NF = CTP * 0.36 + CP * 0.64

if CTP < 6.5 or CP < 6.5:
    ATPR = float(input('Nota ATPR: '))
    APR = float(input('Nota APR: '))
    NF2 = max(CTP, ATPR) * 0.36 + max(CP, APR) * 0.64
    if NF2 < 9.5:
        print(f'Reprovado com média de {NF2:2f} valores')
    else:
        print(f'Aprovado com média de {NF2:.2f} valores')

else:
    print(f'Aprovado com média de {NF:.2f} valores')