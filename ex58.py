from random import randint
c = 1
jogador = int(input('Digite um número qualquer e tente adivinhar em qual número eu pensei: '))
computador = randint(0,10)
while computador != jogador:
    if jogador > computador:
        jogador = int(input('Menos...escolha um número novamente: '))
    elif jogador < computador:
        jogador = int(input('Mais...escolha um número novamente: '))
    c += 1

if c == 1:
    print('Parabéns! você acertou de primeira!')
else:
    print('Parabéns! você acertou!')
