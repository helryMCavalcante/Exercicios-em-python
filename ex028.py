from random import randint
from time import sleep
com = randint(0, 5)
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
p1 = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if com == p1:
    print('PARABÉNS! O NÚMERO QUE EU PENSEI FOI {}! VOCÊ ACERTOU!'.format(com))
else:
    print('Você errou! Eu pensei no número {} tente novamente...'.format(com))