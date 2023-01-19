def aumentar(preço, taxa):
    aum = preço + (preço * taxa/100)
    return f'R${aum:.2f}'

def diminuir(preço, taxa):
    dim = preço - (preço * taxa/100)
    return f'R${dim:.2f}'

def metade(preço):
    met = preço / 2
    return f'R${met:.2f}'

def dobro(preço):
    dob = preço * 2
    return f'R${dob:.2f}'