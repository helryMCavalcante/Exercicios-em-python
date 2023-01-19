import moeda
valor = float(input('Informe o preço do produto: '))
taxa = float(input('Informe a taxa: '))
print(f'O valor {valor}, com a taxa de {taxa}, passará a ficar no valor de {moeda.aumentar(valor,taxa)}')
print(f'O valor {valor}, com desconto de {taxa}, passará a ficar no valor de {moeda.diminuir(valor,taxa)}')
print(f'Metade do valor de {valor}, passará a ser {moeda.metade(valor)}')
print(f'O dobro do valor {valor}, passará a ficar no valor de {moeda.dobro(valor)}')
