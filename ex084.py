lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome do usuário: ')))
    dados.append(float(input('Informe o peso do usuário: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar o cadastro? [S/N]')).upper()
    if resp in 'N':
        break

print(f'Foram cadastradas o total de {len(lista)} usuários')
print(f'O maior peso tem o valor de {maior}kg', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso tem o valor de {menor}kg', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}')
