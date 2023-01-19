from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os numeros sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado é {max(numeros)}')
print(f'O menor valor sorteado pe {min(numeros)}')