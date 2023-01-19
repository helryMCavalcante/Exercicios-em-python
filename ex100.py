from random import randint
from time import sleep

def sorteia(lst):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(1,6):
        n = randint(1,10)
        lst.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')
def somaPar(lst):
    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pares de {lst}, temos: {s}')
    print('-=' * 30)


números = []
sorteia(números)
somaPar(números)