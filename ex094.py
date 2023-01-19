galera= []
pessoas = {}
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar? [S / N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite S ou N')
    if resp == 'N':
        break
print(f'Ao todo um total de {len(galera)} pessoas estão cadastradas no sistema.')
media = soma / len(galera)
print(f'A media total das idades é de {media:5.2f}')
print('As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end="")
print()
print('Lista de pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
print()