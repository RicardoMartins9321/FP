d = {'abc': 123, 'xyz': 456, 'klm': 789}
x = 'klm'
if x in d:
    print(x, '-', d[x], sep='')
else:
    print('Something')
d['olx'] = 999
l1 = list(d.keys())
x = 'x'
for k in l1:
    if x in k:
        print(k, '-', d[k], sep='', end=',')
print()
# procura de um numero no dicionário (valor)
l2 = list(d.values())
x = 123
for i in range(len(l2)):
    if x == l2[i]:
        print(l1[i], '-', x, sep='', end=',')
print()
