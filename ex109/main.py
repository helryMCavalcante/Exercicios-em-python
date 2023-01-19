import moeda
valor = float(input('Informe o preço do produto: '))
taxa = float(input('Informe a taxa: '))
print(f'O valor {moeda.moeda(valor)} com a taxa de {taxa:.0f}%, passará a ficar no valor de {moeda.aumentar(valor, taxa, True)}')
print(f'O valor {moeda.moeda(valor)} com desconto de {taxa:.0f}%, passará a ficar no valor de {moeda.diminuir(valor, taxa, True)}')
print(f'Metade do valor de {moeda.moeda(valor)} passará a ser {moeda.metade(valor, True)}')
print(f'O dobro do valor {moeda.moeda(valor)} passará a ficar no valor de {moeda.dobro(valor, True)}')
