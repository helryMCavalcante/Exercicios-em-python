n = int(input('Informe um número'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
    print('{}'.format(c), end=' ')
print('\n O numero {} foi divisivel {} vezes'.format(n,tot))
if tot == 2:
    print('E por isso ele é um número primo')
else:
    print('E por isso ele não é um número primo')