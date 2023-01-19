primeiro = int(input('Primeiro'))
razão = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 10:
    print('{}'.format(primeiro), end='')
    print(' -> ' if c < 10 else ' = ',end='')
    primeiro += razão
    c += 1
print('Acabou')