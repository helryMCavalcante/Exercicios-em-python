from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('O aluno tem {} anos, sua categoria é Mirim.'.format(idade))
elif 14 >= idade >= 10:
    print('O aluno tem {} anos, sua categoria é infantil.'.format(idade))
elif 19 >= idade >= 15:
    print('O alino tem {} anos, sua categoria é júnior.'.format(idade))
elif 25 >= idade >=20:
    print('O aluno tem {} anos, sua categoria é sênior.'.format(idade))
else:
    print('O aluno tem {} anos, sua categoria é de master.'.format(idade))