listagem = ('Lápis', 1.75,'Caderno', 5.00,'Caneta', 2.50,'Estojo',25.00,'Compasso',9.99,'Mochila',50.00)
print('-=-'*17)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-=-'*17)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}R$', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')
print('-=-'*17)