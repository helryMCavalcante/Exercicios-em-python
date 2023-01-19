import random
from time import sleep
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Selecione umas das opções: '))
computador = random.randint(0,2)

if computador == 0 and jogador == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('''Computador escolheu Pedra\nJogador escolheu Tesoura''')
    print('COMPUTADOR VENCEU')
elif computador == 0 and jogador == 1:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('''Computador escolheu Pedra\nJogador escolheu Papel''')
    print('JOGADOR VENCEU')
elif computador == 1 and jogador == 0:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('''Computador escolheu Papel\nJogador escolheu Pedra''')
    print('COMPUTADOR VENCEU')
elif computador == 1 and jogador == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('''Computador escolheu Papel\nJogador escolheu Tesoura''')
    print('JOGADOR VENCEU')
elif computador == 2 and jogador == 1:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('''Computador escolheu Tesoura\nJogador escolheu Papel''')
    print('COMPUTADOR VENCEU')
elif computador == 2 and jogador == 0:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('''Computador escolheu Tesoura\nJogador escolheu Pedra''')
    print('JOGADOR VENCEU')
elif computador == 0 and jogador == 0:
    print('EMPATE')
elif computador == 1 and jogador == 1:
    print('EMPATE')
elif computador == 2 and jogador == 2:
    print('EMPATE')
elif jogador >=3:
    print('Opção invalida')