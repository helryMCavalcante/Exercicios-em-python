totGasto = totProduto = menor = cont = 0
nomeProduto = ''
while True:
    print('-=-'*10,'SISTEMA DE CADASTRO DE PRODUTOS','-=-'*10)
    produto = str(input('Informe o produto: '))
    preço = float(input('Informe o valor do produto: '))
    cont += 1
    totGasto += preço
    if preço > 1000:
        totProduto += 1
    if cont == 1 or preço < menor:
        menor = preço
        nomeProduto = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja cadastrar mais produtos? [S / N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total gasto na compra foi de R$ {totGasto:.2f}, {totProduto} produtos custa acima de R$ 1000.00, sendo a(o) {nomeProduto} o produto de menor valor.')
print('-=-'*10)

