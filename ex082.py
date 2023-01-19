lista = []
listaA = []
listaB = []
while True:
    lista.append(int(input('Informe um valor: ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
for v in lista:
    if v % 2 == 0:
        listaA.append(v)
    else:
        if v % 2 == 1:
            listaB.append(v)
print(f'Lista com o total de todos os valores: {lista}\nLista com apenas valores pares:  {listaA}\nLista com apenas valores impares: {listaB}')