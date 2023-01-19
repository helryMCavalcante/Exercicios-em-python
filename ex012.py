produto = float(input('Informe o preço do produto: '))
desc = produto - (produto*0.05)
print('O produto que custava {} R$, na promoção com 5% de desconto custar {:.2f} R$'.format(produto, desc))