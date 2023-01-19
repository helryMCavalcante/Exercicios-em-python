media = float(0)
somaIdade = float(0)
nomeHomem = ''
idadeHomem = 0
totMulheres = 0
for c in range(1, 5):
    nome = str(input('Informe o nome da {}º pessoa: '.format(c)))
    idade = int(input('Informe a idade da {}º pessoa'.format(c)))
    sexo = str(input('Informe o sexo da {}º pessoa'.format(c))).upper()
    if idade > idadeHomem and sexo == 'H':
        idadeHomem = idade
        nomeHomem = nome
    if idade < 20 and sexo == 'M':
        totMulheres += 1
    somaIdade += idade
media = somaIdade/4
print('A media de idade do grupo é de {:.1f}\nO nome do homem mais velho é {}\nHá um total de {} mulheres com idade menor que 20 anos'.format(media, nomeHomem,totMulheres))