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
