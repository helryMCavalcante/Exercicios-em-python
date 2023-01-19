sexo = str(input('Informe o sexo do usuário. Utilize [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Opção invalida, digite novamente.')
    sexo = str(input('Informe o sexo do usuário. Utilize [M/F]: ')).strip().upper()
print('Você selecionou {}.'.format(sexo))