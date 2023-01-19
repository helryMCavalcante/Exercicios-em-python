from random import randint
vitoria = 0
while True:
    jogador = int(input('Informe seu número jogador: '))
    com = randint(1, 10)
    soma = jogador + com
    JparImpar = ' '
    while JparImpar not in 'PI':
        JparImpar = str(input('Par ou Ímpar [P / I]: ')).upper()[0]
    print(f'Jogador escolheu {jogador} e o computador escolheu {com}. Total de {soma}', end= '')
    if JparImpar == 'P':
        if soma % 2 == 0:
            print(' Você venceu!')
            vitoria += 1
        else:
            print(' Você perdeu')
            break
    if JparImpar == 'I':
        if soma % 2 == 1:
            print(' Você venceu!')
            vitoria += 1
        else:
            print(' Você perdeu!')
            break
print(f'Você acertou {vitoria} vezes')
print('GAME OVER')

