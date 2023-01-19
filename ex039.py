from datetime import date
nasc = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade > 18:
    print('Você possui {} anos, você excedeu o tempo de alistamento em {} ano(s). Procure uma junta militar imediatamente!'.format(idade, idade - 18))
elif idade < 18:
    print('Você possi {} anos, ainda faltam {} anos para o alistamento.'.format(idade, 18 - idade))
else:
    print('Você possui {} anos, procure que uma junta militar para realizar o alistamento.'.format(idade))