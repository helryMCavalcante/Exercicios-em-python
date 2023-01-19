import math
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando as notas {:.1f} e {:.1f} a media do aluno foi de {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('Alunos reprovado!')
elif 7 > media >= 5:
    print('Aluno está de recuperação!')
else:
    print('Aluno está aprovado!')