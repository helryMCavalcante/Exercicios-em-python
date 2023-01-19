numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
         numeros.append(n)
         print('Valor adicionado com sucesso.')
    else:
         print('Valor duplicado, não será adicionado...')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print(f'Os valores informados foram {numeros}')
