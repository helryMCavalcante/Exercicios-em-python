primeiro = int(input('Primeiro: '))
razão = int(input('Razão: '))
termo = primeiro
opção = 10
cont = 1
total = 0
while opção != total:
    while cont <= 10:
        print('{}'.format(termo),end='')
        print(' -> ' if cont < 10 else ' = ',end='')
        termo += razão
        cont += 1
    opção = int(input('Deseja verificar mais algum termo: [Digite 0 para encerrar]'))

