

def aumentar(preço=0, taxa=0, format=False):
    aum = preço + (preço * taxa/100)
    return aum if format is False else moeda(aum)


def diminuir(preço=0, taxa=0,format=False):
    dim = preço - (preço * taxa/100)
    return dim if not format else moeda(dim)


def metade(preço=0,format=False):
    met = preço / 2
    return met if not format else moeda(met)


def dobro(preço=0,format=False):
    dob = preço * 2
    return dob if not format else moeda(dob)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0,aum=0,desc=0):
    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'A metade do valor: \t{metade(preço, True)}')
    print(f'O dobro do valor: \t{dobro(preço, True)}')
    print(f'O valor com a taxa de {aum:.0f}%: \t{aumentar(preço, aum, True)}')
    print(f'O valor com desconto de {desc:.0f}%: \t{diminuir(preço, desc, True)}')
    print('-' * 30)