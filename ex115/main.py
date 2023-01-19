from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'Curso em video.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Cadastrar usuário', 'Consulta', 'Sair'])
    if resp == 1:
        cabeçalho('NOVO CADASTRO.')
        nome = str(input('Nome: '))
        idade = leiaint('idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 2:
        lerArquivo(arq)
    elif resp == 3:
        cabeçalho('Saindo do sistema...até breve')
        break
    else:
        print('Opção invalida! Digite novamente.')
    sleep(2)


