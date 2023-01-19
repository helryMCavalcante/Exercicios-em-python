resp = sexo = ' '
totIdade = totSexo = totMulheres =0
while True:
    nome = str(input('Informe o nome do usuário: ')).strip().upper()
    idade = int(input('Informe a idade do usuário: '))
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo do usuário [M/F]: ')).strip().upper()[0]
    if idade > 18:
        totIdade += 1
    if sexo == 'M':
        totSexo += 1
    if sexo == 'F' and idade < 20:
        totMulheres += 1
    while resp not in 'SN':
        resp = str(input('Deseja continuar o cadastro [S / N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de acima de 18 anos {totIdade}, total {totSexo} masculinos cadastrados e total de {totMulheres} abaixo dos 20 anos.')
