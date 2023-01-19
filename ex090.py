aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Informa a media do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print()
print('-=' * 20)
print(f'Nome do aluno é {aluno["nome"]}')
print(f'Sua nota foi {aluno["media"]}')
print(f'Sua situação atual é {aluno["situação"]}')
print('-=' * 20)