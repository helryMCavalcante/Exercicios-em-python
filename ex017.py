import math
catop = float(input('Comprimento do cateto oposto: '))
cataj = float(input('Comprimento do cateto adjacente: '))
hipt = math.hypot(catop, cataj)
print('A hipotenusa vai medir: {:.2f}'.format(hipt))
