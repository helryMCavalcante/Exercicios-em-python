num = (int(input('Informe um valor: ')),
       int(input('Informe outro valor: ')),
       int(input('Informe mais um valor: ')),
       int(input('Informe o ultimo valor: ')),)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} veze(s)')
if 3 in num:
       print(f'O valor 3 apareceu na posição {num.index(3)+1}')
else:
       print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in num:
       if n % 2 == 0:
              print(f'{n} ', end='')