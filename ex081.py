lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break

print(f'Os valores informados são: {lista}.')
lista.sort(reverse=True)
print(f'Em ordem decrescente ficam:  {lista}.')
print(f'Total de números digitados foram {len(lista)}.')
if 5 in lista:
    print(f'O valor 5 está dentro da lista.')
else:
    print('O valor 5 não está na lista.')

